from flask import Flask, jsonify, render_template, request
import datetime
import pytz
import os


def get_time(timezone):
    timezone_datetime = datetime.datetime.now(pytz.timezone(timezone)) #'America/New_York'
    return timezone_datetime

app = Flask(__name__)

app.jinja_env.globals.update(get_time=get_time)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/health")
def ReturnJSON(): 
    if(request.method == 'GET'): 
        data = { 
            "Responce" : 200, 
        } 
  
        return jsonify(data) 

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8080))
    app.run(debug=True, host='0.0.0.0', port=port)