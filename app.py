from flask import Flask, render_template, request
import base64

app = Flask(__name__)

def encode_base64(text):
    return base64.b64encode(text.encode()).decode()

def decode_base64(text):
    return base64.b64decode(text.encode()).decode()

def caesar_cipher(text, shift, decrypt=False):
    if decrypt:
        shift = -shift
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            result += chr((ord(char) + shift - shift_amount) % 26 + shift_amount)
        else:
            result += char
    return result

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ''
    if request.method == 'POST':
        text = request.form['text']
        method = request.form['method']
        operation = request.form['operation']
        if method == 'base64':
            if operation == 'encode':
                result = encode_base64(text)
            else:
                result = decode_base64(text)
        elif method == 'caesar':
            shift = int(request.form['shift'])
            if operation == 'encode':
                result = caesar_cipher(text, shift)
            else:
                result = caesar_cipher(text, shift, decrypt=True)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
