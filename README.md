## Testing Aplikasi di Lokal komputer anda. 
1. Pastikan Anda sudah menginstall Anaconda
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
    
