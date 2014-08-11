import os
from flask import Flask, render_template, request, redirect
import sms
import direction

# test mobile number
TEST_NUMBER = os.getenv('TEST_NUMBER', '')

app = Flask(__name__, static_folder='client', static_url_path='')
app.config['DEBUG'] = os.environ.get('DEBUG', False)

@app.route('/')
def index():
  return app.send_static_file('index.html')

@app.route('/api/direction', methods=['POST'])
def send_sms():
  origin = request.form.get('origin'),
  destination.args.get('destination')
  return direction.getDirection(origin, destination)

@app.route("/receive-sms", methods=['GET'])
def receive_sms():
  text = request.args.get('Text')
  _from = request.args.get('From')
  origin,destination = text.split(":")
  if origin == None or destination == None:
    return 'Message does not satify the schema', 404

  response = direction.getDirection(origin, destination)
  sms.send(_from, response)
  return 'Success!'

if __name__ == '__main__':
  app.run()
