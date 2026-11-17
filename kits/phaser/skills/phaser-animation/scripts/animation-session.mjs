/**
 * One owned Phaser animation session; not a gameplay state machine.
 * Markers use Phaser's one-based AnimationFrame.index, once per repeat cycle.
 * A yoyo forward/backward pair is one cycle. Skipped render frames do not imply hits.
 * External play (even same key), stop and destruction end ownership.
 * Phaser may report an external replacement as 'stopped' before its new start.
 * Supports global string-key animations; mixes, local animations and chains need an adapter.
 * onEnd reports a reason; the gameplay controller chooses the next state.
 * Callbacks should enqueue transitions rather than synchronously replay animations.
 */
export function playAnimation(sprite, key, { markers = [], onMarker = () => {}, onEnd = () => {} } = {}) {
  if (!sprite.anims.animationManager.exists(key)) throw new Error(`Unknown animation: ${key}`);
  const ids = new Set();
  for (const marker of markers) {
    if (!marker || typeof marker.id !== 'string' || !marker.id || ids.has(marker.id)
      || !Number.isInteger(marker.frame) || marker.frame < 1) throw new Error('Invalid/duplicate marker');
    ids.add(marker.id);
  }
  // Stop the previous session before registering this one's same-key listeners.
  sprite.stop();
  let ended = false;
  let starting = true;
  let cycle = 0;
  const fired = new Set();
  const listeners = [];
  const listen = (event, fn) => { listeners.push([event, fn]); sprite.on(event, fn); };
  const finish = (reason, stop = false) => {
    if (ended) return;
    ended = true;
    for (const [event, fn] of listeners) sprite.off(event, fn);
    fired.clear();
    if (stop && sprite.anims?.currentAnim?.key === key) sprite.stop();
    onEnd(reason);
  };
  const visit = (animation, frame) => {
    if (ended || animation.key !== key || !frame) return;
    for (const marker of markers) {
      if (ended) break;
      if (marker.frame === frame.index && !fired.has(marker.id)) {
        fired.add(marker.id);
        onMarker({ id: marker.id, cycle, frame: frame.index });
      }
    }
  };
  listen('animationstart', (animation, frame) => {
    if (starting && animation.key === key) {
      starting = false;
      visit(animation, frame);
    } else finish('replaced');
  });
  listen('animationupdate', visit);
  listen('animationrestart', () => finish('restarted'));
  listen('animationrepeat', (animation, frame) => {
    if (animation.key !== key || ended) return;
    cycle += 1;
    fired.clear();
    visit(animation, frame);
  });
  listen('animationcomplete', animation => { if (animation.key === key) finish('complete'); });
  listen('animationstop', animation => { if (animation.key === key) finish('stopped'); });
  listen('destroy', () => finish('destroyed'));
  try {
    sprite.play(key);
  } catch (error) {
    finish('error');
    throw error;
  }
  return {
    get ended() { return ended; },
    cancel() {
      if (ended) return;
      // Detach before stopping; cancellation emits one termination reason.
      finish('cancelled', true);
    }
  };
}
