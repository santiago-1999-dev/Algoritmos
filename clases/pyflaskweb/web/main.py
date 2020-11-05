from flask import Flask, request, make_response, redirect, render_template, url_for

#se crea un objeto de tipo app
app = Flask (__name__)

@app.errorhandler(404)
def not_found(error):
    return render_template("404.html")

@app.route('/')
def baseRoute():
    return redirect(url_for('login'))

@app.route('/home')
def home():
   return render_template('home.html')

@app.route('/login', methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        nameUser = request.form['name']
        passUser = request.form ['pass']
        if (passUser == 'hola1234'):
            return  redirect(url_for('home'))
        else:
            return 'Falló proceso de autenticación'
    else: 
        return render_template('login.html')

@app.route("/lugares")
def casasRoute():
    return render_template ("lugares.html")

@app.route("/personajes")
def carroRoute():
    return render_template ("personajes.html")

if __name__== '__main__':
    app.run()