from flask import Flask
from flask import render_template

import pandas as pd
from matplotlib import pyplot as Mplt
import seaborn as sb

Dados = pd.read_excel('C:/aula8/PesquisaAuto.xlsx', 'Pesquisa')



Mplt.hist(Dados["Imagem"], bins=5)
Mplt.savefig("static\Grafico2.JPG")

sb.jointplot(x="Preco", y="Imagem",  data=Dados)
Mplt.savefig('static\Grafico.JPG')




App = Flask(__name__, template_folder='./')

@App.route("/", methods=["GET"])
@App.route("/dispersao", methods=["GET"])
def Home():
    return render_template ("dispersao.html")

@App.route("/histograma", methods=["GET"])
def Contato():
    return render_template ("histograma.html")



if __name__ == "__main__":
    App.run(port=80)
