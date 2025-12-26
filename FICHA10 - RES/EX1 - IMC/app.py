"""
Flask para criar as rotas e renderizar as páginas HTML
Python linguagem de programação: lógica de negócio, cálculos
"""
from flask import Flask, render_template, request

# Object app
app = Flask(__name__)




def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"


"""
Rota para a página Index
"""
@app.route("/", methods=["GET", "POST"])
def index():
    urlImage = './static/images/IMCImage.jpg'
    imc = 0
    classificacao = ""

    if request.method == "POST":
        peso = float(request.form.get("peso"))
        altura = float(request.form.get("altura"))
        imc = float(calcular_imc(peso, altura)).__round__(2)
        classificacao = classificar_imc(imc)

    return render_template("index1.html", urlImage= urlImage, imc=imc, 
                                        classificacao=classificacao)




# Flask Constructor
if __name__ == "__main__":
    app.run(debug=True)
