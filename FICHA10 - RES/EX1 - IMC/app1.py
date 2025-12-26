"""
Flask para criar as rotas e renderizar as páginas HTML
Python linguagem de programação: lógica de negócio, cálculos
"""
from flask import Flask, render_template, request

# Object app
app = Flask(__name__)



"""
Rota para a página Index
"""
@app.route("/", methods=["GET", "POST"])
def index():
    # INCLUIR CODIGO AQUI
    return render_template("index.html")




# Flask Constructor
if __name__ == "__main__":
    app.run(debug=True)
