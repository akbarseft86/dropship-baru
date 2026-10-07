"""Build a Meora landing page in the Movensa (marketplace-style) layout."""
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from build_meora_pages import CHECKOUT_CSS, FORM, SCRIPT, EXACT_SCRIPT_PATCHES  # noqa: E402
from build_movensa_page import PAGE as MOVENSA  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
FOLDER = "meora-movensa"

STYLE = MOVENSA[MOVENSA.index("<style>"):MOVENSA.index("</style>") + len("</style>")]
STYLE = STYLE.replace("--red: #5b2d8e;", "--red: #a3382a;").replace("--red-dark: #3f1d66;", "--red-dark: #7d2a1f;")
STYLE = STYLE.replace("  footer b { display: block; color: #444; }", """  footer b { display: block; color: #444; }
  .store .logo { flex: 0 0 48px; height: 48px; border-radius: 50%; background: var(--red); color: #fff; display: flex; align-items: center; justify-content: center; font: 700 22px Georgia, serif; }
  .review .pic { width: 26px; height: 26px; margin: 0; border-radius: 50%; }""")
GALLERY_JS = MOVENSA[MOVENSA.rindex("<script>"):MOVENSA.rindex("</script>") + len("</script>")]

GALLERY = [
    ("../meora-fa1/img/01-hero.jpg", "Meora – bekas luka menonjol seperti keloid"),
    ("../meora-fa1/img/02-10x.jpg", "10x lebih efektif ratakan keloid dan bekas luka"),
    ("../meora-fa1/img/03-tumpas.jpg", "Tumpas bekas luka sampai ke akarnya, 3 kandungan alami"),
    ("../meora-fa1/img/04-offer.jpg", "Kekuatan alami Papua, diskon 50%, COD available"),
    ("../meora-2/img/06-promo.jpg", "Promo hari ini diskon 50%, Rp99 ribu"),
]

LONG = [
    ("../meora/img/02-masalah.jpg", "Apakah Anda mengalami ini?"),
    ("../meora/img/03-kandungan.jpg", "Kandungan alami dan manfaatnya"),
    ("../meora-2/img/03-10x.jpg", "10x lebih efektif ratakan keloid dan bekas luka"),
    ("../meora/img/04-bpom.jpg", "Produk Meora sudah terdaftar di BPOM"),
    ("../meora/img/07-pengiriman.jpg", "Testimoni pengiriman barang"),
]

slides = "\n".join(
    f'      <img src="{f}" alt="{alt}"{"" if i == 0 else " loading=" + chr(34) + "lazy" + chr(34)}>'
    for i, (f, alt) in enumerate(GALLERY))
thumbs = "\n".join(
    f'      <button type="button" data-i="{i}"{" class=" + chr(34) + "on" + chr(34) if i == 0 else ""}><img src="{f}" alt="" loading="lazy"></button>'
    for i, (f, _) in enumerate(GALLERY))
long_imgs = "\n".join(f'    <img class="full" src="{f}" alt="{alt}" loading="lazy">' for f, alt in LONG)

PAGE = """<!doctype html>
<html lang="id">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Meora Natural Glow Balm</title>
<meta name="description" content="Meora balm dengan ekstrak Buah Merah Papua.">
<meta name="theme-color" content="#a3382a">
__STYLE__
</head>
<body>
<div class="wrap">
  <div class="search"><a href="#" aria-label="Kembali">‹</a><div class="box">🔍 Cari di MEORA Natural Glow Balm...</div><a href="#order" aria-label="Keranjang">🛒</a></div>

  <div class="gallery">
    <div class="slides" id="slides">
__SLIDES__
    </div>
    <div class="count" id="count">1/__N__</div>
  </div>
  <div class="thumbs" id="thumbs">
__THUMBS__
  </div>

  <div class="pricebar">
    <div class="promo">PROMO SPESIAL HARI INI</div>
    <div class="mid">
      <div><s>🔥 Harga Normal Rp200.000</s></div>
      <div>🔥 Harga Promo</div>
      <div><span class="now">Rp99.000</span> <span class="save">🎁 Diskon 50%</span></div>
    </div>
    <div class="stock">📦 STOK PROMO TERBATAS<b>Sisa 12 Jar Lagi</b></div>
  </div>

  <div class="info">
    <div class="badges"><span class="badge off">RESELLER RESMI</span><span class="badge cod">🚚 Bisa Bayar di Tempat (COD)</span></div>
    <h1>[ORIGINAL] Meora Body Brightening &amp; Natural Glow Balm – Ekstrak Buah Merah Papua untuk Kulit Lembap, Cerah &amp; Bekas Luka | BPOM</h1>
    <div class="meta"><b>4.9 ★</b><i>|</i>Rating Kepuasan<i>|</i>10rb+ Wanita Terbantu</div>
  </div>

  <div class="voucher">PROMO: <span class="v">Diskon 50%</span><span class="v green">Bisa COD</span><a href="#order">AMBIL PROMO</a></div>

  <div class="assure">
    <div>💵<p style="margin:0"><b>Bisa Bayar di Tempat (COD)</b><span>Sangat aman. Cukup bayar tunai ke kurir saat produk sampai di tangan Anda.</span></p></div>
    <div>📦<p style="margin:0"><b>Dikirim ke Seluruh Indonesia</b><span>Paket dikirim langsung ke alamat rumah Anda.</span></p></div>
  </div>

  <div class="store" id="toko">
    <div class="row">
      <div class="logo">M</div>
      <div class="name"><b>MEORA – Reseller Resmi</b><em>Online</em><small>Balm Buah Merah Papua · Terdaftar BPOM</small></div>
      <a class="visit" href="#order">PESAN SEKARANG</a>
    </div>
    <div class="stats">
      <div><b>100%</b><span>Bahan Natural</span></div>
      <div><b>4.9</b><span>Rating Kepuasan</span></div>
      <div><b>BPOM</b><span>Terdaftar Resmi</span></div>
    </div>
  </div>

  <div class="desc">
    <h2>MEORA NATURAL GLOW BALM</h2>
    <p class="sub">Kekuatan alami Papua untuk kulit sehat, lembap, dan bercahaya!</p>
    <p>Rahasia kecantikan eksotis dengan ekstrak Buah Merah murni. Diperkaya minyak kelapa dara dan ekstrak tumbuhan herbal untuk merawat kulit kering, kusam, noda hitam, hingga area bekas luka.</p>
  </div>

  <div class="block">
    <h3>KEUNGGULAN MEORA NATURAL GLOW BALM</h3>
    <div class="check"><div class="ok">✓</div><div><b>Hidrasi Mendalam</b><span>Melembapkan kulit secara intensif dan tahan lama. Selamat tinggal kulit kering.</span></div></div>
    <div class="check"><div class="ok">✓</div><div><b>Mencerahkan &amp; Meratakan</b><span>Membantu mengurangi noda hitam dan mencerahkan kulit kusam secara bertahap.</span></div></div>
    <div class="check"><div class="ok">✓</div><div><b>Perlindungan Antioksidan</b><span>Melindungi sel kulit dari kerusakan akibat radikal bebas dan polusi lingkungan.</span></div></div>
    <div class="check"><div class="ok">✓</div><div><b>Menutrisi &amp; Meregenerasi</b><span>Memelihara kesehatan kulit secara menyeluruh dan membantu proses peremajaan sel.</span></div></div>
  </div>

  <div class="formula">
    <h3>FORMULA PILIHAN &amp; MANFAAT NYATA</h3>
    <p>Diperkaya dengan Buah Merah asli Papua</p>
  </div>
  <div style="padding:14px 0 0">
__LONG__
  </div>

  <div class="block">
    <h3>KOMPOSISI UTAMA (INGREDIENTS):</h3>
    <div class="ing"><b>Ekstrak Buah Merah</b><span>Antioksidan &amp; Vitamin E. Kaya akan tokoferol dan betakaroten yang membantu menangkal radikal bebas dan mendukung regenerasi sel kulit.</span></div>
    <div class="ing"><b>Minyak Kelapa Dara</b><span>Pelembap alami intensif. Mengunci kelembapan kulit, merawat <i>skin barrier</i>, dan membuat tekstur kulit halus dan kenyal.</span></div>
    <div class="ing"><b>Ekstrak Tumbuhan Herbal</b><span>Menenangkan &amp; menyegarkan. Membantu menenangkan kulit kemerahan dan memberikan sensasi segar sepanjang hari.</span></div>
  </div>

  <div class="block">
    <p class="eyebrow">MANFAAT PRODUK</p>
    <p class="big">Kembalikan Pesona Alami Kulitmu</p>
    <p class="lead">Rawat kulit dan area bekas luka dengan bahan alami</p>
    <div class="benefit">Membantu merawat kulit pada area bekas luka menonjol.</div>
    <div class="benefit">Membantu menjaga kelembapan area keloid.</div>
    <div class="benefit">Membantu membuat kulit terasa lebih halus &amp; lembut.</div>
    <div class="benefit">Membantu merawat tekstur kulit yang tidak rata.</div>
    <div class="benefit">Membantu menjaga elastisitas kulit di area bekas luka.</div>
  </div>

  <div class="block">
    <p class="eyebrow">PANDUAN &amp; DETAIL</p>
    <p class="big" style="font-size:16px;color:var(--red)">Cara Penggunaan</p>
    <ol class="steps">
      <li>Bersihkan dan keringkan area kulit yang akan dirawat.</li>
      <li>Oleskan balm tipis-tipis secara merata.</li>
      <li>Gunakan rutin setiap hari, pagi dan malam.</li>
    </ol>
    <p class="big" style="font-size:16px;color:var(--red);margin-top:14px">Detail Produk</p>
    <div class="detail"><div><span>Netto</span><b>30 gram</b></div><div><span>Kemasan</span><b>Jar (Balm)</b></div></div>
    <p class="warn">Untuk kulit sensitif, oleskan sedikit di lengan bagian dalam dan tunggu 24 jam sebelum dipakai di area yang lebih luas.</p>
  </div>

  <div class="block">
    <div class="reviews-head"><h3 style="margin:0">ULASAN PENGGUNA PILIHAN</h3><a href="#order">Lihat Semua</a></div>
    <div class="review"><div class="who"><img class="pic" src="../meora-fa1/img/av-arini.jpg" alt="">Arini Putri<span class="when">Karyawan, 32 Tahun</span></div><div class="stars">★★★★★</div><p>"Awalnya udah pasrah banget sama kulit wajah yang kusam dan banyak flek hitam. Pas coba telaten pakai krim Meora ini tiap malam, tekstur kulit perlahan jadi kenyal dan cerah. Flek juga makin pudar merata sama warna kulit asli. Hasilnya bener-bener nyata!"</p><img src="../meora-fa1/img/wa-ayu.jpg" alt="Testimoni WhatsApp" loading="lazy"></div>
    <div class="review"><div class="who"><img class="pic" src="../meora-fa1/img/av-diana.jpg" alt="">Diana S.<span class="when">Ibu Rumah Tangga, 28 Tahun</span></div><div class="stars">★★★★★</div><p>"Sumpah bagus banget produk ini! Kulitku yang tadinya super kering sampai bersisik, sekarang udah jauh lebih lembap dan glowing setelah rutin pakai. Teksturnya nyaman banget di kulit, nggak lengket, dan cepet meresap."</p><img src="../meora-fa1/img/wa-diana.jpg" alt="Testimoni WhatsApp" loading="lazy"></div>
    <div class="review"><div class="who"><img class="pic" src="../meora-fa1/img/av-nita.jpg" alt="">Nita Maharani<span class="when">Wiraswasta, 35 Tahun</span></div><div class="stars">★★★★★</div><p>"Puas banget! Krim perawatan wajah paling mantul. Kandungan alaminya ramah banget di kulit, nggak bikin iritasi sama sekali. Pemakaian rutin sebulan udah kelihatan lebih awet muda!"</p></div>
  </div>

  <section id="order" class="block">
    <h2>Isi Form Pemesanan</h2>
    <p>Isi data di bawah ini, paket dikirim ke alamat Anda.</p>
__FORM__
  </section>

  <footer><b>MEORA – Reseller Resmi</b>© 2026 Meora. Hak Cipta Dilindungi Undang-Undang.</footer>
</div>

<div class="sticky" id="sticky"><a class="ico" href="#order"><span>💬</span>Tanya CS</a><a class="ico" href="#toko"><span>🏪</span>Toko</a><a class="btn" href="#order">BELI SEKARANG (COD)</a></div>

__SCRIPT__
__GALLERY_JS__
</body>
</html>
"""


def build():
    html = (PAGE.replace("__STYLE__", STYLE).replace("__SLIDES__", slides).replace("__THUMBS__", thumbs)
            .replace("__N__", str(len(GALLERY))).replace("__LONG__", long_imgs)
            .replace("__FORM__", FORM).replace("__SCRIPT__", SCRIPT).replace("__GALLERY_JS__", GALLERY_JS))
    html = html.replace("__CHECKOUT_CSS__", CHECKOUT_CSS.rstrip("\n"))
    for old, new in EXACT_SCRIPT_PATCHES:
        assert html.count(old) == 1, old
        html = html.replace(old, new)
    html = html.replace('id="submitBtn">Beli Sekarang<', 'id="submitBtn">BELI SEKARANG<')
    html = html.replace('btn.textContent = "Beli Sekarang";', 'btn.textContent = "BELI SEKARANG";')
    assert "movensa" not in html.lower(), "Movensa text left"
    assert "__" not in re.sub(r"<script>.*?</script>", "", html, flags=re.S)
    return html


def with_cdn(html, sha):
    return re.sub(r'src="\.\./([\w-]+)/img/',
                  lambda m: f'src="https://cdn.jsdelivr.net/gh/akbarseft86/dropship-baru@{sha}/{m.group(1)}/img/', html)


if __name__ == "__main__":
    sha = sys.argv[1] if len(sys.argv) > 1 else None
    html = build()
    (ROOT / FOLDER).mkdir(exist_ok=True)
    (ROOT / FOLDER / "index.html").write_text(html)
    if sha:
        (ROOT / FOLDER / "index.scalev.html").write_text(with_cdn(html, sha))
