from flask import Flask, jsonify
from database import db
from models import User  # Se você tiver mais modelos, importe-os aqui

app = Flask(_name_)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'  # Banco de dados SQLite para simplicidade
db.init_app(app)

@app.route('/status')
def status():
    return jsonify({'status': "it's alive"})

if _name_ == '_main_':
    app.run(debug=True)