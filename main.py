from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route('/') # Pagina principal
def home():
    return render_template('index.html')

@app.route('/controles') # Ruta : /controles
def controles():
    return render_template('controles.html')

if __name__ == '__main__':
    app.run(debug=True)