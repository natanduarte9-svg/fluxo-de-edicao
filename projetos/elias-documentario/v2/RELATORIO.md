# Versão 2 — relatório (23/11/2026)
- **Vídeos usados (os 6, na ordem):** clipe1 Elias diante de Acabe · clipe2 ribeiro e corvos · clipe3 fogo no Carmelo · clipe4 anjo no deserto · clipe5 manto sobre Eliseu · clipe6 carruagem subindo no redemoinho. Todos 10 s, 9:16 (1 em 1080×1920, 5 em 1440×2560), HEVC 30 fps, com áudio (removido).
- **Movimento original preservado:** sem zoom artificial, sem efeito sobre os personagens. Cada clipe foi esticado para caber na fala com **câmera lenta por fluxo óptico** (ffmpeg `minterpolate` mci): fatores 1,02 / 1,14 / 1,70 / 1,29 / 1,14 / 1,52.
- **Encerramento:** último quadro da subida (carruagem sumindo no redemoinho), leve aproximação, brasas, fundo escurecido.
- **Voz:** Antonio, +8% (o prompt pedia 60–70 s; o texto inteiro em ritmo natural dá 84 s de fala → 86,7 s no total).
- **Som:** trilha original (piano Salamander + orquestra VSCO/VCSL) refeita no novo tempo; ducking a 15% da voz; ambiente sintetizado (riacho, fogo, vento).
- **Saída:** `documentario_historia_de_elias.mp4`, 1080×1920, H.264 + AAC, −14,0 LUFS, pico −1,4 dB, sem telas pretas. Legendas `.srt` (92 blocos).
- Pastas de trabalho: `/home/user/projeto_elias/` (videos_originais somente leitura, audio, legendas, temporarios, exportacao).
