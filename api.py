from flask import *
import json
import time 
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home_page():
    data_set ={'page':'Home','message':'Succesfully loaded the home page','timestap':time.time()}
    json_dumps = json.dumps(data_set)
    return json_dumps

@app.route('/user/')
def request_page():
    user_query = str(request.args.get('user'))  # /user/?user=User_Name 
    data_set = {'page':'Request','message':f'Succesfully got the request for {user_query}',
                'timestap':time.time()}
    json_dump = json.dumps(data_set)
    return json_dump


if __name__ =='__main__':
    app.run(debug = True,port=7777)
    
    
