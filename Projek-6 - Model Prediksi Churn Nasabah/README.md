### Model Prediksi Churn Nasabah Bank Menggunakan Machine Learning: Studi Kasus pada Data Bank Syariah

Sebuah `Bank Syariah` yang menerapkan akad syariah `agama islam` dalam proses bisnisnya dimana hanya menyediakan layanan jual beli, bukan akad peminjaman uang dengan riba terhadap pihak pertama (`developer/penjual`), kedua(`bank`) dan ketiga(`nasabah`). Nasabah yang menginginkan sesuatu namun terkendala biaya bisa menggunakan fasilitas ini, dimana barang dibeli oleh bank kemudian dijual kembali dengan margin yang lebih tinggi kepada nasabah dengan pembayaran cicil selama jangka waktu tertentu. 

Nasabah `Bank Syariah` pergi meninggalkan perusahaan: sedikit demi sedikit, jumlah mereka berkurang setiap bulannya. Para pegawai bank menyadari bahwa akan lebih menghemat biaya jika perusahaan fokus untuk mempertahankan nasabah lama mereka yang setia daripada menarik nasabah baru.
Pada kasus ini, tugas kita adalah untuk memprediksi apakah seorang nasabah akan segera meninggalkan bank atau tidak. Kita memiliki data terkait perilaku para klien di masa lalu dan riwayat pemutusan kontrak mereka dengan bank. Target dinyatakan dengan `Kelas 0` bahwa nasabah tidak segera pergi dan `Kelas 1` bahwa nasabah akan segera pergi.

Berdasarkan penjelasan diatas, `model machine learning` yang dipilih adalah jenis `klasifikasi - supervised learning`. Kita akan mencari F1 Skor semaksimal mungkin dan melihat metrik AUC-ROC. Ambang batas (threshold) F1 yang ditetapkan untuk projek ini sebesar 0.59.

Beberapa tujuan dan rumusan masalah dari analisis projek ini:
- Mengetahui algoritma terbaik untuk `model machine learning` untuk dataset `Bank Syariah`
- `Hyperparameter` terbaik seperti apa pada `model machine learning`
- Apakah ketidak seimbangan (`imbalance`) kelas mempengaruhi metrik kualitas `model machine learning`?
- Benarkah model yang sudah dilatih menggunakan kelas data yang seimbang (`balance`) menghasilkan metrik kualitas F1 yang lebih baik?