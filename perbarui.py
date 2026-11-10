"""Salin halaman kasir dari folder Apps Script ke situs GitHub Pages ini.

Sumber utama tetap kasir-cahaya-77/apps-script/Index.html (dipakai juga oleh link /exec).
Jalankan setelah Index.html diubah:  python perbarui.py  lalu commit + push.
Di situs ini halaman memanggil Apps Script lewat alamat /exec (mode API), dan cetak Bluetooth
berjalan langsung dari halaman karena tidak berada di dalam bingkai Google.
Kode versi (12 huruf dari isi halaman) ditulis ke halaman dan ke versi.txt; halaman yang masih
terbuka di HP membandingkannya lalu menampilkan bar "Ada versi baru".
"""
import hashlib, os

DIR = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(DIR, '..', 'kasir-cahaya-77', 'apps-script', 'Index.html')

s = open(SRC, encoding='utf-8').read()
head = ('<link rel="manifest" href="manifest.webmanifest">\n'
        '<link rel="icon" type="image/png" href="ikon-192.png">\n'
        '<link rel="apple-touch-icon" href="ikon-192.png">\n'
        '<meta name="theme-color" content="#121a55">\n')
a = '<title>Kios Cahaya 77</title>\n'
assert s.count(a) == 1
s = s.replace(a, a + head)
versi = hashlib.sha256(s.encode('utf-8')).hexdigest()[:12]
b = "const VERSI_SITUS = '';"
assert s.count(b) == 1
s = s.replace(b, "const VERSI_SITUS = '" + versi + "';")
open(os.path.join(DIR, 'index.html'), 'w', encoding='utf-8', newline='').write(s)
open(os.path.join(DIR, 'versi.txt'), 'w', encoding='utf-8', newline='').write(versi + '\n')
print('index.html diperbarui, versi ' + versi)
