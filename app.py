from flask import Flask, request, render_template
import math

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    if request.method == 'POST':
        try:
            objetivo = float(request.form['objetivo'])
            poupanca_mensal = float(request.form['poupanca_mensal'])
            
            tempo = math.ceil(objetivo / poupanca_mensal)
            
            return render_template('resultado.html', tempo=tempo)
        except Exception as e:
            return render_template('erro.html', erro=str(e))

if __name__ == '__main__':
    app.run(debug=True)
