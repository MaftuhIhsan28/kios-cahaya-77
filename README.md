# Kios Cahaya 77

Dashboard harga dan kasir Kios Cahaya 77, dibuka di https://maftuhihsan28.github.io/kios-cahaya-77/

- Data (daftar harga, info kios, pulsa) tetap di Google Sheet. Halaman ini membacanya dan menyimpannya
  lewat Apps Script (alamat `/exec`), jadi repo ini tidak berisi data, kunci AI, atau PIN.
- Karena tidak berada di dalam bingkai Google, cetak Bluetooth (printer RPP02N) dan mikrofon asisten
  bisa dipakai langsung dari halaman.
- Sumber halaman: `kasir-cahaya-77/apps-script/Index.html`. Setelah mengubahnya, jalankan
  `python perbarui.py`, lalu commit dan push.
