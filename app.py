from flask import Flask, jsonify
import json

app = Flask(__name__)

# Cargar datos desde el archivo externo API.json
with open("API.json", "r", encoding="utf-8") as json_api:
    datos_api_json = json.load(json_api)

# Endpoint HTML
@app.route('/')
def inicio():
    print("Cambio")

    return jsonify(datos_api_json["3D:RF:09:7F::014"])

@app.route('/json/<mac>')
def json_data(mac):
    print(datos_api_json[mac]["Name"])
    print(datos_api_json[mac]["Protocolos"])
    print(datos_api_json[mac]["VLANs"])
    print(datos_api_json[mac]["Status"])
    
    return jsonify(datos_api_json[mac])

if __name__ == '__main__':
    app.run(debug=True)