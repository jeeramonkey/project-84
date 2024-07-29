from flask import Flask, render_template, request, redirect
import os
from encrypt import encrypt, decrypt, generateKeys
# import generatehash from hash.py
from hash import generateHash

STATIC_DIR = os.path.abspath('static')

app = Flask(__name__, static_folder=STATIC_DIR)
app.use_static_for_root = True

blockData={}

publicKey, privateKey = generateKeys()

@app.route("/", methods= ["GET", "POST"])
def home():
     return render_template('signup.html')
     
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    global blockData
    if request.method == 'POST':
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        # Generate hash for the password instead of encrypting it 
        password = generateHash(password)
        password = encrypt(password, publicKey)

        blockData = {
            'username': username,
            'email': email,
            'password': password
        }
        
        
        return redirect('/signin')
    return render_template('signup.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    global blockData
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Replace following line and Generate Hash of the password variable recieved from the signin form and save it in variable 'hash'
        hash = generateHash(password)
        plainPassword = decrypt(blockData['password'], privateKey)

        # Compair hash password stored in the block and the current hash insead of plainPassword == password
        
        if blockData['username'] == username and plainPassword == password:
                    return render_template('profile.html', block= blockData)
        if blockData['username'] == username and blockData['password'] == hash:

            return "Invalid credentials!"
    return render_template('signin.html')


    
if __name__ == '__main__':
    app.run(debug = True, port=4000)