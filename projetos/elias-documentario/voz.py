import asyncio, os, json, sys, edge_tts
FALAS = [
 "Você conhece a história de Elias? Ele foi um profeta de Deus que enfrentou o rei Acabe e anunciou que não choveria sobre Israel, conforme a palavra do Senhor.",
 "Durante a seca, Deus ordenou que Elias fosse ao ribeiro de Querite. Ali, corvos levavam pão e carne pela manhã e à tarde, enquanto ele bebia da água do ribeiro.",
 "Mais tarde, no monte Carmelo, Elias desafiou os profetas de Baal. Enquanto eles não obtiveram resposta, Elias orou, e o fogo do Senhor caiu do céu, consumindo o sacrifício. O povo reconheceu que somente o Senhor é Deus!",
 "Mas Elias também enfrentou momentos difíceis. Com medo e esgotado, foi para o deserto. Ali, Deus enviou um anjo para alimentá-lo e fortalecê-lo para continuar sua jornada.",
 "No caminho, Elias encontrou Eliseu trabalhando no campo e o chamou para segui-lo. Assim começou uma nova etapa: Eliseu seria preparado para continuar o trabalho profético.",
 "Elias não morreu como os outros homens. Em um acontecimento extraordinário, foi levado ao céu em um redemoinho, enquanto uma carruagem de fogo separou Elias de Eliseu. Sua história ficou marcada pela fé e coragem!",
 "Se você gostou desse conteúdo, comente aqui embaixo sobre qual outra história você gostaria que eu fizesse. Não se esqueça de deixar o like e se inscrever no canal para acompanhar mais histórias bíblicas!",
]
RATE = sys.argv[1] if len(sys.argv) > 1 else "+0%"
async def one(i, txt):
    c = edge_tts.Communicate(txt, "pt-BR-AntonioNeural", rate=RATE, proxy=os.environ["HTTPS_PROXY"], boundary="WordBoundary")
    words = []; audio = bytearray()
    async for ch in c.stream():
        if ch["type"] == "audio": audio += ch["data"]
        elif ch["type"] == "WordBoundary":
            words.append((ch["text"], ch["offset"] / 1e7, (ch["offset"] + ch["duration"]) / 1e7))
    open(f"voz/f{i}.mp3", "wb").write(audio)
    return words
async def main():
    out = {}
    for i, t in enumerate(FALAS, 1): out[i] = await one(i, t)
    json.dump(out, open("voz/words.json", "w"), ensure_ascii=False, indent=0)
asyncio.run(main())
