"""Linha do tempo: Paulo e Silas na prisão (6 cenas, Atos 16)."""
import json, os
D = os.path.dirname(os.path.abspath(__file__))
_W = json.load(open(f"{D}/voz/words.json"))
CENAS = [
    dict(ref="ATOS 16:19–24", pre=0.6, pos=0.7),
    dict(ref="ATOS 16:25", pre=0.45, pos=0.8),
    dict(ref="ATOS 16:26", pre=0.45, pos=0.9),
    dict(ref="ATOS 16:27–29", pre=0.45, pos=0.7),
    dict(ref="ATOS 16:30–32", pre=0.45, pos=0.8),
    dict(ref="ATOS 16:33–34", pre=0.45, pos=3.2),   # fim: cartão ATOS 16:25–34
]
t = 0.0
for i, c in enumerate(CENAS, 1):
    w = _W[str(i)]
    c["ini"] = t; c["voz_em"] = t + c["pre"] - w[0][1]
    c["fala_ini"] = t + c["pre"]; c["fala_fim"] = c["voz_em"] + w[-1][2]
    c["fim"] = c["fala_fim"] + c["pos"]
    c["words"] = [(x, c["voz_em"] + a, c["voz_em"] + b) for x, a, b in w]
    t = c["fim"]
DUR = t
def quando(cena, palavra, n=1):
    k = 0
    for x, a, b in CENAS[cena - 1]["words"]:
        if x.strip(".,!?:").lower() == palavra.lower():
            k += 1
            if k == n: return a
    raise KeyError(palavra)
T_TERREMOTO = quando(3, "terremoto")
T_GRITOU = quando(4, "Não")
T_CREIA = quando(5, "Creia")
T_FINAL = quando(6, "Quando")
if __name__ == "__main__":
    for i, c in enumerate(CENAS, 1): print(i, "ini %.2f fim %.2f (%.1f s)" % (c["ini"], c["fim"], c["fim"] - c["ini"]))
    print("DUR %.2f terremoto %.2f gritou %.2f creia %.2f final %.2f" % (DUR, T_TERREMOTO, T_GRITOU, T_CREIA, T_FINAL))
