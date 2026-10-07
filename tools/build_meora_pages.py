"""Build the extra Meora landing pages, reusing the checkout form from meora/index.html."""
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
base = (ROOT / "meora/index.html").read_text()

CHECKOUT_CSS = base[base.index("  .btn {"):base.index("  footer {")]
FORM = base[base.index('    <form class="card" id="orderForm"'):base.index("    </form>") + len("    </form>")]
SCRIPT = base[base.index("<script>"):base.index("</script>") + len("</script>")]

FA1 = """<!doctype html>
<html lang="id">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Meora – Kekuatan Alami Papua</title>
<meta name="description" content="Meora balm dengan ekstrak Buah Merah Papua.">
<meta name="theme-color" content="#a3382a">
<style>
  :root {
    --red: #a3382a;
    --red-dark: #7d2a1f;
    --brown: #4a2c22;
    --gold: #8a6a2f;
    --green: #2f4a2a;
    --cream: #fdfaf5;
    --text: #3a2a24;
    --muted: #7a6a62;
    --border: #eadfce;
  }
  * { box-sizing: border-box; }
  html { scroll-behavior: smooth; }
  body {
    margin: 0; background: #f5efe6; color: var(--text);
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    font-size: 16px; line-height: 1.55;
  }
  .serif { font-family: Georgia, "Times New Roman", serif; }
  .wrap { max-width: 480px; margin: 0 auto; background: var(--cream); padding-bottom: 88px; box-shadow: 0 0 24px rgba(0,0,0,.06); }
  .topbar { text-align: center; font-size: 12px; font-weight: 600; letter-spacing: .4px; color: var(--muted); padding: 12px 16px; border-bottom: 1px solid var(--red); }
  section { padding: 28px 20px; border-bottom: 1px solid var(--border); }
  .center { text-align: center; }
  .pills { display: flex; justify-content: center; gap: 8px; flex-wrap: wrap; }
  .pill { border: 1px solid #d8c7ad; border-radius: 999px; padding: 5px 12px; font-size: 11px; font-weight: 700; letter-spacing: .6px; color: var(--red); }
  .pill.gold { color: var(--gold); }
  h1 { font-family: Georgia, serif; color: var(--red); font-size: 34px; line-height: 1.15; margin: 18px 0 10px; letter-spacing: 1px; }
  h2 { font-family: Georgia, serif; color: var(--brown); font-size: 26px; line-height: 1.25; margin: 6px 0 16px; font-weight: 600; }
  h3 { font-family: Georgia, serif; color: var(--brown); font-size: 21px; margin: 24px 0 12px; padding-bottom: 8px; border-bottom: 1px solid var(--border); font-weight: 600; }
  .lead { color: #6a4a3e; margin: 0 0 18px; }
  .eyebrow { font-size: 12px; font-weight: 700; letter-spacing: 1.6px; color: var(--gold); text-transform: uppercase; }
  .eyebrow.red { color: #c9826f; }
  .img-card { position: relative; margin: 8px 0 26px; }
  .img-card img { display: block; width: 100%; height: auto; border-radius: 6px; }
  .img-card .tag {
    position: absolute; left: 50%; bottom: -16px; transform: translateX(-50%); white-space: nowrap;
    background: #fff; border-radius: 999px; padding: 7px 16px; font-size: 13px; font-weight: 700; letter-spacing: .6px;
    color: var(--red); box-shadow: 0 2px 10px rgba(0,0,0,.12);
  }
  .img-card .tag.muted { color: var(--muted); }
  .facts { display: grid; grid-template-columns: repeat(3, 1fr); border: 1px solid var(--border); border-radius: 12px; background: #fff; padding: 14px 6px; text-align: center; }
  .facts div + div { border-left: 1px solid var(--border); }
  .facts b { display: block; font-size: 15px; color: var(--brown); }
  .facts span { font-size: 12px; color: var(--muted); }
  .link-cta { display: block; text-align: center; margin: 26px 0 4px; font-weight: 800; letter-spacing: .6px; color: #2f4f8a; text-decoration: none; }
  .problems { list-style: none; margin: 0; padding: 18px 20px; border: 1px solid var(--border); border-radius: 12px; background: #fff; }
  .problems li { position: relative; padding-left: 28px; margin: 10px 0; }
  .problems li::before { content: "✕"; position: absolute; left: 0; color: #c0392b; font-weight: 700; }
  blockquote { margin: 20px 0 0; padding: 14px 18px; border-left: 4px solid var(--red); background: #fff; font-family: Georgia, serif; font-style: italic; color: #4a3a34; }
  .ing { display: flex; gap: 14px; border: 1px solid var(--border); border-radius: 12px; background: #fff; padding: 16px; margin-bottom: 14px; }
  .ico { flex: 0 0 44px; height: 44px; border-radius: 50%; border: 1px solid #e3cfc3; display: flex; align-items: center; justify-content: center; color: var(--red); font-size: 20px; }
  .ing h4 { margin: 0; color: var(--red); font-size: 17px; letter-spacing: .4px; }
  .ing small { display: block; color: var(--gold); font-weight: 700; font-size: 14px; margin: 2px 0 6px; }
  .ing p { margin: 0; font-size: 15px; }
  .benefits { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }
  .benefit { border: 1px solid var(--border); border-radius: 12px; background: #fff; padding: 14px; font-size: 13px; color: #5a4a44; }
  .benefit .ico { width: 36px; height: 36px; flex: none; font-size: 16px; margin-bottom: 8px; }
  .benefit b { display: block; color: var(--brown); font-size: 14px; margin-bottom: 4px; }
  .offer { border: 2px solid var(--red); border-radius: 14px; background: #fff; padding: 18px; text-align: center; }
  .offer img { display: block; width: 100%; height: auto; border-radius: 6px; }
  .offer .label { margin-top: 16px; font-weight: 800; letter-spacing: .6px; color: var(--red); }
  .offer .price { font-size: 34px; font-weight: 800; color: var(--brown); margin: 2px 0 10px; }
  .offer .chip { display: inline-block; border: 1px solid #e3b3a6; border-radius: 999px; padding: 6px 14px; font-size: 13px; font-weight: 700; color: var(--red); }
  .form-wrap { margin-top: 22px; border: 1px solid var(--border); border-radius: 14px; background: #fff; padding: 20px 16px; }
  .form-wrap > p { text-align: center; font-size: 14px; color: #5a4a44; margin: 0 0 16px; }
  .assure { display: flex; justify-content: space-around; margin-top: 18px; padding-top: 14px; border-top: 1px solid var(--border); font-size: 12px; color: #5a4a44; text-align: center; }
  .review { border: 1px solid var(--border); border-radius: 12px; background: #fff; padding: 18px; margin-bottom: 14px; }
  .stars { color: #8a6a2f; letter-spacing: 2px; }
  .review p { font-style: italic; margin: 8px 0 14px; }
  .who { display: flex; align-items: center; gap: 12px; }
  .who img { width: 50px; height: 50px; object-fit: cover; border-radius: 4px; }
  .who b { display: block; }
  .who span { font-size: 12px; color: var(--muted); }
  .wa { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }
  .wa img { width: 100%; height: auto; border-radius: 8px; border: 1px solid var(--border); }
  details { border: 1px solid var(--border); border-radius: 10px; background: #fff; margin-bottom: 12px; }
  summary { cursor: pointer; padding: 14px 16px; font-weight: 600; list-style: none; display: flex; justify-content: space-between; }
  summary::after { content: "⌄"; color: var(--red); }
  details[open] summary::after { content: "⌃"; }
  details p { margin: 0; padding: 0 16px 14px; font-size: 15px; color: #5a4a44; }
  .card { border-color: var(--border); }
__CHECKOUT_CSS__
  .sticky .btn { background: #fff; color: #5a6f9a; box-shadow: 0 -2px 14px rgba(0,0,0,.08); border: 1px solid var(--border); letter-spacing: .6px; }
  footer { text-align: center; font-size: 12px; color: var(--muted); padding: 16px; }
</style>
</head>
<body>
<div class="wrap">
  <div class="topbar">PROMO SPESIAL: DISKON 50% &amp; BISA COD SELURUH INDONESIA!</div>

  <section class="center">
    <div class="pills"><span class="pill">🍃 100% BAHAN ALAMI</span><span class="pill gold">★ PREMIUM QUALITY</span></div>
    <h1>KEKUATAN<br>ALAMI PAPUA</h1>
    <p class="lead">Rahasia kecantikan eksotis dengan ekstrak Buah Merah murni untuk kulit sehat, lembap, dan bercahaya.</p>
    <div class="img-card"><img src="img/01-hero.jpg" alt="Meora – bekas luka menonjol seperti keloid"><span class="tag">DIPERKAYA BUAH MERAH ASLI</span></div>
    <div class="facts">
      <div><b>Buah Merah</b><span>Papua Asli</span></div>
      <div><b>Tekstur Balm</b><span>Lembut di Kulit</span></div>
      <div><b>100%</b><span>Bahan Natural</span></div>
    </div>
    <a class="link-cta" href="#order">DAPATKAN KULIT SEHAT SEKARANG</a>
  </section>

  <section>
    <p class="eyebrow red center">KENALI MASALAH KULITMU</p>
    <h2 class="center">Apakah Anda Mengalami Ini?</h2>
    <div class="img-card"><img src="img/02-10x.jpg" alt="Masalah dan solusi bekas luka" loading="lazy"><span class="tag muted">MASALAH KULIT WAJAH?</span></div>
    <ul class="problems">
      <li>Kulit terasa sangat kering, bersisik, dan kusam.</li>
      <li>Banyak noda hitam dan warna kulit tidak merata.</li>
      <li>Tanda-tanda penuaan dini mulai muncul (garis halus).</li>
      <li>Sudah mencoba berbagai produk tapi kulit tetap rentan iritasi.</li>
    </ul>
    <blockquote>"Kunci kulit sehat bukan pada bahan kimia keras, melainkan pada nutrisi alami yang tepat."</blockquote>
  </section>

  <section>
    <p class="eyebrow center">FORMULASI PREMIUM</p>
    <h2 class="center">Kandungan Alami &amp; Manfaatnya</h2>
    <div class="img-card"><img src="img/03-tumpas.jpg" alt="3 kandungan alami Meora" loading="lazy"><span class="tag muted">🔍 DETAIL FORMULA</span></div>
    <h3>Kandungan Utama</h3>
    <div class="ing"><div class="ico">🍂</div><div><h4>EKSTRAK BUAH MERAH</h4><small>Antioksidan &amp; Vitamin E</small><p>Rahasia awet muda dari Papua. Sangat kaya akan tokoferol dan betakaroten yang terbukti ampuh menangkal radikal bebas dan mempercepat regenerasi sel kulit.</p></div></div>
    <div class="ing"><div class="ico">💧</div><div><h4>MINYAK KELAPA DARA</h4><small>Pelembap Alami Intensif</small><p>Mengunci kelembapan alami kulit dari dalam, memperbaiki <i>skin barrier</i> yang rusak, dan membuat tekstur kulit menjadi sangat halus dan kenyal.</p></div></div>
    <div class="ing"><div class="ico">🌱</div><div><h4>EKSTRAK TUMBUHAN HERBAL</h4><small>Menenangkan &amp; Menyegarkan</small><p>Paduan herbal pilihan yang berfungsi menenangkan kulit kemerahan, meredakan peradangan, dan memberikan sensasi segar sepanjang hari.</p></div></div>
    <h3>Manfaat Untuk Kulit Anda</h3>
    <div class="benefits">
      <div class="benefit"><div class="ico">💧</div><b>Hidrasi Mendalam</b>Melembapkan kulit secara intensif dan tahan lama. Selamat tinggal kulit kering.</div>
      <div class="benefit"><div class="ico">✨</div><b>Mencerahkan &amp; Meratakan</b>Membantu mengurangi noda hitam dan mencerahkan kulit kusam secara bertahap.</div>
      <div class="benefit"><div class="ico">🛡️</div><b>Perlindungan Antioksidan</b>Melindungi sel kulit dari kerusakan akibat radikal bebas dan polusi lingkungan.</div>
      <div class="benefit"><div class="ico">🌱</div><b>Menutrisi &amp; Meregenerasi</b>Memelihara kesehatan kulit secara menyeluruh dan membantu proses peremajaan sel.</div>
    </div>
  </section>

  <section id="order">
    <p class="eyebrow red center">PENAWARAN SPESIAL HARI INI</p>
    <h2 class="center">Kembalikan Pesona Alami Kulitmu ✨</h2>
    <div class="offer">
      <img src="img/04-offer.jpg" alt="Meora – Kekuatan Alami Papua, diskon 50%" loading="lazy">
      <div class="label">PROMO EKSKLUSIF</div>
      <div class="price" id="offerPrice">Rp 99.000,-</div>
      <span class="chip">DISKON 50% &amp; BISA COD</span>
    </div>
    <div class="form-wrap">
      <h2 class="center" style="font-size:22px;margin:0 0 6px">Isi Form Pengiriman</h2>
      <p>Isi data di bawah ini, kami akan mengirimkan paket ke rumah Anda (Bisa Bayar di Tempat/COD)</p>
__FORM__
      <div class="assure"><span>🔒<br>Privasi Aman</span><span>📦<br>Bisa Buka Dulu</span><span>🏅<br>Garansi Ori</span></div>
    </div>
  </section>

  <section>
    <p class="eyebrow center">BUKTI NYATA</p>
    <h2 class="center">Apa Kata Mereka?</h2>
    <p class="center lead" style="font-size:14px">Pelanggan setia kami telah membuktikan sendiri manfaat luar biasa dari ekstrak Buah Merah.</p>
    <div class="review"><div class="stars">★★★★★</div><p>"Awalnya udah pasrah banget sama kulit wajah yang kusam dan banyak flek hitam. Pas coba telaten pakai krim Meora ini tiap malam, tekstur kulit perlahan jadi kenyal dan cerah. Flek juga makin pudar merata sama warna kulit asli. Hasilnya bener-bener nyata!"</p><div class="who"><img src="img/av-arini.jpg" alt=""><div><b>Arini Putri</b><span>Karyawan, 32 Tahun</span></div></div></div>
    <div class="review"><div class="stars">★★★★★</div><p>"Sumpah bagus banget produk ini! Kulitku yang tadinya super kering sampai bersisik, sekarang udah jauh lebih lembap dan glowing setelah rutin pakai. Teksturnya nyaman banget di kulit, nggak lengket, dan cepet meresap."</p><div class="who"><img src="img/av-diana.jpg" alt=""><div><b>Diana S.</b><span>Ibu Rumah Tangga, 28 Tahun</span></div></div></div>
    <div class="review"><div class="stars">★★★★★</div><p>"Puas banget! Krim perawatan wajah paling mantul. Kandungan alaminya ramah banget di kulit, nggak bikin iritasi sama sekali. Pemakaian rutin sebulan udah kelihatan lebih awet muda!"</p><div class="who"><img src="img/av-nita.jpg" alt=""><div><b>Nita Maharani</b><span>Wiraswasta, 35 Tahun</span></div></div></div>
    <div class="wa"><img src="img/wa-ayu.jpg" alt="Testimoni WhatsApp" loading="lazy"><img src="img/wa-diana.jpg" alt="Testimoni WhatsApp" loading="lazy"></div>
  </section>

  <section>
    <h2 class="center">Pertanyaan Sering Diajukan</h2>
    <details><summary>Apakah Meora aman untuk kulit sensitif?</summary><p>Meora dibuat dari bahan alami. Untuk kulit sensitif, oleskan sedikit di lengan bagian dalam dan tunggu 24 jam sebelum dipakai di area yang lebih luas.</p></details>
    <details><summary>Berapa lama hasilnya mulai terlihat?</summary><p>Hasil berbeda pada tiap orang, tergantung kondisi kulit dan rutinitas pemakaian. Gunakan secara rutin setiap hari.</p></details>
    <details><summary>Apakah bisa dipakai siang dan malam?</summary><p>Bisa. Oleskan tipis-tipis pada kulit yang bersih, pagi dan malam.</p></details>
    <details><summary>Apakah melayani pembayaran di tempat (COD)?</summary><p>Metode pembayaran yang tersedia ditampilkan di form pemesanan di atas.</p></details>
  </section>

  <footer>© Meora – Reseller Resmi</footer>
</div>

<div class="sticky" id="sticky"><a class="btn" href="#order">🛍 AMBIL DISKON 50% (COD)</a></div>

__SCRIPT__
</body>
</html>
"""

M2 = """<!doctype html>
<html lang="id">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Meora Balm – Rawat Bekas Luka</title>
<meta name="description" content="Meora balm dengan ekstrak Buah Merah Papua.">
<meta name="theme-color" content="#2f3237">
<style>
  :root {
    --red: #d81f26;
    --red-dark: #a3161b;
    --green: #2f4a2a;
    --text: #2f3237;
    --muted: #6b6b6b;
    --border: #e2e2e2;
  }
  * { box-sizing: border-box; }
  html { scroll-behavior: smooth; }
  body { margin: 0; background: #f4f4f4; color: var(--text); font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; font-size: 16px; line-height: 1.5; }
  .wrap { max-width: 480px; margin: 0 auto; background: #fff; padding-bottom: 88px; }
  .head { text-align: center; padding: 16px 16px 10px; }
  .head h1 { font-size: 17px; margin: 0 0 4px; font-weight: 800; }
  .head p { margin: 0; color: #9a9a9a; font-size: 15px; }
  img.full { display: block; width: 100%; height: auto; }
  .block { padding: 18px 16px; }
  h2 { text-align: center; font-size: 22px; margin: 6px 0 14px; font-weight: 800; }
  .checks { list-style: none; padding: 0; margin: 0; }
  .checks li { margin: 10px 0; padding-left: 28px; position: relative; font-size: 15px; }
  .checks li::before { content: "✅"; position: absolute; left: 0; }
  hr { border: 0; border-top: 2px solid #111; margin: 18px 16px; }
  .sub { text-align: center; color: #555; margin: -6px 0 6px; font-size: 15px; }
  .benefits { margin: 0; padding-left: 20px; }
  .benefits li { margin: 8px 0; font-size: 15px; }
  .proof { margin: 0 16px; border: 2px solid #111; text-align: center; font-weight: 800; font-size: 14px; padding: 10px; }
  #order { padding: 8px 16px 20px; }
__CHECKOUT_CSS__
  footer { text-align: center; font-size: 12px; color: var(--muted); padding: 16px; }
</style>
</head>
<body>
<div class="wrap">
  <div class="head">
    <h1>PROMO SPESIAL DISKON 50% BISA COD SELURUH INDONESIA!</h1>
    <p>Kembalikan Kulit Mulusmu, Hapus Jejak Luka Tanpa Bekas.</p>
  </div>
  <a href="#order"><img class="full" src="img/01-hero.jpg" alt="Meora – punya bekas luka menonjol seperti keloid?"></a>

  <div class="block">
    <h2>Apakah ini yang Kamu rasakan?</h2>
    <ul class="checks">
      <li><b>Keloid Menonjol:</b> Membuat tidak percaya diri saat berpakaian terbuka.</li>
      <li><b>Bekas Luka Operasi / Sesar:</b> Garis gelap yang merusak kulit jadi tidak mulus.</li>
      <li><b>Noda Hitam Gigitan Nyamuk/Knalpot:</b> Membekas bertahun-tahun dan susah hilang.</li>
      <li><b>Tekstur Kulit Kasar:</b> Luka lama yang mengeras &amp; menghitam.</li>
    </ul>
  </div>
  <hr>
  <div class="block" style="padding-top:4px">
    <h2>MEORA BALM + Ultra Scar Eraser</h2>
    <p class="sub">Sekali Oles Keloid &amp; Bekas Luka Beres</p>
  </div>
  <img class="full" src="img/02-tumpas.jpg" alt="3 kandungan alami Meora" loading="lazy">

  <div class="block">
    <h2>Manfaat MEORA BALM</h2>
    <ul class="benefits">
      <li>Membantu <b>merawat kulit pada area bekas luka menonjol</b></li>
      <li>Membantu menjaga <b>kelembapan area keloid</b></li>
      <li>Membantu membuat kulit terasa <b>lebih halus &amp; lembut</b></li>
      <li>Membantu merawat <b>tekstur kulit yang tidak rata</b></li>
      <li>Membantu menjaga <b>elastisitas kulit di area bekas luka</b></li>
      <li>Membantu membuat kulit tampak <b>lebih terawat</b></li>
    </ul>
  </div>
  <img class="full" src="img/03-10x.jpg" alt="Before after bekas luka" loading="lazy">
  <div class="proof">Bukan Katanya, Tapi Realitanya! 15.420+ Orang Sudah Buktikan Sendiri.</div>
  <div style="height:16px"></div>
  <img class="full" src="img/04-testimoni.jpg" alt="Testimoni pemakai Meora Balm" loading="lazy">

  <div class="block"><h2>BERSERTIFIKASI BPOM</h2></div>
  <img class="full" src="img/05-bpom.jpg" alt="Detail produk BPOM" loading="lazy">

  <div class="block"><h2>PROMO SPESIAL HARI INI !</h2></div>
  <img class="full" src="img/06-promo.jpg" alt="Promo hari ini diskon 50%" loading="lazy">
  <hr>

  <section id="order">
    <img class="full" src="img/07-isi-form.jpg" alt="Isi form di bawah ini untuk pemesanan" loading="lazy" style="margin-bottom:12px">
__FORM__
  </section>

  <img class="full" src="img/08-penting.jpg" alt="Produk yang kami jual 100% original" loading="lazy">
  <img class="full" src="img/09-warning.jpg" alt="Pastikan order hanya di website ini" loading="lazy">
  <footer>© Meora – Reseller Resmi</footer>
</div>

<div class="sticky" id="sticky"><a class="btn" href="#order">Beli Sekarang</a></div>

__SCRIPT__
</body>
</html>
"""


# Exact replicas of the reference pages (kept separate so the edited versions stay untouched).
FA1_EXACT = (FA1
    .replace("""    <p class="lead">Rahasia kecantikan eksotis dengan ekstrak Buah Merah murni untuk kulit sehat, lembap, dan bercahaya.</p>
""", """    <p class="lead">Rahasia kecantikan eksotis dengan ekstrak Buah Merah murni untuk kulit sehat, lembap, dan bercahaya.</p>
    <div class="viewers"><b>125</b> orang sedang melihat halaman ini</div>
""")
    .replace("""      <div><b>Buah Merah</b><span>Papua Asli</span></div>
      <div><b>Tekstur Balm</b><span>Lembut di Kulit</span></div>
      <div><b>100%</b><span>Bahan Natural</span></div>""", """      <div><b>4.9<small>★</small></b><span>Rating Kepuasan</span></div>
      <div><b>10k+</b><span>Wanita Terbantu</span></div>
      <div><b>100%</b><span>Bahan Natural</span></div>""")
    .replace("""      <span class="chip">DISKON 50% &amp; BISA COD</span>
""", """      <span class="chip">DISKON 50% &amp; BISA COD</span>
      <div class="timer"><small>PROMO BERAKHIR DALAM:</small><div>00 <i>:</i> 15 <i>:</i> 00</div></div>
      <div class="stock">⚠️ Perhatian: Stok promo hari ini tersisa <u>12 jar</u> saja!</div>
""")
    .replace("  .card { border-color: var(--border); }", """  .card { border-color: var(--border); }
  .viewers { display: inline-block; border: 1px solid var(--border); border-radius: 999px; padding: 6px 18px; font-size: 13px; color: #5a4a44; margin: 0 0 22px; background: #fff; }
  .facts small { color: var(--gold); font-size: 12px; }
  .timer { margin: 16px 0 10px; border: 1px solid var(--border); border-radius: 10px; padding: 12px; }
  .timer small { display: block; font-size: 11px; font-weight: 700; letter-spacing: .6px; color: #6a5a52; }
  .timer div { font-size: 16px; letter-spacing: 2px; color: #9a9a9a; margin-top: 4px; }
  .timer i { color: var(--red); font-style: normal; font-weight: 700; }
  .stock { font-size: 13px; font-weight: 700; color: #d9826f; border-radius: 8px; padding: 8px; box-shadow: 0 1px 6px rgba(0,0,0,.06); }"""))

M2_EXACT = (M2
    .replace("""    <img class="full" src="img/07-isi-form.jpg" alt="Isi form di bawah ini untuk pemesanan" loading="lazy" style="margin-bottom:12px">
""", """    <img class="full" src="img/07-isi-form.jpg" alt="Isi form di bawah ini untuk pemesanan" loading="lazy" style="margin-bottom:12px">
    <p style="font-weight:700;margin:8px 0 6px">Pilihan Produk</p>
    <label class="opt" style="margin-bottom:14px"><input type="radio" checked> Promo 99rb Dapat 1PCS</label>
""")
    .replace("""<div class="sticky" id="sticky"><a class="btn" href="#order">Beli Sekarang</a></div>
""", ""))

# The exact replicas keep their own button labels and may have no sticky bar.
EXACT_SCRIPT_PATCHES = [
    ("""  if ("IntersectionObserver" in window) {""", """  if ("IntersectionObserver" in window && $("sticky")) {"""),
    ("""    if (state.variant) {
      $("sticky")""", """    if (state.variant && $("sticky") && $("sticky").hasAttribute("data-price-label")) {
      $("sticky")"""),
]


def render_exact(template, submit_label=None, address_placeholder=None):
    html = render(template)
    for old, new in EXACT_SCRIPT_PATCHES:
        assert html.count(old) == 1, old
        html = html.replace(old, new)
    if submit_label:
        html = html.replace('id="submitBtn">Beli Sekarang<', f'id="submitBtn">{submit_label}<')
        html = html.replace('btn.textContent = "Beli Sekarang";', f'btn.textContent = "{submit_label}";')
    if address_placeholder:
        html = html.replace('placeholder="Nama jalan, nomor rumah, RT/RW, patokan"', f'placeholder="{address_placeholder}"')
    return html


def render(template):
    return (template.replace("__CHECKOUT_CSS__", CHECKOUT_CSS.rstrip("\n"))
            .replace("__FORM__", FORM)
            .replace("__SCRIPT__", SCRIPT))


def with_cdn(html, folder, sha):
    return re.sub(r'src="(?:\.\./[\w-]+/)?img/', lambda m: f'src="https://cdn.jsdelivr.net/gh/akbarseft86/dropship-baru@{sha}/{img_folder(m.group(0), folder)}/img/', html)


def img_folder(match, folder):
    m = re.match(r'src="\.\./([\w-]+)/img/', match)
    return m.group(1) if m else folder


if __name__ == "__main__":
    import sys
    sha = sys.argv[1] if len(sys.argv) > 1 else None
    for folder, tpl in (("meora-fa1", FA1), ("meora-2", M2)):
        html = render(tpl)
        (ROOT / folder / "index.html").write_text(html)
        if sha:
            (ROOT / folder / "index.scalev.html").write_text(with_cdn(html, folder, sha))
    exact = (
        ("meora-fa1-persis", "meora-fa1", render_exact(FA1_EXACT, "Selesaikan Pesanan",
            "Alamat Lengkap Anda (Kelurahan, Nama Jln/Gang, RT/RW, No Rumah, Patokan Lain)")),
        ("meora-2-persis", "meora-2", render_exact(M2_EXACT, None, "Alamat Lengkap Anda")),
    )
    for folder, img_src, html in exact:
        html = html.replace('src="img/', f'src="../{img_src}/img/')
        (ROOT / folder).mkdir(exist_ok=True)
        (ROOT / folder / "index.html").write_text(html)
        if sha:
            (ROOT / folder / "index.scalev.html").write_text(with_cdn(html, folder, sha))
