### Model Prediksi Lokasi Eksplorasi Sumur OilyGiant

Sebuah perusahaan bernama `OilyGiant` ingin melakukan eksplorasi minyak untuk tiga wilayah. Kita diminta untuk menentukan lokasi mana yang cocok untuk dilakukan eksplorasi dengan memperhatikan aspek bisnis mereka agar tidak mengalami/mengurangi potensi kerugian dengan ambang batas risiko dibawah `2.5%` serta memperoleh laba yang tinggi. `OilyGiant` memiliki modal sebsar `100 Juta USD` dengan harga `per barel` minyak sebesar `4.5 USD`. 

Dataset yang berasal dari `OilyGiant` memiliki beberapa variabel yang mempengaruhi `kandungan minyak`. Kita akan membuat `model machine learning` yang mampu memprediksi lokasi dengan `kandungan minyak` paling tinggi. Kemudian dilanjutkan dengan analisis `keuntungan/margin profit` dan analisis `risiko` dengan teknik `bootstrapping`. Beberapa tujuan dan rumusan masalah untuk projek ini diantaranya: 
1. Kriteria seperti apa agar perusahaan `OilyGiant` tidak mengalami kerugian?
2. Bagaimana performa `model machine learning` terhadap dataset?
3. Wilayah mana yang cocok dijadikan lokasi `200 titik` explorasi sumur?
4. Seberapa besar rata-rata `profit margin` untuk lokasi yang terpilih menggunakan teknik `bootstrapping`?
5. Berapa `selang kepercercayaan` untuk lokasi tersebut dengan `tingkat keyakinan 95%`?

| Projek | Deskripsi | Modul |
| ------- | ------- | ------- |
| [Model Prediksi Lokasi Eksplorasi Sumur OilyGiant](https://github.com/fuadraharjo/TripleTen_IND/blob/main/Projek-7%20-%20Model%20Prediksi%20Lokasi%20Sumur%20Eksplorasi/Model%20prediksi%20lokasi%20eksplorasi%20sumur%20OilyGiant%20menggunakan%20bootstrap%20dan%20machine%20learning.ipynb) | Analisis bisnis untuk mengurangi risiko kerugian dalam pencarian lokasi sumur eksplorasi menggunakan `machine learning` dan teknik `bootstrapping`. | *pandas*, *numpy*, *sklearn*, *matplotlib*, *seaborn* |