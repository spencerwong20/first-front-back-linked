from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS

import random
import string

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/users', methods=['GET', 'POST', 'DELETE'])
def get_users():
   if request.method == 'GET':
      search_username = request.args.get('name')
      search_job = request.args.get('job')
      if search_username and search_job:
         subdict = {'users_list' : []}
         for user in users['users_list']:
            if user['name'] == search_username:
               if user['job'] == search_job:
                  subdict['users_list'].append(user)
         return subdict
      elif search_username :
         subdict = {'users_list' : []}
         for user in users['users_list']:
            if user['name'] == search_username:
               subdict['users_list'].append(user)
         return subdict
      return users
   elif request.method == 'POST':
      userToAdd = request.get_json()
      name = userToAdd['name']
      users['users_list'].append(userToAdd)
      id = randomIDGenerator()
      users['users_list'][-1]['id'] = id
      resp = jsonify(userToAdd)
      resp.status_code = 201
      #resp.status_code = 200 #optionally, you can always set a response code. 
      # 200 is the default code for a normal response
      return resp
   elif request.method == 'DELETE':
      userToAdd = request.get_json()
      try:
         users['users_list'].remove(userToAdd)
         resp = jsonify(success=True)
         resp.status_code = 204
<<<<<<< HEAD
      except ValueError:
         resp = jsonify(success=False)
         resp.status_code = 404
=======
      
      except ValueError:
         resp = jsonify(success = False)
         resp.status_code = 404
      
>>>>>>> 6d910c22a08f669f72cf20948ce293da58ff756d
      #resp.status_code = 200 #optionally, you can always set a response code. 
      # 200 is the default code for a normal response
      return resp

@app.route('/users/<id>')
def get_user(id):
   if id :
      for user in users['users_list']:
        if user['id'] == id:
           return user
      return ({})
   return users

users = { 
   'users_list' :
   [
      { 
         'id' : 'xyz789',
         'name' : 'Charlie',
         'job': 'Janitor',
      },
      {
         'id' : 'abc123', 
         'name': 'Mac',
         'job': 'Bouncer',
      },
      {
         'id' : 'ppp222', 
         'name': 'Mac',
         'job': 'Professor',
      }, 
      {
         'id' : 'yat999', 
         'name': 'Dee',
         'job': 'Aspring actress',
      },
      {
         'id' : 'zap555', 
         'name': 'Dennis',
         'job': 'Bartender',
      }
   ]
}

def randomIDGenerator(charLetters = string.ascii_lowercase,
   charNums =  string.digits):
   id =  ''.join(random.choice(charLetters) for i in range(3))
   return id.join(random.choice(charNums) for n in range(3))
