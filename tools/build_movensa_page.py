"""Build the Movensa landing page (exact replica), reusing the Meora checkout form."""
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from build_meora_pages import CHECKOUT_CSS, FORM, SCRIPT, EXACT_SCRIPT_PATCHES  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
FOLDER = "movensa-persis"

GALLERY = [
    ("g1-beli1gratis1.jpg", "Perut kembung? Begah? Tidak nyaman? Beli 1 gratis 1"),
    ("g2-keaslian.jpg", "Pernyataan keaslian merek resmi MOVENSA"),
    ("g3-formula.jpg", "Formula bahan alami"),
    ("g4-cara-pakai.jpg", "Cara pakai Movensa"),
    ("g5-area-perut.jpg", "Untuk digunakan pada area perut"),
    ("g6-redakan.jpg", "Bantu redakan perut kembung, begah dan rasa kurang nyaman"),
    ("g7-mudah-diserap.jpg", "Mudah diserap dan bekerja cepat pada area perut"),
    ("g8-tips.jpg", "Tips penggunaan Movensa"),
]

LONG = [
    ("s1-dioleskan.jpg", "Dioleskan pada area perut"),
    ("s2-masalah.jpg", "Jika Anda juga mengalami masalah berikut"),
    ("s3-tekstur.jpg", "Tekstur gel segar dan tidak lengket"),
    ("s4-keterangan.jpg", "Keterangan produk dan cara penggunaan"),
    ("s5-informasi.jpg", "Informasi produk Movensa Gel Perut"),
    ("s6-bonus-gratis.jpg", "Gratis Movensa Gel Pereda Nyeri Perut"),
]

slides = "\n".join(
    f'      <img src="img/{f}" alt="{alt}"{'' if i == 0 else ' loading="lazy"'}>'
    for i, (f, alt) in enumerate(GALLERY))
thumbs = "\n".join(
    f'      <button type="button" data-i="{i}"{' class="on"' if i == 0 else ''}><img src="img/{f}" alt="" loading="lazy"></button>'
    for i, (f, _) in enumerate(GALLERY))
long_imgs = "\n".join(f'    <img class="full" src="img/{f}" alt="{alt}" loading="lazy">' for f, alt in LONG)

PAGE = """<!doctype html>
<html lang="id">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>MOVENSA GEL PERUT</title>
<meta name="description" content="Movensa Body Comfort Cream Herbal – bantu redakan perut begah, kembung, masuk angin.">
<meta name="theme-color" content="#5b2d8e">
<style>
  :root {
    --red: #5b2d8e;
    --red-dark: #3f1d66;
    --purple-soft: #f3eefa;
    --orange: #ee4d2d;
    --green: #1f8a4c;
    --text: #222;
    --muted: #777;
    --border: #ececec;
  }
  * { box-sizing: border-box; }
  html { scroll-behavior: smooth; }
  body {
    margin: 0; background: #f0f0f0; color: var(--text);
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    font-size: 15px; line-height: 1.5;
  }
  .wrap { max-width: 480px; margin: 0 auto; background: #fff; padding-bottom: 76px; }
  .search { position: sticky; top: 0; z-index: 9; display: flex; align-items: center; gap: 10px; padding: 8px 12px; background: #fff; border-bottom: 1px solid var(--border); }
  .search .box { flex: 1; display: flex; align-items: center; gap: 6px; border: 1px solid var(--border); border-radius: 6px; padding: 6px 10px; font-size: 13px; color: #999; }
  .search a { color: #444; text-decoration: none; font-size: 20px; line-height: 1; }
  .gallery { position: relative; }
  .slides { display: flex; overflow-x: auto; scroll-snap-type: x mandatory; scrollbar-width: none; }
  .slides::-webkit-scrollbar { display: none; }
  .slides img { flex: 0 0 100%; width: 100%; aspect-ratio: 1; object-fit: cover; scroll-snap-align: center; display: block; }
  .count { position: absolute; right: 10px; bottom: 10px; background: rgba(0,0,0,.45); color: #fff; font-size: 12px; padding: 2px 8px; border-radius: 10px; }
  .thumbs { display: flex; gap: 6px; padding: 8px 10px; overflow-x: auto; scrollbar-width: none; }
  .thumbs button { flex: 0 0 52px; height: 52px; padding: 0; border: 2px solid transparent; border-radius: 4px; background: none; cursor: pointer; }
  .thumbs button.on { border-color: var(--orange); }
  .thumbs img { width: 100%; height: 100%; object-fit: cover; border-radius: 2px; display: block; }
  .pricebar { display: grid; grid-template-columns: 82px 1fr 92px; align-items: center; background: linear-gradient(90deg, #ee4d2d, #ff7337); color: #fff; }
  .pricebar .promo { font-size: 11px; font-weight: 800; line-height: 1.2; padding: 10px; }
  .pricebar .mid { background: #fff5f1; color: var(--orange); padding: 8px 10px; }
  .pricebar .mid s { color: #999; font-size: 12px; }
  .pricebar .mid .now { font-size: 22px; font-weight: 800; }
  .pricebar .mid .save { font-size: 11px; font-weight: 700; }
  .pricebar .stock { text-align: center; font-size: 11px; font-weight: 800; line-height: 1.25; padding: 8px 6px; }
  .pricebar .stock b { display: block; font-size: 12px; }
  .info { padding: 12px 14px; border-bottom: 8px solid #f5f5f5; }
  .badges { display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 6px; }
  .badge { font-size: 10px; font-weight: 800; padding: 2px 6px; border-radius: 2px; }
  .badge.off { background: var(--red); color: #fff; }
  .badge.cod { background: #fff4e5; color: #d46b08; border: 1px solid #ffd591; }
  h1 { font-size: 16px; font-weight: 600; line-height: 1.4; margin: 0 0 8px; }
  .meta { font-size: 13px; color: #555; }
  .meta b { color: var(--orange); }
  .meta i { font-style: normal; color: #ddd; margin: 0 8px; }
  .voucher { display: flex; align-items: center; gap: 6px; padding: 10px 14px; border-bottom: 8px solid #f5f5f5; font-size: 12px; }
  .voucher .v { border: 1px dashed var(--orange); color: var(--orange); padding: 2px 6px; border-radius: 3px; font-weight: 700; }
  .voucher .v.green { border-color: #00bfa5; color: #00a08a; }
  .voucher a { margin-left: auto; color: var(--orange); font-weight: 800; text-decoration: none; }
  .assure { padding: 6px 14px; border-bottom: 8px solid #f5f5f5; }
  .assure div { display: flex; gap: 10px; padding: 8px 0; font-size: 13px; }
  .assure div + div { border-top: 1px solid var(--border); }
  .assure b { display: block; font-size: 14px; }
  .assure span { color: var(--muted); }
  .store { padding: 12px 14px; border-bottom: 8px solid #f5f5f5; }
  .store .row { display: flex; align-items: center; gap: 10px; }
  .store img { width: 48px; height: 48px; border-radius: 50%; border: 1px solid var(--border); }
  .store .name { flex: 1; font-size: 14px; }
  .store .name b { display: block; }
  .store .name small { display: block; color: var(--muted); font-size: 11px; }
  .store .name em { color: #26aa99; font-style: normal; font-size: 11px; }
  .store a.visit { border: 1px solid var(--red); color: var(--red); font-size: 11px; font-weight: 700; padding: 5px 8px; border-radius: 3px; text-decoration: none; }
  .stats { display: grid; grid-template-columns: repeat(3, 1fr); text-align: center; margin-top: 12px; }
  .stats b { display: block; color: var(--red); font-size: 15px; }
  .stats span { font-size: 11px; color: var(--muted); }
  .desc { padding: 18px 16px; text-align: center; border-bottom: 1px solid var(--border); }
  .desc h2 { color: var(--red); font-size: 16px; letter-spacing: .4px; margin: 0 0 4px; }
  .desc .sub { font-weight: 700; margin: 0 0 10px; }
  .desc p { color: #555; font-size: 14px; margin: 0; }
  .block { padding: 18px 16px; border-bottom: 1px solid var(--border); }
  .block h3 { font-size: 14px; letter-spacing: .4px; margin: 0 0 14px; }
  .block h3.center, .center { text-align: center; }
  .check { display: flex; gap: 10px; margin-bottom: 14px; }
  .check .ok { flex: 0 0 22px; height: 22px; border-radius: 4px; background: #25a244; color: #fff; display: flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 700; }
  .check b { display: block; font-size: 14px; }
  .check span { font-size: 13px; color: #666; }
  .formula { text-align: center; padding: 18px 16px 6px; }
  .formula h3 { color: var(--red); font-size: 15px; letter-spacing: .4px; margin: 0 0 4px; }
  .formula p { font-size: 13px; color: #666; margin: 0; }
  img.full { display: block; width: 100%; height: auto; }
  .ing { margin-bottom: 12px; }
  .ing b { display: block; font-size: 14px; }
  .ing b::before { content: "✔ "; color: var(--red); }
  .ing span { display: block; font-size: 13px; color: #666; padding-left: 18px; }
  .eyebrow { font-size: 11px; letter-spacing: 1.5px; color: #999; text-transform: uppercase; text-align: center; margin: 0 0 6px; }
  .big { text-align: center; font-size: 18px; font-weight: 700; margin: 0 0 4px; }
  .lead { text-align: center; color: #666; font-size: 13px; margin: 0 0 14px; }
  .benefit { border: 1px solid var(--border); border-radius: 8px; padding: 12px 14px; margin-bottom: 10px; font-size: 14px; box-shadow: 0 1px 4px rgba(0,0,0,.04); }
  .benefit::before { content: "🔹 "; }
  ol.steps { margin: 0; padding-left: 20px; color: #555; font-size: 14px; }
  ol.steps li { margin-bottom: 8px; }
  .detail { display: grid; grid-template-columns: 1fr 1fr; text-align: center; border: 1px solid var(--border); border-radius: 8px; margin-top: 10px; }
  .detail div { padding: 10px; }
  .detail div + div { border-left: 1px solid var(--border); }
  .detail span { display: block; font-size: 12px; color: var(--muted); }
  .warn { margin: 14px 0 0; font-size: 12px; color: #a33; background: #fff6f6; border: 1px solid #f3d0d0; border-radius: 6px; padding: 10px 12px; text-align: center; }
  .reviews-head { display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px; }
  .reviews-head a { color: var(--orange); font-size: 13px; text-decoration: none; }
  .review { padding: 12px 0; border-bottom: 1px solid var(--border); }
  .review .who { display: flex; align-items: center; gap: 8px; font-size: 13px; }
  .review .av { width: 26px; height: 26px; border-radius: 50%; background: #eee; color: #666; display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 700; }
  .review .when { margin-left: auto; color: #aaa; font-size: 11px; }
  .review .stars { color: #ffb400; font-size: 13px; margin: 6px 0 4px; letter-spacing: 1px; }
  .review p { margin: 0; font-size: 14px; color: #333; }
  .review img { width: 72px; height: 72px; object-fit: cover; border-radius: 4px; margin-top: 8px; display: block; }
  #order h2 { font-size: 17px; margin: 0 0 4px; }
  #order > p { color: #666; font-size: 13px; margin: 0 0 12px; }
__CHECKOUT_CSS__
  .sticky { padding: 6px 10px calc(6px + env(safe-area-inset-bottom)); background: #fff; display: flex; gap: 6px; align-items: center; max-width: 480px; margin: 0 auto; border-top: 1px solid var(--border); }
  .sticky.hide { display: none; }
  .sticky .ico { flex: 0 0 52px; text-align: center; font-size: 10px; color: #555; text-decoration: none; line-height: 1.2; }
  .sticky .ico span { display: block; font-size: 20px; }
  .sticky .btn { border-radius: 4px; box-shadow: none; background: var(--orange); font-size: 15px; padding: 13px 10px; }
  footer { text-align: center; font-size: 12px; color: var(--muted); padding: 16px; }
  footer b { display: block; color: #444; }
</style>
</head>
<body>
<div class="wrap">
  <div class="search"><a href="#" aria-label="Kembali">‹</a><div class="box">🔍 Cari di MOVENSA Body Comfort...</div><a href="#order" aria-label="Keranjang">🛒</a></div>

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
      <div><s>🔥 Harga Normal Rp198.000</s></div>
      <div>🔥 Harga Promo</div>
      <div><span class="now">Rp99.000</span> <span class="save">🎁 Hemat 50%</span></div>
    </div>
    <div class="stock">📦 STOK PROMO TERBATAS<b>Sisa 3 Botol Lagi</b></div>
  </div>

  <div class="info">
    <div class="badges"><span class="badge off">OFFICIAL STORE</span><span class="badge cod">🚚 Bisa Bayar di Tempat (COD)</span></div>
    <h1>[ORIGINAL] Movensa Body Comfort Cream Herbal – Bantu Redakan Perut Begah, Kembung, Masuk Angin &amp; Perut Tidak Nyaman | BPOM &amp; Halal</h1>
    <div class="meta"><b>4.9 ★</b><i>|</i>Ulasan Pengguna 950+<i>|</i>Terjual 3,2rb+</div>
  </div>

  <div class="voucher">VOUCHER: <span class="v">Diskon Rp5.000</span><span class="v green">Gratis Ongkir</span><a href="#order">KLAIM VOUCHER</a></div>

  <div class="assure">
    <div>💵<p style="margin:0"><b>Bisa Bayar di Tempat (COD)</b><span>Sangat aman. Cukup bayar tunai ke kurir saat produk sampai di tangan Anda.</span></p></div>
    <div>🛡️<p style="margin:0"><b>Gratis Ongkir Seluruh Indonesia</b><span>Nikmati pengiriman Rp0 langsung ke alamat rumah Anda.</span></p></div>
  </div>

  <div class="store" id="toko">
    <div class="row">
      <img src="img/logo.jpg" alt="MOVENSA">
      <div class="name"><b>MOVENSA Official Store</b><em>Online Baru Saja</em><small>Penyedia Body Cream &amp; Relaksasi Berizin Resmi</small></div>
      <a class="visit" href="#order">KUNJUNGI TOKO</a>
    </div>
    <div class="stats">
      <div><b>100%</b><span>Bahan Pilihan</span></div>
      <div><b>4.9</b><span>Rating Toko</span></div>
      <div><b>100%</b><span>Original Bergaransi</span></div>
    </div>
  </div>

  <div class="desc">
    <h2>MOVENSA BODY COMFORT CREAM</h2>
    <p class="sub">Solusi praktis untuk meredakan kembung dan begah kapan saja!</p>
    <p>Diformulasikan dengan bahan-bahan pilihan yang memberikan efek hangat menenangkan, sangat cocok dioleskan pada perut untuk usir masuk angin maupun saat perut terasa begah. Jangan biarkan perut tidak nyaman mengganggu aktivitas Anda!</p>
  </div>

  <div class="block">
    <h3>KEUNGGULAN MOVENSA BODY COMFORT CREAM</h3>
    <div class="check"><div class="ok">✓</div><div><b>Plant-Based Ingredients</b><span>Menggunakan bahan-bahan berbasis tanaman yang lebih ramah di kulit.</span></div></div>
    <div class="check"><div class="ok">✓</div><div><b>Quick Absorb into Skin</b><span>Teknologi gel yang memastikan produk cepat meresap tanpa meninggalkan rasa lengket di perut atau dada.</span></div></div>
    <div class="check"><div class="ok">✓</div><div><b>Instant Comfort Sensation</b><span>Memberikan rasa hangat dan nyaman seketika pada perut yang kembung, mual atau masuk angin.</span></div></div>
    <div class="check"><div class="ok">✓</div><div><b>Targeted Relief</b><span>Sangat efektif digunakan pada area spesifik seperti Perut (Stomach), Dada (Chest), dan Punggung (Back) untuk meredakan masuk angin dan kembung.</span></div></div>
  </div>

  <div class="formula">
    <h3>FORMULA PILIHAN &amp; MANFAAT NYATA</h3>
    <p>Kombinasi bahan alami berkualitas tinggi untuk memberikan sensasi hangat terbaik</p>
  </div>
  <div style="padding:14px 0 0">
__LONG__
  </div>

  <div class="block">
    <h3>KOMPOSISI UTAMA (INGREDIENTS):</h3>
    <div class="ing"><b>Capsicum Oil</b><span>Memberikan warming sensation (sensasi hangat) untuk membantu melancarkan sirkulasi dan merelaksasi perut yang tegang.</span></div>
    <div class="ing"><b>Menthol Crystal</b><span>Memberikan efek segar dan membantu mengurangi rasa tidak nyaman atau mual.</span></div>
    <div class="ing"><b>Glycerin</b><span>Menjaga kelembapan kulit agar tetap halus saat dioleskan.</span></div>
    <div class="ing"><b>Aqua &amp; Castor Oil</b><span>Basis cream yang ringan dan mempermudah proses pemijatan ringan di perut.</span></div>
  </div>

  <div class="block">
    <p class="eyebrow">MANFAAT PRODUK</p>
    <p class="big">Kembalikan Kenyamanan Tubuh Anda</p>
    <p class="lead">Rasakan sensasi nyaman dan lega tanpa perut begah di sela rutinitas Anda</p>
    <div class="benefit">Membantu meredakan perut begah, kembung, dan masuk angin.</div>
    <div class="benefit">Memberikan rasa hangat dan nyaman pada perut yang terasa melilit atau tidak enak.</div>
    <div class="benefit">Membantu mengatasi mual dan menghangatkan tubuh saat cuaca dingin.</div>
    <div class="benefit">Cocok digunakan sebagai media pijat ringan untuk area perut, dada, dan punggung.</div>
  </div>

  <div class="block">
    <p class="eyebrow">PANDUAN &amp; DETAIL</p>
    <p class="big" style="font-size:16px;color:var(--red)">Cara Penggunaan</p>
    <ol class="steps">
      <li>Oleskan gel secukupnya pada area perut, dada, atau punggung yang terasa kembung/tidak nyaman.</li>
      <li>Pijat secara lembut melingkar hingga gel terserap sepenuhnya ke dalam kulit.</li>
      <li>Gunakan setiap kali Anda membutuhkan kehangatan dan relaksasi ekstra pada perut.</li>
    </ol>
    <p class="big" style="font-size:16px;color:var(--red);margin-top:14px">Detail Produk</p>
    <div class="detail"><div><span>Netto</span><b>50 gram</b></div><div><span>Kemasan</span><b>Jar / Pot (Praktis)</b></div></div>
    <p class="warn">Peringatan: Hanya untuk pemakaian luar. Hindari kontak dengan mata dan luka terbuka. Jauhkan dari jangkauan anak-anak.</p>
  </div>

  <div class="block">
    <div class="reviews-head"><h3 style="margin:0">ULASAN PENGGUNA PILIHAN (950+)</h3><a href="#order">Lihat Semua</a></div>
    <div class="review"><div class="who"><span class="av">S</span>Siti Aminah<span class="when">1 hari lalu</span></div><div class="stars">★★★★★</div><p>"Sangat cocok untuk perut ibu saya yang sering kembung dan begah. Dioles rutin rasanya hangat nyaman. Pengiriman cepat banget."</p></div>
    <div class="review"><div class="who"><span class="av">H</span>Hendra Wijaya<span class="when">2 hari lalu</span></div><div class="stars">★★★★★</div><p>"Perut sering masuk angin karena AC kantor, perlahan sembuh semenjak pakai movensa body comfort cream. Sangat enak buat perut."</p></div>
    <div class="review"><div class="who"><span class="av">D</span>Dewi Lestari<span class="when">3 hari lalu</span></div><div class="stars">★★★★★</div><p>"Udah langganan beli disini, respon admin ramah dan cepat banget nanggapin pertanyaan chat. Wangi creamnya bikin rileks."</p></div>
    <div class="review"><div class="who"><span class="av">M</span>M. Iqbal<span class="when">4 hari lalu</span></div><div class="stars">★★★★☆</div><p>"Khasiatnya oke banget buat meredakan kembung dan begah sehabis makan sembarangan. Nyaman dioles ke perut."</p><img src="img/r1-review.jpg" alt="Foto ulasan" loading="lazy"></div>
  </div>

  <section id="order" class="block">
    <h2>Isi Form Pemesanan</h2>
    <p>Isi data di bawah ini, paket dikirim ke alamat Anda.</p>
__FORM__
  </section>

  <footer><b>MOVENSA Official Store</b>Hak Cipta ©️ 2026. Hak Cipta Dilindungi Undang-Undang.<br>Toko ini dikelola secara independen demi memberikan kepuasan berbelanja terbaik untuk Anda.</footer>
</div>

<div class="sticky" id="sticky"><a class="ico" href="#order"><span>💬</span>Tanya CS</a><a class="ico" href="#toko"><span>🏪</span>Toko</a><a class="btn" href="#order">BELI SEKARANG (COD)</a></div>

__SCRIPT__
<script>
(function () {
  var slides = document.getElementById("slides"), count = document.getElementById("count");
  var thumbs = document.querySelectorAll("#thumbs button"), n = thumbs.length;
  function current() { return Math.round(slides.scrollLeft / slides.clientWidth); }
  slides.addEventListener("scroll", function () {
    var i = current();
    count.textContent = (i + 1) + "/" + n;
    thumbs.forEach(function (t, j) { t.classList.toggle("on", i === j); });
  }, { passive: true });
  thumbs.forEach(function (t) {
    t.addEventListener("click", function () { slides.scrollTo({ left: Number(t.dataset.i) * slides.clientWidth, behavior: "smooth" }); });
  });
})();
</script>
</body>
</html>
"""


def build():
    html = (PAGE.replace("__SLIDES__", slides).replace("__THUMBS__", thumbs)
            .replace("__N__", str(len(GALLERY))).replace("__LONG__", long_imgs)
            .replace("__CHECKOUT_CSS__", CHECKOUT_CSS.rstrip("\n"))
            .replace("__FORM__", FORM).replace("__SCRIPT__", SCRIPT))
    for old, new in EXACT_SCRIPT_PATCHES:
        assert html.count(old) == 1, old
        html = html.replace(old, new)
    html = html.replace('id="productName">Meora Natural Glow Balm<', 'id="productName">Movensa Body Comfort Cream 50g<')
    html = html.replace('id="submitBtn">Beli Sekarang<', 'id="submitBtn">BELI SEKARANG<')
    html = html.replace('btn.textContent = "Beli Sekarang";', 'btn.textContent = "BELI SEKARANG";')
    assert "Meora" not in html
    return html


def with_cdn(html, sha):
    return re.sub(r'src="img/', f'src="https://cdn.jsdelivr.net/gh/akbarseft86/dropship-baru@{sha}/{FOLDER}/img/', html)


if __name__ == "__main__":
    sha = sys.argv[1] if len(sys.argv) > 1 else None
    html = build()
    (ROOT / FOLDER / "index.html").write_text(html)
    if sha:
        (ROOT / FOLDER / "index.scalev.html").write_text(with_cdn(html, sha))
