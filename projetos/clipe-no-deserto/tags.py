"""Monta tags (limite do YouTube: 500 caracteres; tag com espaço conta +2 pelas aspas) e 15 hashtags."""
def caber(lista, lim=500):
    out, tot = [], 0
    for t in lista:
        c = len(t) + (2 if " " in t else 0) + (1 if out else 0)
        if tot + c <= lim and t not in out: out.append(t); tot += c
    return out, tot
BASE = ["no deserto ele venceu", "ele venceu no deserto", "fire and grace", "louvor gospel", "música gospel",
        "louvor com letra", "música gospel com letra", "jesus no deserto", "tentação de jesus", "jesus venceu",
        "louvor 2026", "gospel 2026", "música cristã", "louvor de vitória", "louvor para fortalecer a fé",
        "hino de vitória", "adoração", "louvor e adoração", "mateus 4", "lucas 4", "quarenta dias no deserto",
        "nem só de pão vive o homem", "jesus cristo", "fé em deus", "louvor emocionante", "música evangélica",
        "louvores", "gospel", "louvor", "worship", "clipe gospel", "videoclipe gospel", "letra gospel",
        "louvor para ouvir", "musica de deus", "hinos evangélicos", "louvor que toca", "fire & grace"]
SH = ["shorts", "gospel shorts", "louvor shorts", "status gospel", "música gospel", "louvor gospel",
      "no deserto ele venceu", "ele venceu no deserto", "fire and grace", "jesus venceu", "jesus no deserto",
      "tentação de jesus", "louvor com letra", "louvor de vitória", "louvor 2026", "gospel 2026", "música cristã",
      "louvor emocionante", "adoração", "fé em deus", "musica de deus", "louvor para fortalecer a fé", "worship",
      "música evangélica", "louvores", "gospel", "louvor", "hino de vitória", "jesus cristo", "fire & grace"]
ESP = {1: ["e a morte não o fez parar", "com jesus eu vou ficar", "o mesmo cristo que venceu"],
       2: ["quantas vezes nós também", "provação", "caminho fácil", "venceu a fome e a tentação"],
       3: ["nem todo desejo é caminho", "nem toda porta vem de deus", "nem todo aplauso é aprovação dos céus", "pela graça"]}
HL = ["#NoDesertoEleVenceu", "#LouvorGospel", "#MúsicaGospel", "#Gospel", "#Jesus", "#Louvor", "#FireAndGrace",
      "#LouvorComLetra", "#Adoração", "#MúsicaCristã", "#Gospel2026", "#JesusVenceu", "#Fé", "#Worship", "#Deus"]
HS = ["#Shorts", "#NoDesertoEleVenceu", "#Gospel", "#LouvorGospel", "#Jesus", "#Louvor", "#FireAndGrace",
      "#MúsicaGospel", "#GospelShorts", "#Fé", "#Adoração", "#JesusVenceu", "#MúsicaCristã", "#Deus", "#Worship"]
if __name__ == "__main__":
    t, n = caber(BASE); print("LONGO", n, "caracteres,", len(t), "tags"); print(", ".join(t)); print(" ".join(HL), len(HL))
    for k in (1, 2, 3):
        t, n = caber(ESP[k] + SH); print(f"\nSHORT {k}", n, "caracteres,", len(t), "tags"); print(", ".join(t))
    print(" ".join(HS), len(HS))
