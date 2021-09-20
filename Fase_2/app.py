from flask import Flask, jsonify, request
# from flask_cors import  CORS
import json

app = Flask(__name__)

@app.route('/carga', methods=['POST'])
def cargaMasiva():
    tipo = request.json['tipo']
    path = request.json['path']
    if tipo == "estudiante":
        return jsonify({'Tipo': tipo})
    elif tipo == "recordatorio":
        return jsonify({'Tipo': tipo})
    elif  tipo == "curso":
        return jsonify({'Tipo': tipo})
    else:
        return jsonify({'Error': 'Tipo invalido'})

if __name__ == '__main__':
    app.run(debug=True, port=3000)