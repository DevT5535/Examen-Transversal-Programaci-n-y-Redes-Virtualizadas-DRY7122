# app_web_hash.py
from flask import Flask, request, render_template_string
import sqlite3
import hashlib
import os

# Crear base de datos si no existe
db_name = "usuarios.db"

def crear_base_datos():
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    # Eliminar la tabla si existe
    cursor.execute('DROP TABLE IF EXISTS usuarios')
    
    # Crear la tabla con la estructura correcta
    cursor.execute('''
        CREATE TABLE usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            password_hash TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def agregar_usuario(nombre, password):
    hash_pw = hashlib.sha256(password.encode()).hexdigest()
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (nombre, password_hash) VALUES (?, ?)", (nombre, hash_pw))
    conn.commit()
    conn.close()

def validar_usuario(nombre, password):
    hash_pw = hashlib.sha256(password.encode()).hexdigest()
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE nombre = ? AND password_hash = ?", (nombre, hash_pw))
    result = cursor.fetchone()
    conn.close()
    return result is not None

# Crear DB si no existe
crear_base_datos()

# Agregar usuarios del examen (una sola vez)
if not os.path.exists("usuarios_inicializados.txt"):
    integrantes = {
        "Camilo": "clave123",
        "Pedro": "clave456",
        "Juan": "clave789"
    }
    for nombre, clave in integrantes.items():
        agregar_usuario(nombre, clave)
    open("usuarios_inicializados.txt", "w").close()

# Crear app Flask
app = Flask(__name__)

# HTML simple embebido
html = '''
<!doctype html>
<title>Login DRY7122</title>
<h2>Validación de Usuario - Examen Transversal</h2>
<form method=post>
  Nombre: <input type=text name=nombre><br><br>
  Contraseña: <input type=password name=clave><br><br>
  <input type=submit value=Validar>
</form>
<p>{{ mensaje }}</p>
'''

@app.route('/', methods=['GET', 'POST'])
def login():
    mensaje = ""
    if request.method == 'POST':
        nombre = request.form['nombre']
        clave = request.form['clave']
        if validar_usuario(nombre, clave):
            mensaje = "✅ Usuario válido."
        else:
            mensaje = "❌ Usuario o contraseña incorrecta."
    return render_template_string(html, mensaje=mensaje)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5800)