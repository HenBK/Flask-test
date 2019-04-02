from flask import Flask, render_template, url_for   #importando el objeto Flask , la funcion render_template y url_for

app = Flask(__name__) # creando el webserver, __name__ hace referencia al archivo actual (__name__ = main.py)

@app.route("/")
def home ():
    return render_template("home.html")

@app.route("/about")
def about ():
    return render_template("about.html")

@app.route('/hello/<name>')
def hello(name):
    return render_template('page.html', name=name)

if __name__ == "__main__": #cuando se ejectuta el script python le asigna el nombre "__main__" al script 
    app.run(debug = True)  #por si se importa otro script, el if previene que otros scripts se ejecuten,
                           #cuando se ejecute el archivo main.py solo entonces su nombre sera cambiado a __main__
                           #y solo entonces se ejecutara el if (linea 15) 
