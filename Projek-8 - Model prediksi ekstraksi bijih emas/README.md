### Model Prediksi Ekstraksi Bijih Emas di Perusahaan Tambang

Sebuah perusahaan tambang emas membutuhkan sebuah `model machine learning` untuk meprediksi hasil ekstraksi bijih emas yang berasal dari tambang. Perushaan ini memberikan kita dataset mentah yaitu dataset `train`, `test` dan `full`. Proses ekstraksi dan pemurnian `emas - Au` dari bijih emas melalui beberapa tahapan `proses teknologi` yaitu proses `flotasi`, `pemurnian tahap primer` dan `pemurnian tahap sekunder`. Disetiap proses `stage` akan menghasilkan konsentrat `emas - Au`, beberapa konsentrat lain dan beberapa `residu`.

Model `machine learning` diharapkan bisa menyingkirkan parameter-parameter lain yang tidak menghasilkan keuntungan dan berfokus pada parameter-parameter yang menghasilkan keuntungan. Untuk mengetahui `model machine learning` memiliki kualitas yang baik diperlukan pengunjian dengan teknik `cross-validation` dan menghitung nilai SMAPE `(Symmetry Mean Absolute Percentage Error)`.

Beberapa tujuan dan rumusan masalah untuk projek ini diantaranya:
- Bagaimana distribusi konsentrat logam `Au`, `Ag` dan `Pb` disetiap proses teknologi (`stage`)-nya?
- Mengetahui distribusi ukuran partikel umpan (`umpan`) untuk dataset `train` dan `test`.
- Mengetahui distribusi konsentrat ditiap proses teknologi (`stage`) untuk dataset `train` dan `test`.
- Seberapa banyak fitur/parameter yang bisa direduksi?
- Diantara jenis `model machine learing` berikut: `regresi linier`, `random forest` dan `K-Nearest neighbors`. Manakah yang memberikan hasil terbaik menggunakan teknik skor `cross-validation SMAPE`?
- Berapakah skor `SMAPE` yang dihasilkan oleh `model terbaik` pada dataset `test`?