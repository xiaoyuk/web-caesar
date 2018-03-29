from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
                }}
        </style>
    </head>
    <body>
      <form action="/" method  ="post">
        <label for ="Rotate-by"> Rotate by: </label>
        <input id="Rotate-by" type ="text" name ="rot" value="0" />
        <br>
        <textarea name="text" />{0}</textarea>
        </br>
        <br>
        <input type = "submit" />
        </br>
      </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format(...)

@app.route("/", methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    text = str(request.form['text'])
    rotate_string_1 = rotate_string(text, rot)
    return form.format(rotate_string_1)

app.run()