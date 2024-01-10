## Introduction
Repository ini merupakan bahan latihan pengembangan model data mining yang menerapkan CRISP-DM.

[Dataset](https://drive.google.com/drive/folders/1HWmqPe8dwr1NVZhRbEtdYaPVnjJe0e3E?usp=sharing) merupakan Data Sampel dari BPJS Kesehatan pada kurun waktu 2015 hingga 2021.

![Buku Data Sampel Tahun 2022-2_page-0001](https://github.com/san-limbong/Klasifikasi-Status-Kepesertaan-Case-Data-Sample-BPJS-2015-2021/assets/81342084/52765587-5ab6-4988-bf1f-669edf148ba2)

Adapun sumber data yang digunakan berfokus terhadap data kepesertaan dengan struktur sebagai berikut.
![Annotation 2024-01-10 133656](https://github.com/san-limbong/Klasifikasi-Status-Kepesertaan-Case-Data-Sample-BPJS-2015-2021/assets/81342084/fa86b49b-6094-498f-9c71-424d3eb4f921)

Berikut atribut yang tersedia dari dataset yang digunakan.
![Buku Data Sampel Tahun 2022-57_page-0001](https://github.com/san-limbong/Klasifikasi-Status-Kepesertaan-Case-Data-Sample-BPJS-2015-2021/assets/81342084/44114c91-0c11-451d-8484-2306a55ade7f)


Tujuan dari pengembangan model adalah untuk melatih model yang dapat mengklasifikasikan status kepesertaan antara AKTIF dan TIDAK AKTIF.

Sebagai catatan anda juga dapat mengeksplorasi dengan menggunakan dataset dan e-book melalui link diatas untuk mengembangkan model anda.


## Coba Aplikasi di Komputer Anda. 
1. Pastikan Anda sudah menginstall Anaconda dan telah menyesuaikan PATH ENVIRONMENTnya
2. Buka terminal/command prompt/power shell
3. Cek Ketersediaan Environment
    conda info --envs
4. Jika tidak tersedia, nuat virtual environment dengan 
    conda create -n <nama-environment> python=3.9
4. Aktifkan virtual environment dengan 
    conda activate <nama-environment>
5. Install semua dependency/package Python dengan
    pip install flask gunicorn scikit-learn==1.2.2
6. Jalankan API menggunakan perintah
    python app.py
7. Akses web di localhost:5000
    
