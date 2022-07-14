from flask import Flask, render_template, abort
import os

app = Flask(__name__)

@app.route("/")
def index():
    return "Flask + Docker demo!"


#if file exists, return the appropriate handler

@app.route('/<name>')
def hello(name):
    #return a simple template
    try:
        return render_template(name)
    except:
        #abort(404)
        #error_404(404)
        #endsHTML = name.endswith(".html")
        #endsCSS = name.endswith(".css")
        if "~" in name or "//" in name or ".." in name:
            abort(403)
            #403 forbidden
            #error_403(403)
        #elif endsHTML or endsCSS:
        #else:
            abort(404)
            #error_404(404)
            #isFile = os.path.isfile("./templates/" + name)
            #if isFile is False:
                #404 not found
                #error_404(404)


#else, return appropriate error using error handler

@app.errorhandler(404)
def error_404(e):
    #if "~" in name or "//" in name or ".." in name:
        #403 forbidden
        #error_403(e)
        #abort(403)
    return render_template("404.html"), 404

@app.errorhandler(403)
def error_403(e):
    return render_template("403.html"), 403



if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
