from flask import Flask, render_template, request, redirect, url_for
import os, json, csv

app = Flask(__name__)
HISTORIAL = os.path.join(os.path.dirname(__file__), 'historial.json')

def get_historial():
    return json.load(open(HISTORIAL, 'r', encoding='utf-8')) if os.path.exists(HISTORIAL) else []

@app.route('/')
def index():
    return render_template('index.html', historial=get_historial())

@app.route('/procesar', methods=['POST'])
def procesar():
    file = request.files.get('archivo')
    if not file or not file.filename: return redirect(url_for('index'))

    ext = file.filename.split('.')[-1].lower()
    texto = file.read().decode('utf-8', errors='ignore')

    if ext == 'txt':
        cat, det = "Análisis de Documento", f"{len(texto.splitlines())} líneas, {len(texto.split())} palabras"
    elif ext == 'csv':
        filas = list(csv.reader(texto.splitlines()))
        cat, det = "Estadísticas de Datos", f"{max(0, len(filas)-1)} registros, {len(filas[0]) if filas else 0} columnas"
    elif ext == 'json':
        datos = json.loads(texto) if texto else []
        cat, det = "Procesamiento JSON", f"{len(datos) if isinstance(datos, (list, dict)) else 1} elementos"
    else:
        return redirect(url_for('index'))

    historial = get_historial()
    historial.insert(0, {"nombre": file.filename, "tipo": ext.upper(), "categoria": cat, "detalle": det})
    json.dump(historial, open(HISTORIAL, 'w', encoding='utf-8'), indent=2, ensure_ascii=False)

    return redirect(url_for('index'))