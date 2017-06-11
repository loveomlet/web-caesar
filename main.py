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
            form{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px auto;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form action="/" method="post">
            <label>Rotate by:</label>
            <input name="rot" type="text" value="0" /><br>
            <textarea name="text"></textarea><br>
            <input type="submit" value="Submit query">
    </form>
    </body>
</html>
"""
@app.route("/", methods=['POST'])
def encrypt():
    
    rot = int(request.form['rot'])
    text = request.form['text']
    encrypted_text = caesar.encrypt(text, rot)
    
    
    return '<h1>' + encrypted_text + '</h1>'    

@app.route("/")
def index():
    return form

app.run()