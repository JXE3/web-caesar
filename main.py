from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['Debug'] = True

form = """
<!DOCTYPE html5>

<html>
    <head>
        <style>
            form {{
                background-color:#eee;
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
        <form action="/encrypt", method="POST">
            <label for="rot">Rotate by:</label>
            <input type="text" name="rot" value="0">
            
            <textarea name="text">{0}</textarea>    
            
            <input type="submit" value="Submit">
        </form>
            
         
    </body>
</html>
"""

@app.route("/")
def index():
 
     return form.format('')

@app.route("/encrypt", methods=['POST'])
def encrypt():
    
    rotateInput = int(request.form['rot'])
    textInput = request.form['text']

    encryptedMessage = rotate_string(textInput, rotateInput)

    return form.format(encryptedMessage)


app.run()