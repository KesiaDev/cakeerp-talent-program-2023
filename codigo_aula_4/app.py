from flask import Flask, jsonify, request

app = Flask(__name__)

courses = [
    {
        'id': 1,
        'title': 'Curso de Python',
        'description': 'Aprenda programação em Python',
        'carga_horaria': 40,
        'qtd_exercicios': 10
    },
    {
        'id': 2,
        'title': 'Curso de Web Development',
        'description': 'Aprenda a criar sites e aplicações web',
        'carga_horaria': 60,
        'qtd_exercicios': 15
    }
]

@app.route('/courses', methods=['GET'])
def get_all_courses():
    return jsonify(courses)

# Resto do seu código aqui...

if __name__ == '__main__':
    app.run(debug=True)
