from flask import Flask
from flask import render_template



app = Flask(__name__,static_folder="static")

@app.route("/")
def index():
  return render_template("index.html")

# Ruta para la página "Nosotros"
@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')

@app.route('/productos')
def mostrar_productos():
    return render_template('productos.html')


if __name__ == "__main__":
  app.run(debug=True)