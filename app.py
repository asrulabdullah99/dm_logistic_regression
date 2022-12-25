import pickle
from flask import Flask, request, render_template

app = Flask(__name__)

model_file = open('logistic_model.pkl', 'rb')
model = pickle.load(model_file)


@app.route('/')
def index():
    return render_template('index.html', output='belum diprediksi')


@app.route('/predict', methods=['POST'])
def predict():
    usia, jeniskelamin, tekanandarah, kolesterol, guladarah, detakjantung = [
        x for x in request.form.values()]
    data = []

    data.append(int(usia))
    if jeniskelamin == 'Laki-Laki':
        data.extend([1])
    else:
        data.extend([0])
    data.append(int(tekanandarah))
    data.append(int(kolesterol))
    data.append(int(guladarah))
    data.append(int(detakjantung))

    prediction = model.predict([data])
    output = (prediction[0])
    if output == 1.0:
        hasil = "Anda beresiko penyakit jantung"
    else:
        hasil = "Anda tidak beresiko penyakit jantung"

    return render_template('index.html', output=hasil, usia=usia, jeniskelamin=jeniskelamin, tekanandarah=tekanandarah, kolesterol=kolesterol, guladarah=guladarah, detakjantung=detakjantung)

    if __name__ == '__main__':
        app.run(debug=True)
