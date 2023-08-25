### Analisis Trip Pengguna Jasa Taksi

Sebuah perusahaan bernama Zuber yang bergerak dibidang `ride-sharing` merupakan perusahaan baru yang diluncurkan di Chicago ingin menemukan pola pada informasi yang tersedia. Perusahaan ingin memahami preferensi penumpang dan dampak faktor eksternal terhadap perjalanan. Analisis ini merupakan kelanjutan dari analisis sebelumnya menggunakan SQL untuk mendapatkan data-data yang relevan untuk dianalisis menggunakan Python. Beberapa analisis berupa tujuan dan hipotesis yang diajukan, dimuat sebagai berikut:
- Perusahaan taksi manakah yang memiliki jumlah trip terbanyak pada tanggal 15-16 November 2017
- Mengetahui distribusi data jumlah trips dari seluruh perushaan pada tanggal 15-16 November 2017
- Mengetahui lokasi favorit (`dropoff_location`) manakah yang sering dikunjungi pengguna selama bulan November 2017
- Mengetahui distribusi data dari rata-rata trip ditiap lokasi dropoff selama bulan November 2017
- Menguji hipotesis: Benarkah durasi rata-rata perjalanan dari Loop ke Bandara Internasional O'Hare berubah pada hari-hari Sabtu yang hujan

| Projek | Deskripsi | Modul |
| ------- | ------- | ------- |
| [Penggunaan Trip Jasa Taksi](https://github.com/fuadraharjo/TripleTen_IND/blob/main/Projek-4%20-%20Penggunaan%20Trip%20Jasa%20Taksi/Analisis%20trip%20pengguna%20jasa%20taksi.ipynb) | Analisis preferensi pengguna taksi dari perusahaan Zuber terhadap beberapa faktor seperti `dropoff location`, `company name` dan uji hipotesis menggunakan *scipy*. | *pandas*, *numpy*, *matplotlib*, *seaborn*, *re*, *scipy* , *requests*, *SQL*, *bs4*|