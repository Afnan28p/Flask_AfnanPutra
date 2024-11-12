from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hello/<user>')
def hello_name(user):
    return render_template('index.html', nama_user = user)

@app.route('/fakultas')
def fakultas():
    fakultas = ["FIKR", "FEB"]
    return render_template('fakultas.html', dataFakultas = fakultas)

@app.route('/prodi')
def prodi():
    prodi = [
        {"nama" : "informatika",
        "fakultas" : "FIKR"},
        {"nama" : "sistem informasi",
        "fakultas" : "FIKR"},
        {"nama" : "elektro",
        "fakultas" : "FEB"},
        {"nama" : "elektronika",
        "fakultas" : "FEB"}
    ]
    return render_template('prodi.html',dataProdi = prodi)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)