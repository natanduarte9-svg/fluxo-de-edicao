"""Narração (Antonio) por cena. Cada cena pode ter partes com pausa dramática entre elas.
Gera voz/f<k>.wav (partes juntas com silêncio) e voz/words.json com o tempo de cada palavra.
Confere se nenhuma fala veio cortada (edge-tts às vezes corta) e refaz a parte que falhou."""
import asyncio, os, json, sys, subprocess, edge_tts, numpy as np, soundfile as sf
VOZ = os.environ.get("VOZ", "pt-BR-AntonioNeural"); RATE = sys.argv[1] if len(sys.argv) > 1 else "+5%"
CENAS = [
 [("Por anunciarem o Evangelho, Paulo e Silas foram acusados injustamente, espancados e lançados na prisão. Seus pés foram presos ao tronco, e tudo parecia indicar que aquela seria uma noite de sofrimento.", 0)],
 [("Mas, por volta da meia-noite, algo extraordinário aconteceu. Mesmo feridos e acorrentados, Paulo e Silas oravam e cantavam louvores a Deus. E os outros presos os escutavam.", 0)],
 [("De repente, um forte terremoto abalou os alicerces da prisão. As portas se abriram, e as correntes de todos os presos se soltaram. O impossível estava acontecendo diante dos olhos de todos.", 0)],
 [("Quando o carcereiro viu as portas abertas, pensou que todos haviam fugido. Desesperado, tentou tirar a própria vida. Mas Paulo gritou:", 0),
  ("Não faça nenhum mal a si mesmo! Estamos todos aqui!", 0.75)],
 [("Então, tremendo, ele perguntou: Senhores, o que devo fazer para ser salvo?", 0),
  ("Eles responderam: Creia no Senhor Jesus, e será salvo, você e os de sua casa.", 0.6)],
 [("Naquela mesma noite, o carcereiro cuidou dos ferimentos deles. Em seguida, ele e todos os seus foram batizados. Sua casa se encheu de alegria, porque agora todos criam em Deus.", 0),
  ("Quando todos os caminhos parecem fechados, Deus ainda pode transformar uma prisão em testemunho de fé.", 1.0)],
 [("Se você gostou desse conteúdo, se inscreva no canal, deixe o like e comente aqui qual outra história você gostaria que eu contasse.", 0)],
]
SR = 24000
async def tts(txt, path):
    for tentativa in range(4):
        c = edge_tts.Communicate(txt, VOZ, rate=RATE, proxy=os.environ["HTTPS_PROXY"], boundary="WordBoundary")
        words = []; audio = bytearray()
        async for ch in c.stream():
            if ch["type"] == "audio": audio += ch["data"]
            elif ch["type"] == "WordBoundary": words.append((ch["text"], ch["offset"] / 1e7, (ch["offset"] + ch["duration"]) / 1e7))
        open(path, "wb").write(audio)
        dur = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path]))
        if len(words) == len(txt.split()) and dur >= words[-1][2]: return words
        print("fala cortada, refazendo:", txt[:40])
    raise RuntimeError("edge-tts falhou 4 vezes")
def load(p):
    raw = subprocess.check_output(["ffmpeg", "-v", "error", "-i", p, "-f", "f32le", "-ac", "1", "-ar", str(SR), "-"])
    return np.frombuffer(raw, np.float32)
ONLY = [int(x) for x in sys.argv[2:]]
async def main():
    out = json.load(open("voz/words.json")) if ONLY else {}
    for k, partes in enumerate(CENAS, 1):
        if ONLY and k not in ONLY: continue
        buf = np.zeros(0, np.float32); ws = []
        for j, (txt, pausa) in enumerate(partes):
            w = await tts(txt, f"voz/p{k}_{j}.mp3"); a = load(f"voz/p{k}_{j}.mp3")
            if j > 0:   # corta a sobra de silêncio do fim da parte anterior e põe a pausa pedida
                end = int((ws[-1][2] + 0.05) * SR); buf = buf[:end]; buf = np.concatenate([buf, np.zeros(int(pausa * SR), np.float32)])
            off = len(buf) / SR - (w[0][1] - 0.02 if j > 0 else 0)
            if j > 0: a = a[int((w[0][1] - 0.02) * SR):]
            ws += [(x, off + s, off + e) for x, s, e in w]
            buf = np.concatenate([buf, a])
        sf.write(f"voz/f{k}.wav", buf, SR); out[str(k)] = ws
    json.dump(out, open("voz/words.json", "w"), ensure_ascii=False, indent=0)
    tot = 0
    for k in sorted(out): d = out[k][-1][2] - out[k][0][1]; tot += d; print(k, "fala %.2f s" % d)
    print("total de fala %.1f s" % tot)
asyncio.run(main())
