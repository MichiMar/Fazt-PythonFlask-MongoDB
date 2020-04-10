from flask import Flask, request
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['MONGO_URI']='mongodb://localhost/pythonmongodb'
mongo = PyMongo(app)

@app.route('/users', methods=['POST'])
def create_user():
    #reciving data
   username = request.json['username']
   password = request.json['password'] #para cifrar lacontrase;a importare un modulo que me ayudara a cifrar de manera automatica
   email = request.json['email']

   if username and email and password:
       hashed_password = generate_password_hash(password)
       id = mongo.db.users.insert(
           {'username': ussername, 'password': hashed_password, 'email': email}
       )
       response = {
           'id': str(id),
           'username': username,
           'password': password,
           'email': email
       }
       return response
    else:
        {'message': 'received'}
        

    return {'message': 'received'}

if __name__ == "__main__":
    app.run(debug=True)