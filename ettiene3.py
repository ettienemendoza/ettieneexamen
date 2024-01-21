from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/ettiene1', methods=['GET', 'POST'])
def pagina():
    if request.method == 'POST':

        porcentaje = 0
        total = 0
        
        nombres = str(request.form['nombres'])
        edades = int(request.form['edades'])
        tarros = int(request.form['tarros'])
        calculo = tarros * 9000

        if edades >= 18 and edades <= 30:
            porcentaje = calculo * 0.15
            total = calculo - porcentaje
        elif edades >30:
            porcentaje = calculo * 0.25
            total = calculo - porcentaje
        return render_template('ettiene1.html', calculo=calculo, total=total, porcentaje=porcentaje, nombres=nombres, edades=edades, tarros=tarros)
    return render_template('ettiene1.html')


@app.route('/ettiene2', methods=['GET', 'POST'])
def usuarios():
    if request.method == 'POST':
        usuario = str(request.form['usuario'])
        password = str(request.form['password'])
        usuario1 = 'juan'
        usuario2 = 'pepe'
        password1 = 'admin'
        password2 = 'user'
        mensaje = ''
        if usuario == usuario1 and password == password1:
            mensaje = 'bienvenido administrador juan'
        elif usuario == usuario2 and password == password2:
            mensaje = 'bienvenido usuario pepe'
        else:
            mensaje = ' usuario o contraseña incorrectos'
        return render_template('ettiene2.html',usuario=usuario, password=password, mensaje=mensaje)
    return render_template('ettiene2.html')

if __name__ == '__main__':
    app.run(debug=True)





