#uno de los mejores lenguajes para servidores web,python en desarrollo web,backend, como plataforma de todas las aplicaciones
#que se conectan a interner como google
# MI FIRST SERVER IN PYTHON :0 :0 :0 :0
from flask import Flask, make_response
from flask import render_template, request, redirect, url_for, flash,session,abort
from contact_models import Contact



app = Flask(__name__, template_folder='templates', static_folder='static') #instacion de flask, parametro del modulo


@app.route(r'/', methods=['GET']) #generar una ruta, en que url se va ejecutar una función
def users():
    #objeto = Contact()
    #contactos = objeto.Get()
    return render_template('users.html')
    

@app.route(r'/add', methods=['GET','POST'])
def add_user():
    if request.form:
        name = request.form.get('name')
        lastname = request.form.get('lastname')
        phone = request.form.get('phone_number')
        email = request.form.get('email')
        password = request.form.get('password')
        user = request.form.get('Tipo')
        objeto = Contact()
        if user == "generador":
            objeto.GuardarGenerador(name,lastname,phone,email,password)
        else:
            objeto.GuardarRecolector(name,lastname,phone,email,password)



    return render_template('add_user.html')

if __name__ == '__main__':
    app.run()
