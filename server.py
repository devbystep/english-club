
from bottle import route, run, template
from bottle import static_file

@route('/')
def index():
    return static_file('index.html', root="public")

@route("/public/<filename>")
def static(filename):
    return static_file(filename, root="public")
run(host='localhost', port=8001)
