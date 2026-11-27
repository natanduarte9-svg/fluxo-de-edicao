"""Título animado de abertura (estilo pedido pelo usuário em 27/11/2026, referência "Back to HOME" do CapCut):
1) palavra em letra cursiva branca escrita letra por letra;
2) palavra GRANDE e grossa em amarelo surgindo letra por letra (cada letra "pula"), com as letras se juntando;
3) linha pequena de letras espaçadas que se aproximam;
4) clarões de luz quente (filme queimado) nas entradas e na saída.
Uso no código:
    T = Titulo(OW, OH, cursiva="No deserto,", forte="ELE VENCEU", linha="FIRE & GRACE", t0=1.0, t_saida=10.6, cy=0.70)
    rgba = T.camada(t)      # None fora do intervalo; senão imagem RGBA (numpy HxWx4, uint8) para sobrepor
    luz  = T.clarao(t)      # None ou imagem BGR (uint8) para SOMAR (cv2.add)
Determinístico (sem aleatório)."""
import os, math, numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont, ImageFilter

F = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fontes")

def ease_out(x): x = min(1, max(0, x)); return 1 - (1 - x) ** 3
def ease_back(x):
    x = min(1, max(0, x)); c1, c3 = 1.70158, 2.70158
    return 1 + c3 * (x - 1) ** 3 + c1 * (x - 1) ** 2

class Titulo:
    def __init__(self, W, H, cursiva, forte, linha, t0=1.0, t_saida=10.6, cy=0.70,
                 amarelo=(250, 200, 30), tam=1.0, fixar=None):
        """fixar=dict(t=..., dur=1.2, escala=0.55, y=0.09, x=0.5): em vez de sair, o título SOBE e fica
        fixo no alto até o fim (a linha pequena some na subida). x, y = centro do bloco (frações da largura/altura)."""
        self.fx = fixar; self._fixo = None
        self.W, self.H, self.c, self.f, self.l = W, H, cursiva, forte, linha
        self.t0, self.ts, self.cy, self.am = t0, t_saida, cy, amarelo
        s = tam * H / 1080
        self.fc = ImageFont.truetype(f"{F}/KaushanScript-Regular.ttf", int(92 * s))
        self.ff = ImageFont.truetype(f"{F}/MontserratBlack.ttf", int(132 * s))
        self.fl = ImageFont.truetype(f"{F}/MontserratSemi.ttf", int(36 * s))
        self.s = s
        # tempos
        self.tc = t0                                   # cursiva começa
        self.dc = 0.11                                 # s por letra
        self.tf = t0 + len(cursiva) * self.dc + 0.35   # palavra forte começa
        self.df = 0.085
        self.tl = self.tf + len(forte) * self.df + 0.45
        self.tfim = t_saida + 1.0
        # clarões: entrada da cursiva, entrada da palavra forte, saída
        self.claroes = [(self.tc + 0.35, 0.9, 0.0), (self.tf + 0.25, 1.0, 1.7)]
        if fixar:
            self.ts = 1e9; self.tfim = 1e9
            self.claroes.append((fixar["t"] + fixar.get("dur", 1.2) * 0.7, 0.9, 3.1))   # luz quando ele "gruda" no alto
        else:
            self.claroes.append((t_saida + 0.1, 1.1, 3.1))
        self._leak = self._textura_luz()

    # ---------- textura de luz (manchas quentes, borradas) ----------
    def _textura_luz(self):
        w, h = 480, 270
        yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
        img = np.zeros((h, w, 3), np.float32)
        for cx, cy, r, col in [(0.15, 0.3, 0.45, (40, 120, 255)), (0.55, 0.15, 0.35, (60, 190, 255)),
                               (0.85, 0.6, 0.5, (30, 70, 240)), (0.35, 0.85, 0.4, (90, 210, 255))]:
            d = ((xx / w - cx) ** 2 + ((yy / h - cy) * 0.6) ** 2) / r ** 2
            img += np.exp(-d * 2.2)[..., None] * np.array(col, np.float32)
        return np.clip(img, 0, 255)

    def clarao(self, t):
        tot = None
        for tc, d, ph in self.claroes:
            u = (t - tc) / d
            if 0 <= u <= 1:
                k = math.sin(math.pi * u) ** 1.5 * 0.42
                dx = int((u - 0.5) * 220 + 40 * math.sin(ph))
                L = np.roll(self._leak, dx, axis=1)
                L = cv2.resize(L, (self.W, self.H), interpolation=cv2.INTER_LINEAR) * k
                tot = L if tot is None else tot + L
        return None if tot is None else np.clip(tot, 0, 255).astype(np.uint8)

    # ---------- texto ----------
    def camada(self, t):
        if t < self.tc or t > self.tfim: return None
        if self.fx and t >= self.fx["t"]:
            dur = self.fx.get("dur", 1.2); u = ease_out((t - self.fx["t"]) / dur) if t < self.fx["t"] + dur else 1.0
            if u >= 1 and self._fixo is not None: return self._fixo
            base = self._desenhar(self.fx["t"], linha_mult=1 - min(1, u * 1.8))
            ys, xs = np.nonzero(base[..., 3] > 3)
            if len(xs) == 0: return base
            y0, y1, x0, x1 = ys.min(), ys.max() + 1, xs.min(), xs.max() + 1
            if not hasattr(self, "_c0"): self._c0 = ((y0 + y1) / 2, (x0 + x1) / 2)   # centro do bloco completo
            cy0, cx0 = self._c0
            sc = 1 + (self.fx.get("escala", 0.55) - 1) * u
            cyt = cy0 + (self.fx.get("y", 0.09) * self.H - cy0) * u
            cxt = cx0 + (self.fx.get("x", 0.5) * self.W - cx0) * u
            crop = base[y0:y1, x0:x1]
            nw, nh = max(1, int(round((x1 - x0) * sc))), max(1, int(round((y1 - y0) * sc)))
            crop = cv2.resize(crop, (nw, nh), interpolation=cv2.INTER_AREA)
            px = int(round(cxt + (x0 - cx0) * sc)); py = int(round(cyt + (y0 - cy0) * sc))
            out = np.zeros_like(base)
            ya, xa = max(0, py), max(0, px); yb, xb = min(self.H, py + nh), min(self.W, px + nw)
            out[ya:yb, xa:xb] = crop[ya - py:yb - py, xa - px:xb - px]
            if u >= 1: self._fixo = out
            return out
        return self._desenhar(t)

    def _desenhar(self, t, linha_mult=1.0):
        S = 2                                           # supersampling
        W, H = self.W * S, self.H * S
        im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
        sh = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ds = ImageDraw.Draw(sh)   # sombra
        sa = 1.0                                        # saída
        if t > self.ts: sa = 1 - ease_out((t - self.ts) / 0.9)
        dy_out = -30 * self.s * S * (1 - sa)
        fc = self.fc.font_variant(size=self.fc.size * S); ff = self.ff.font_variant(size=self.ff.size * S)
        fl = self.fl.font_variant(size=self.fl.size * S)
        cy = self.cy * H + dy_out
        # 1) cursiva, letra por letra
        y_c = cy - 125 * self.s * S
        tot = fc.getlength(self.c); x0 = W / 2 - tot / 2 - 60 * self.s * S
        n = (t - self.tc) / self.dc
        for i, ch in enumerate(self.c):
            a = min(1, max(0, n - i) / 0.6)
            if a <= 0: break
            x = x0 + fc.getlength(self.c[:i])
            A = int(255 * a * sa)
            ds.text((x + 4 * S, y_c + 5 * S), ch, font=fc, fill=(0, 0, 0, int(A * 0.55)))
            d.text((x, y_c), ch, font=fc, fill=(255, 255, 255, A))
        # 2) palavra forte: cada letra pula; espaçamento diminui
        if t >= self.tf:
            u = (t - self.tf) / (len(self.f) * self.df + 0.6)
            track = (70 - 64 * ease_out(u)) * self.s * S
            ws = [ff.getlength(ch) for ch in self.f]
            tw = sum(ws) + track * (len(self.f) - 1)
            x = W / 2 - tw / 2; y_f = cy - 40 * self.s * S
            for i, ch in enumerate(self.f):
                p = (t - self.tf - i * self.df) / 0.22
                if p > 0 and ch != " ":
                    sc = 0.4 + 0.6 * ease_back(p)
                    A = int(255 * min(1, p * 1.6) * sa)
                    L = Image.new("RGBA", (int(ws[i] + 40 * S), int(ff.size * 1.5)), (0, 0, 0, 0))
                    ImageDraw.Draw(L).text((20 * S, 0), ch, font=ff, fill=self.am + (255,))
                    if abs(sc - 1) > 0.01:
                        L = L.resize((max(1, int(L.width * sc)), max(1, int(L.height * sc))), Image.BICUBIC)
                    if A < 255: L.putalpha(L.getchannel("A").point(lambda v: v * A // 255))
                    px = int(x + ws[i] / 2 - L.width / 2 + 0 * S); py = int(y_f + ff.size * 0.75 * (1 - sc) * 0.5)
                    sdw = Image.new("RGBA", L.size, (0, 0, 0, 0)); sdw.putalpha(L.getchannel("A").point(lambda v: int(v * 0.5)))
                    sh.alpha_composite(sdw, (px + 5 * S, py + 7 * S)); im.alpha_composite(L, (px, py))
                x += ws[i] + track
        # 3) linha pequena com letras espaçadas
        if t >= self.tl:
            u = ease_out((t - self.tl) / 1.1)
            track = (26 - 12 * u) * self.s * S
            ws = [fl.getlength(ch) for ch in self.l]
            tw = sum(ws) + track * (len(self.l) - 1)
            x = W / 2 - tw / 2; y_l = cy + 125 * self.s * S
            A = int(255 * u * sa * linha_mult)
            for i, ch in enumerate(self.l):
                ds.text((x + 2 * S, y_l + 3 * S), ch, font=fl, fill=(0, 0, 0, int(A * 0.6)))
                d.text((x, y_l), ch, font=fl, fill=(255, 255, 255, A)); x += ws[i] + track
        sh = sh.filter(ImageFilter.GaussianBlur(6 * S))
        sh.alpha_composite(im)
        out = sh.resize((self.W, self.H), Image.LANCZOS)
        return np.asarray(out)

def sobrepor(fr_bgr, rgba):
    """sobrepõe a camada RGBA (do PIL, em RGB) num quadro BGR do OpenCV"""
    a = rgba[..., 3:4].astype(np.float32) / 255
    if a.max() == 0: return fr_bgr
    ys, xs = np.nonzero(rgba[..., 3]); y0, y1, x0, x1 = ys.min(), ys.max() + 1, xs.min(), xs.max() + 1
    sub = fr_bgr[y0:y1, x0:x1].astype(np.float32); c = rgba[y0:y1, x0:x1, 2::-1].astype(np.float32); aa = a[y0:y1, x0:x1]
    fr_bgr[y0:y1, x0:x1] = (sub * (1 - aa) + c * aa).astype(np.uint8)
    return fr_bgr
