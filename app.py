from flask import Flask, request, render_template
import pickle
import pandas as pd  # Pastikan Anda mengimpor pandas

# Import fungsi label_encode_columns dari file yang sesuai
from utils import label_encode_columns, columns_to_encode  # tambahkan import columns_to_encode

app = Flask(__name__)

model_file = open('modeldtc.sav', 'rb')
model = pickle.load(model_file)

# Fungsi label_encode_columns yang telah Anda definisikan sebelumnya

@app.route('/')
def index():
    return render_template('index.html', insurance_cost=" ")

@app.route('/predict', methods=['POST'])
def predict():
    PSTV02, PSTV04, PSTV05, PSTV06, PSTV07, PSTV08, PSTV09, PSTV10, PSTV11, PSTV12, PSTV13, PSTV14, PSTV15, PSTV16 = [x for x in request.form.values()]

    # Membuat list data dari input form
    data = [int(PSTV02), PSTV04, PSTV05, PSTV06, PSTV07, PSTV08, PSTV09, PSTV10, PSTV11, PSTV12, PSTV13, PSTV14, float(PSTV15), int(PSTV16)]

    # Membuat dataframe dari list data
    new_data = pd.DataFrame([data], columns=columns_to_encode)

    # Melakukan label encoding pada new data menggunakan fungsi label_encode_columns
    new_data_encoded = label_encode_columns(new_data, columns_to_encode)

    # Melakukan prediksi menggunakan model
    prediction = model.predict(new_data_encoded)

    # Thresholding dengan nilai threshold 0.5
    output = (prediction > 0.5).astype(int)

    # Menyusun pesan berdasarkan output
    if output == 1:
        message = "Aktif"
    else:
        message = "Tidak Aktif"

    return render_template('index.html', insurance_cost=message)

if __name__ == '__main__':
    app.run(debug=True)
