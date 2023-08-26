### Model Prediksi Seri Waktu untuk Mengetahui Jumlah Pesanan Perusahaan Taksi

Sebuah perusahaan taksi bernama `Sweet Lift` telah mengumpulkan data historis (`time series`) tentang pesanan taksi di bandara. Untuk menarik lebih banyak pengemudi pada jam sibuk, perlu memprediksi jumlah pesanan taksi untuk `satu jam` berikutnya. Perusahaan hanya mempunyai data historis dari bulan `maret` hingga bulan `agustus` tahun 2018. Kita akan membuat beberapa model `machine learning` untuk memprediksi jumlah pesanan beserta pengujian model-model tersebut, dimana `metrik RMSE` pada *test set* `tidak boleh lebih dari 48`. Berikut ini beberapa langkah untuk menyelesaikan masalah pada projek ini:
1. Melakukan *resampling* data dalam satu jam.
2. Menganalisis dataset untuk mendapatkan `insights` berupa fitur-fitur `time series` seperti analisis `tren`, `seasonality` dan `residu`.
3.  Melatih `model` yang `berbeda` dengan `hiperparameter` yang `berbeda`. Disini kita akan menentukan bahwa sampel `test` sebesar `10%` dari dataset.
4. Menguji `metrik RMSE` pada `semua model` menggunakan data `test`.
5. Membuat prediksi untuk bulan `september` tahun 2018 menggunakan `best model`.

| Projek | Deskripsi | Modul |
| ------- | ------- | ------- |
| [Model Prediksi Seri Waktu pada Perusahaan Taksi]() | Perbandingan `Model Machine Learning` untuk Memprediksi `Jumlah Pesanan` pada Perusahaan Taksi Menggunakan `Dataset Seri waktu` untuk Mendapatkan Skor `RMSE` yang `Tidak Lebih Besar dari 48` | *pandas*, *numpy*, *sklearn*, *matplotlib*, *seaborn*, *XGBoost*, *time*, *LightGBM*, *statsmodels* |