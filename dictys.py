from bottle import default_app, route, post, request, redirect, static_file
import os

template = """<html>
<head><title>Home</title></head>
<body>
<h1>Upload a file</h1>
<form method='post' action='/upload' enctype='multipart/form-data'>
    <input type='file' name='data'>
    <input type='submit' value='Submit'>
</form>
</body>
</html>"""


path = os.path.abspath(__file__)
dir_path = os.path.dirname(path)

@route('/')
def home():
    file_list = os.listdir('uploads')
    file_html = '<html><head></head><body><ul>'
    file_html += " ".join(['<li><a href="%s">%s</a></li>' % (f, f) for f in file_list])
    file_html += '</ul></body></html>'
    return file_html

@route('/<filename:path>')
def send_static(filename):
    return static_file(filename, root='uploads/', download=filename)


@post('/upload')
def upload():
    data = request.files.get('data')
    save_path = os.path.join('uploads/',data.filename)
    data.save(save_path)
    return redirect('/')

application = default_app()
