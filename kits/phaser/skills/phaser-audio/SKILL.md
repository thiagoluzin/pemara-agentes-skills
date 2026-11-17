---
name: phaser-audio
description: "Medir e integrar música e SFX no Phaser/Web Audio, corrigindo loops, ducking, transições, desbloqueio e recursos duplicados."
---

# Áudio de jogos Phaser

Leia o gerenciador existente e siga a cadeia arquivo → decode → source → gains → saída. Identifique dono, relógio e descarte dos nós. Não crie um segundo player na cena para resolver defeito no gerenciador.

Para análise, registre duração, canais, sample rate e formato. Meça loudness, sample peak e true peak com ferramentas disponíveis; preserve estéreo para medir mix e soma mono. Um pico de amostra em full scale é indício, não prova isolada de clipping audível. Nota dominante de chroma não determina tonalidade. BPM pode ter ambiguidade de metade/dobro; confirme a grade e o offset por escuta e onsets.

Não imponha LUFS universal para jogos nem normalize todos os masters sem medir a saída. Volume final resulta de várias camadas de ganho. Para loop, avalie continuidade de amplitude, energia e fase, e ouça a emenda; zero crossing sozinho não assegura transição suave.

Ducking sobreposto deve restaurar o estado efetivo preservando preferência do usuário, mute e intensidade. Decode antigo não pode vencer pedido de música mais recente. Troca de fase descarta recursos obsoletos e não deixa fade de uma música afetar a seguinte.

Stems exigem início no mesmo relógio e limites de loop compatíveis; chamadas consecutivas de play não garantem sincronismo. Pitch/rate são escolhas de design e podem mudar duração. Não varie sinais musicais ou telegraphs sem intenção.

Áudio acompanha contato e estados, mas não deve pausar/retomar física por conta própria. Defina o dono de hitstop no sistema de gameplay. Teste gesto inicial, contexto suspenso, mute/opções, pausa, foco, derrota, reinício e várias fases na mesma cena. Ouça a saída em contexto e capture evidência quando possível.

Ferramentas como FFmpeg/ffprobe, soundfile, librosa e pyloudnorm são opcionais conforme a medida. Verifique disponibilidade e versão; não instale toda a cadeia para ler a duração de um arquivo. Informe métricas ausentes, estimativas e qualidade de mix ainda não avaliada.
