### Model Prediksi Sentimen pada Ulasan Film Menggunakan Natural Language Processing

Sebuah perusahaan hiburan ingin membuat sebuah model `machine learning` untuk menyaring ulasan-ulasan sebuah `film` serta mengkategorikanya. Ulasan-ulasan tersebut harus bisa dikenali apakah berupa `ulasan positf` atau `ulasan negatif`. Kita akan menggunakan `dataset` ulasan dari `IMBD` dengan `pelabelan polaritas` untuk membuat sebuah model yang bisa mengklasifikasikan `ulasan positif` dan `negatif`. Model ini setidaknya harus memiliki skor `F1` sebesar` 0,85`. Dataset akan kita lakukan eksplorasi menggunakan `analisis data eksploratif (EDA)` untuk mendapatkan `insights` di dalamnya serta memastikan agar `dataset` bisa melatih model dengan baik. Beberapa `model` dengan `konfigurasi`-nya yang akan kita latih dan uji diantaranya:
- Model 0 - Konstan (*Dummy Classifier*)
- Model 1 - NLTK, TF-IDF dan *Logistic Regression*
- Model 2 - spaCy, TF-IDF dan *Logistic Regression*
- Model 3 - spaCy, TF-IDF dan LGBMClassifier
- Model 4 - BERT (*Bidirectional Encoder Representations from Transformers*) dan *Logistic Regression*

| Projek | Deskripsi | Modul |
| ------- | ------- | ------- |
| [Model Prediksi Sentimen Menggunakan NLP](https://github.com/fuadraharjo/TripleTen_IND/blob/main/Projek-12%20-%20Model%20Prediksi%20Sentimen%20pada%20Ulasan%20Film%20Menggunakan%20NLP/Model%20prediksi%20sentimen%20pada%20ulasan%20film%20menggunakan%20natural%20language%20processing.ipynb) | Model prediksi sentimen menggunakan *natural language processing* pada model-model `machine learning`. Tokenisasi dan lematisasi dilakukan menggunakan modul *spaCy*, *nltk*, dan *BERT*. Beberapa `model` yang diujikan `dummy classifier`, `logistic regression` dan `lightGBM`. | *pandas*, *numpy*, *sklearn*, *matplotlib*, *seaborn*, *math*, *re*, *tqdm*, *nltk*, *spaCy*, *LightGBM*, *torch*, *transformers* |