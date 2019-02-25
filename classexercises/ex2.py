from flask import Flask, request, jsonify

app = Flask(__name__)

my_course = [
    {"id":1, "name":"Python"},
    {"id":2, 'name': "Flask"}
]


def post_course(id, name):
    my_course.append({"id": course_id, "name": })
    pass

def get_course(course_id):
 for course in my_course:
     if course["id"] == course_id:
         return jsonify(course)
    else:
        return jsonify({"course": None})


@app.route('/course/<int:id>', methods=['GET', 'POST'])
def course(id, name):
    if request.method == "POST":
        return post_course(id, name)
return get_course(id)