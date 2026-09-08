from flask import Flask, render_template,   request   , redirect, url_for #Herramientas importadas
import os, json, csv #Son los módulos de python / os se utiliza para trabajar con archivos y rutas

app = Flask(__name__) # Crea la aplicación web
HISTORIAL = os.path.join(os.path.dirname(__file__), 'historial.json') # Se le indica al programa donde guardar el historial

def get_historial():
    return json.load(open(HISTORIAL, 'r', encoding='utf-8')) if os.path.exists(HISTORIAL) else [] # obtiene el historial

@app.route('/')
def index():
    return render_template('index.html', historial=get_historial()) # Nos muestra el index.html y nos envia el historial

@app.route('/procesar', methods=['POST']) # Recibe información enviada mediante POST
def procesar():
    file = request.files.get('archivo') # Busca el archivo que es enviado
    if not file or not file.filename: return redirect(url_for('index'))

    ext = file.filename.split('.')[-1].lower() # Obtiene la extensión
    texto = file.read().decode('utf-8', errors='ignore') # Ignora errores existentes en la lectura de un archivo

    if ext == 'txt':
        cat, det = "Análisis de Documento", f"{len(texto.splitlines())} líneas, {len(texto.split())} palabras"
    elif ext == 'csv':
        filas = list(csv.reader(texto.splitlines()))
        cat, det = "Estadísticas de Datos", f"{max(0, len(filas)-1)} registros, {len(filas[0]) if filas else 0} columnas" # Encabezados en primera fila
    elif ext == 'json':
        datos = json.loads(texto) if texto else [] # Convierte el texto JSON en una estructura de Python
        cat, det = "Procesamiento JSON", f"{len(datos) if isinstance(datos, (list, dict)) else 1} elementos" # Calcula cuántos elementos contiene
    else:
        return redirect(url_for('index')) # Regresa a la pagina principal / url_for Sirve para generar la dirección de una ruta de Flask.

    historial = get_historial()
    historial.insert(0,{
        "nombre": file.filename, 
        "tipo": ext.upper(), 
        "categoria": cat, 
        "detalle": det})
    json.dump(
        historial, 
        open(HISTORIAL, 'w', encoding='utf-8'), 
        indent=2, # Ordena y facilita la lectura
        ensure_ascii=False # conserva caracteres
        )
    return redirect(url_for('index'))
