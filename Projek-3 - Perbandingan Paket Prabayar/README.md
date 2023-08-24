### Studi Perbandingan Paket Prabayar: Surf vs. Ultimate di Perusahaan Megaline

Seorang analis di perusahaan operator telekomunikasi `Megaline` diminta oleh perusahaan tersebut menganalisis dua jenis paket prabayar, yaitu paket `Surf` dan paket `Ultimate`. Departemen periklanan perusahaan tersebut ingin mengetahui paket prabayar mana yang menghasilkan lebih banyak pendapatan, sehingga mereka bisa membuat anggaran iklan yang sesuai.

Kita akan melakukan analisis awal untuk paket-paket prabayar tersebut berdasarkan sampel klien yang berukuran relatif kecil. kita memiliki 500 data klien `Megaline`, yang berisi informasi seperti: siapa mereka, dari mana asalnya, jenis paket apa yang mereka gunakan, serta jumlah panggilan dan pesan yang mereka kirim di tahun 2018. Tugas kita adalah untuk menganalisis perilaku para pengguna, lalu menentukan paket prabayar manakah yang lebih menguntungkan bagi perusahaan `Megaline`.

Dataset yang dimiliki perusahaan `Megaline` diantaranya berisi `'calls'`, `'internet'`, `'messages'`, `'plans'` dan `'users'`yang semuanya memiliki informasi yang penting untuk analisis projek ini. Tujuan dari projek ini adalah selain untuk mencari pendapatan terbanyak dari kedua paket prabayar tersebut namun juga menganalisis prilaku pengguna seperti `durasi telepon`, `jumlah sms` dan `jumlah penggunaan data internet` terhadap kedua paket prabayar tersebut. Beberapa hipotesis diajukan sebagai berikut:
- Benarkah untuk kategori `durasi telepon` terbanyak dalam satu bulan dimiliki oleh `Paket Surf`?
- Benarkah untuk kategori `jumlah sms` terbanyak dalam satu bulan dimiliki oleh `Paket Surf`?
- Benarkah rata-rata penggunaan jumlah data internet per bulan untuk kedua tipe `Paket Prabayar` berkisar `16 GB`?
- Benarkah jumlah pendapatan terbanyak dari pengguna per bulan dimiliki oleh `Paket Ultimate`?
- Benarkah Pendapatan Rata-rata dari Pengguna Paket Prabayar Ultimate dan Surf Berbeda?
- Benarkah Pendapatan Rata-rata dari Pengguna di Wilayah NY-NJ dengan Wilayah Lain adalah Berbeda?

| Projek | Deskripsi | Modul |
| ------- | ------- | ------- |
| [Perbandingan Paket Prabayar](https://github.com/fuadraharjo/TripleTen_IND/blob/main/Projek-3%20-%20Perbandingan%20Paket%20Prabayar/Studi%20perbandingan%20paket%20prabayar%20surf%20dan%20ultimate.ipynb) | Departemen periklanan perusahaan `Megaline` ingin mengetahui paket prabayar mana yang menghasilkan lebih banyak pendapatan, sehingga mereka bisa membuat anggaran iklan yang sesuai. Analisis dan Uji Hipotesis dilibatkan dalam projek ini. | *pandas*, *numpy*, *matplotlib*, *seaborn*, *math*, *scipy* |