from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def calcular_meta():
    if request.method == 'POST':
        try:
            objetivo = float(request.form['objetivo'])
            poupanca_mensal = float(request.form['poupanca_mensal'])
            tempo = objetivo / poupanca_mensal
            anos = int(tempo/12)
            meses = int(tempo%12)  
            return render_template('index.html', tempo=tempo, meses=meses,anos=anos, mostrar_resultado=True)

        except ValueError:
            erro = "Certifique-se de inserir números válidos"
            return render_template('index.html', erro=erro)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
