from flask import Flask,render_template, redirect, url_for,request, jsonify, abort

app = Flask(__name__)

students = [
    {
        'id': 1,
        'name': 'Darren',
        'physics': 80,
        'maths': 60,
        'chemistry': 45
    },
    {
        'id': 2,
        'name': 'Jerry',
        'physics': 50, 
        'maths': 45,
        'chemistry': 45
    }
]

#curl -i -H "Content-Type: application/json" -X POST -d '{\"name\":\"Sivu\",\"physics\":30,\"maths\":90,\"chemistry\":10}' http://127.0.0.1:5000/result
#curl -i -H "Content-Type: application/json" -X POST -d "{\"name\":\"Sivu\"}" http://127.0.0.1:5000/result
@app.route('/', methods=['GET'])
def student():
   return jsonify({'student':students})


@app.route('/results/<int:indexId>',methods=["GET"])
def get_id(indexId):
   studentId = [student for student in students if student['id'] == indexId]
   if len(studentId) == 0:
      abort(404)
   return jsonify({'Student':studentId[0]})

@app.route('/result',methods=['POST'])
def add_results() : 
   if not request.json or not 'name' in request.json:    
      abort(400)

   student = {
         'id': students[-1]['id'] + 1,
         'name': request.json['name'],
         'physics': request.json.get('physics',""),
         'maths': request.json.get('maths',""),
         'chemistry': request.json.get('chemistry',"")
      }
  
   students.append(student)
   return jsonify({'students':student}), 201

if __name__ == '__main__':
 app.run(debug=True)
