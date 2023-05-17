from flask import Flask, render_template
import urllib.request

app = Flask(__name__)

@app.route("/")
def home():
    pagina = urllib.request.urlopen('https://github.com/felipe-sant/devweb_desafio') 
    texto = pagina.read().decode('utf8')

    p1 = texto.find('<title>')

    p1_title_inicio = p1 + 28
    p1_title_final = p1_title_inicio + 14
    p1_title = texto[p1_title_inicio:p1_title_final]

    p1_desc_inicio = p1 + 44
    p1_desc_final = p1_desc_inicio + 44
    p1_desc = texto[p1_desc_inicio:p1_desc_final]

    return render_template("home.html", title = "Início", project_1 = p1_title, desc_p1 = p1_desc)

@app.route("/about/")
def about():
    return render_template("about.html", title = "Sobre")

@app.route("/contact/")
def contact():
    return render_template("contact.html", title = "Contato")
