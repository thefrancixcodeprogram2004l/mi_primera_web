from flask import Flask
from flask import render_template
app=Flask(__name__)

#creamos una ruta de acceso y renderizar el template para mostrar el resultado

@app.route('/')
def inicio():
    return render_template('sitio/index.html')

@app.route('/libros')
def libros():
    return render_template('sitio/libros.html')

@app.route('/nosotros')
def libros():
    return render_template('sitio/nosotros.html')

if __name__ =='__main__' :
    app.run(debug=True)