"""Linha do tempo do documentário de Elias: cenas, falas e tempos absolutos de cada palavra."""
import json, os
D = os.path.dirname(os.path.abspath(__file__))
_W = json.load(open(f"{D}/voz/words.json"))

CENAS = [  # imagem, título, referência, pré (s antes da fala), pós (s depois da fala)
    dict(img=1, titulo="ELIAS: UM PROFETA DE CORAGEM", ref="1 REIS 17:1", pre=0.25, pos=0.6),
    dict(img=2, titulo="DEUS CUIDA DOS SEUS", ref="1 REIS 17:2–7", pre=0.45, pos=0.6 + 0.104166),  # fala 2 refeita ("sêca"): 0,104 s mais curta; mantém o fim da cena
    dict(img=3, titulo="O FOGO DO SENHOR CAIU!", ref="1 REIS 18:20–39", pre=0.45, pos=1.1),
    dict(img=4, titulo="DEUS TAMBÉM CUIDA DE QUEM ESTÁ CANSADO", ref="1 REIS 19:1–8", pre=0.45, pos=0.7),
    dict(img=5, titulo="UMA MISSÃO QUE CONTINUA", ref="1 REIS 19:19–21", pre=0.45, pos=0.6),
    dict(img=6, titulo="UMA HISTÓRIA EXTRAORDINÁRIA DE FÉ", ref="2 REIS 2:1–12", pre=0.45, pos=1.0),
    dict(img=6, titulo=None, ref=None, pre=0.45, pos=1.6),
]
VOFF = 0.10  # o mp3 do edge-tts começa a falar 0,10 s depois do início do arquivo

# Versão Thalita: cada cena termina no MESMO instante da versão Antonio (reaproveita as câmeras lentas)
FIM_ALVO = [9.79, 20.33, 36.48, 48.53, 59.09, 73.43, 86.67]
_ini = 0.0
for _i, _c in enumerate(CENAS, 1):
    _end = _ini + _c["pre"] - 0.10 + _W[str(_i)][-1][2]
    _c["pos"] = round(FIM_ALVO[_i - 1] - _end, 4)
    _ini = FIM_ALVO[_i - 1]
t = 0.0
for i, c in enumerate(CENAS, 1):
    w = _W[str(i)]
    c["ini"] = t
    c["voz_em"] = t + c["pre"] - VOFF                 # onde o mp3 da fala é colocado
    c["fala_ini"] = t + c["pre"]
    c["fala_fim"] = c["voz_em"] + w[-1][2]
    c["fim"] = c["fala_fim"] + c["pos"]
    c["words"] = [(x, c["voz_em"] + a, c["voz_em"] + b) for x, a, b in w]
    t = c["fim"]
DUR = t

def quando(cena, palavra, n=1):
    """Tempo absoluto da n-ésima ocorrência de uma palavra na fala da cena (1..7)."""
    k = 0
    for x, a, b in CENAS[cena - 1]["words"]:
        if x.strip(".,!?:").lower() == palavra.lower():
            k += 1
            if k == n: return a
    raise KeyError(palavra)

T_FOGO = quando(3, "fogo")          # impacto 1: o fogo cai
T_REDEMOINHO = quando(6, "redemoinho")  # impacto 2: a subida
T_INSCREVER = quando(7, "inscrever")

if __name__ == "__main__":
    for i, c in enumerate(CENAS, 1):
        print(i, "ini %.2f fala %.2f–%.2f fim %.2f" % (c["ini"], c["fala_ini"], c["fala_fim"], c["fim"]))
    print("DUR %.2f fogo %.2f redemoinho %.2f inscrever %.2f" % (DUR, T_FOGO, T_REDEMOINHO, T_INSCREVER))
