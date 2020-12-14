#import net
from microdot import Microdot, Response
from html_tools import render_template_string, render_template

app = Microdot()

htmldoc = """<!DOCTYPE html>
<html>
    <head>
        <title>Microdot Example Page</title>
    </head>
    <body>
        <div>
            <h1>Microdot Example Page</h1>
            <p>Hello from {{ name }}!</p>
        </div>
    </body>
</html>
"""


@app.route("", methods=["GET", "POST"])
def index(request):
    print(request.headers)
    html = render_template_string(htmldoc, name='Microdot')
    return Response(body=html, headers={"Content-Type": "text/html"})


@app.route("/name/<name>", methods=["GET", "POST"])
def name(request, name):
    print(request.headers)
    html = render_template('templates/hello.html', name=name)
    return Response(body=html, headers={"Content-Type": "text/html"})



app.run(port=5000, debug=True)
