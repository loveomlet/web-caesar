from flask import Flask, request
import cgi
import caesar 

app = Flask(__name__)
app.config['DEBUG'] = True

form ="""
<!DOCTYPE html>

<html>
    <head>
        <style>
            form{{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px auto;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea{{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form action="/" method="post">
            <label>Rotate by:</label>
            <input name="rot" type="text" value="0" /><br>
            <textarea name="text">{rot_text}</textarea><br>
            <input type="submit" value="Submit query">
    </form>
    </body>
</html>
"""
@app.route("/", methods=['POST', 'GET'])
def encrypt():
    if request.method == 'GET':
        return form.format(rot_text='')

    rot = int(request.form.get('rot'))
    text = request.form.get('text')
    encrypted_text = caesar.encrypt(text, rot)
    
    return form.format(rot_text=encrypted_text)    

app.run()