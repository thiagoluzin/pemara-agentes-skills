---
name: audio-analysis
description: "Mede níveis, espectro, dinâmica, transientes e problemas de silêncio em áudio usando a fonte e a janela temporal indicadas."
---

# Skill: Análise de Áudio (ler o som)

Meça, não chute. Instale: `pip install librosa soundfile numpy pyloudnorm` (+ `ffmpeg` no sistema).

## Inspecionar (sempre primeiro)
```python
import soundfile as sf, numpy as np
info = sf.info("audio.wav")
print(info.samplerate, info.channels, info.frames/info.samplerate, "s", info.subtype)
```

## Carregar + métricas básicas
```python
import librosa, numpy as np
y, sr = librosa.load("audio.wav", sr=None, mono=True)
print("dur:", round(len(y)/sr,3), "s | sr:", sr)
print("pico:", float(np.max(np.abs(y))), "(>=1.0 => clipping)")
print("RMS médio:", float(np.sqrt(np.mean(y**2))))
```

## BPM / tempo e batidas
```python
tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
print("BPM:", float(tempo), "| nº batidas:", len(beats))
```

## Tom / key (estimativa por chroma)
```python
chroma = librosa.feature.chroma_cqt(y=y, sr=sr).mean(axis=1)
notas = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
print("nota dominante:", notas[int(chroma.argmax())])
```

## Loudness (LUFS — padrão de broadcast/jogo)
```python
import pyloudnorm as pyln, soundfile as sf
data, rate = sf.read("audio.wav")
lufs = pyln.Meter(rate).integrated_loudness(data)
print("LUFS integrado:", round(lufs,2))   # ex.: alvo de jogo ~ -16 a -23 LUFS
```

## Silêncio / onsets (cortes, ataques)
```python
intervals = librosa.effects.split(y, top_db=30)        # trechos não-silenciosos
onsets = librosa.onset.onset_detect(y=y, sr=sr, units='time')
print("nº trechos com som:", len(intervals), "| nº onsets:", len(onsets))
```

## Espectrograma / waveform (inspeção visual)
```python
import numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt, librosa.display
S = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)
plt.figure(figsize=(10,4)); librosa.display.specshow(S, sr=sr, x_axis='time', y_axis='log')
plt.colorbar(); plt.tight_layout(); plt.savefig("spectro.png")   # abra a imagem pra ver
```

## Conversão / normalização (ffmpeg)
```bash
ffmpeg -i in.mp3 -ar 44100 -ac 2 out.wav                      # resample/canais
ffmpeg -i in.wav -af loudnorm=I=-16:TP=-1.5:LRA=11 out.wav     # normalizar loudness
ffmpeg -i in.wav -af silenceremove=1:0:-50dB out.wav          # tirar silêncio no início
```

## Avançado (ponteiros)
- **Transcrição**: `faster-whisper` / `openai-whisper` → texto + timestamps.
- **Stems (separar voz/instrumentos)**: `demucs` (`python -m demucs audio.wav`).
- **DSP forense**: filtros, denoise, espectro fino com `scipy.signal`.

## Notas
- Mono pra análise de BPM/tom; preserve estéreo pra loudness/mix.
- `sr=None` mantém o sample rate original (não reamostra à toa).
- Clipping (pico ≥ 1.0 / 0 dBFS) é defeito — reganhe headroom antes de exportar.
