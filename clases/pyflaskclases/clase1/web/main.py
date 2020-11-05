from flask import Flask, request, make_response,redirect, render_template

#se crea un objeto de tipo app
app = Flask (__name__)

@app.route('/')
def homeRoute():
    user_ip = request.remote_addr
    response = make_response(redirect("hello"))
    response.set_cookie("ip",user_ip)
    response.set_cookie("gato","lior")
    return response

@app.route("/hello")
def helloRoute():
    gato = request.cookies.get("gato")
    ip = request.cookies.get("ip")
    return render_template ("hello.html", mascota = gato, userIp = ip )

@app.route("/carro")
def carroRoute():
    return render_template ("carro.html")
    


if __name__== '__main__':
    app.run()
