/** Pure input timing policy. Call once per simulation step, time in milliseconds.
 * grounded must reflect contacts; jumpPressed is a press edge, not a held button.
 * Rearming requires leaving the ground after a jump, then landing.
 */
export class JumpWindow {
  constructor({ coyoteMs = 90, bufferMs = 100, jumpSpeed = 240, cutFactor = 0.45 } = {}) {
    if (![coyoteMs, bufferMs, jumpSpeed, cutFactor].every(Number.isFinite)
      || coyoteMs < 0 || bufferMs < 0 || jumpSpeed <= 0 || cutFactor <= 0 || cutFactor > 1) {
      throw new Error('Invalid jump parameters');
    }
    Object.assign(this, { coyoteMs, bufferMs, jumpSpeed, cutFactor });
    this.reset();
  }
  reset() {
    this.lastTime = -Infinity;
    this.lastGround = -Infinity;
    this.lastPress = -Infinity;
    this.jumped = false;
    this.leftGround = false;
    this.cut = false;
  }
  step({ time, grounded, jumpPressed, jumpHeld, velocityY }) {
    if (!Number.isFinite(time) || !Number.isFinite(velocityY) || time < this.lastTime) throw new Error('Invalid clock or velocity');
    this.lastTime = time;
    if (!grounded) this.leftGround = true;
    if (grounded && this.leftGround) {
      this.jumped = false;
      this.leftGround = false;
    }
    if (grounded && !this.jumped) this.lastGround = time;
    if (jumpPressed) this.lastPress = time;
    let didJump = false;
    if (!this.jumped && time - this.lastGround <= this.coyoteMs && time - this.lastPress <= this.bufferMs) {
      velocityY = -this.jumpSpeed;
      this.jumped = true;
      this.leftGround = false;
      this.cut = false;
      this.lastPress = -Infinity;
      this.lastGround = -Infinity;
      didJump = true;
    }
    if (this.jumped && !jumpHeld && !this.cut && velocityY < 0) {
      velocityY *= this.cutFactor;
      this.cut = true;
    }
    return { didJump, velocityY };
  }
}
