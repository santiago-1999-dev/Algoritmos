from flask import Flask, request, make_response, redirect, render_template, url_for
import utilidades as helper 

#se crea un objeto de tipo app
app = Flask (__name__)
fileNameCredential = "usuarios.csv"
data= helper.leerArchivo("usuarios.csv")

@app.errorhandler(404)
def not_found(error):
    return render_template("404.html")

@app.route('/')
def baseRoute():
    return redirect(url_for('login'))

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/signin', methods = ['POST','GET'])
def signin():

    if request.method == 'POST':
        helper.saveUser (data,fileNameCredential,request.form['name'],request.form ['pass'] )
        return redirect(url_for('success'))
    else: 
        return render_template('signIn.html')


@app.route('/login', methods = ['POST','GET'])
def login():
    data = helper.leerArchivo(fileNameCredential)
    if request.method == 'POST':
        nameUser = request.form['name']
        passUser = request.form ['pass']
        output = helper.validatepassword (data, nameUser, passUser)
        print (output, data, nameUser, passUser)
        if (output == True):
            return  redirect(url_for('home'))
        else:
            return  redirect(url_for('signin'))
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