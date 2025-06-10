from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory 'database'
courses = {}
subjects = {}
professors = {}
schedules = []

@app.route('/courses', methods=['GET', 'POST'])
def handle_courses():
    if request.method == 'POST':
        data = request.json
        cid = data.get('id')
        courses[cid] = data
        return jsonify({'message': 'Course created', 'course': data}), 201
    return jsonify(list(courses.values()))

@app.route('/subjects', methods=['POST'])
def add_subject():
    data = request.json
    sid = data.get('id')
    subjects[sid] = data
    return jsonify({'message': 'Subject created', 'subject': data}), 201

@app.route('/professors', methods=['POST'])
def add_professor():
    data = request.json
    pid = data.get('id')
    professors[pid] = data
    return jsonify({'message': 'Professor added', 'professor': data}), 201

@app.route('/schedule', methods=['POST'])
def add_schedule():
    data = request.json
    schedules.append(data)
    return jsonify({'message': 'Schedule added', 'schedule': data}), 201

if __name__ == '__main__':
    app.run(debug=True)
