### Model Prediksi Paket Seluler Pengguna Menggunakan Machine Learning

Sebuah operator seluler bernama `Megaline` merasa tidak puas karena banyak pelanggan mereka yang 
masih menggunakan paket lama. Perusahaan tersebut ingin mengembangkan sebuah 
model yang dapat menganalisis perilaku konsumen dan merekomendasikan salah satu 
dari kedua paket terbaru Megaline: `Smart` atau `Ultra`.

`Megaline` memiliki dataset yang berisi prilaku pengguna paket `Smart` dan `Ultra`. Disini kita akan memuat `model machine learning` untuk menentukan paket mana yang diberikan berdasarkan prilaku pelanggan (`jumlah panggilan`, `durasi panggilan`, `sms`, `jumlah paket data`) tersebut. Pada proyek ini, ambang batas untuk tingkat accuracy-nya adalah 0,75. 

Beberapa tujuan dan rumusan masalah dari analisis projek ini:
- Mengetahui algoritma terbaik untuk `model machine learning` untuk dataset `Megaline`
- `Hyperparameter` terbaik seperti apa pada `model machine learning`
- Apakah `model machine learning` yang dipilih bisa memenuhi uji kelayakan (`sanity check`)?
- Benarkah `model machine learning` yang dipilih bisa menguji sampel data sembarang?

| Projek | Deskripsi | modul |
| ------- | ------- | ------- |
| [Model Prediksi Paket Seluler](https://github.com/fuadraharjo/TripleTen_IND/blob/main/Projek-5%20-%20Model%20Prediksi%20Paket%20Seluler/Model%20prediksi%20paket%20seluler%20pengguna%20menggunakan%20machine%20learning.ipynb) | Membuat model prediksi klasifikasi untuk menentukan paket seluler yang cocok untuk pelanggan menggunakan library dari *`scikit-learn`*. | *pandas*, *sklearn* |