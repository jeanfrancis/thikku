import os
from flask import Flask, render_template, request, redirect
import sms

# test mobile number
TEST_NUMBER = os.getenv('TEST_NUMBER', '')

app = Flask(__name__)
app.config['DEBUG'] = os.environ.get('DEBUG', False)

@app.route('/')
def hello():
  return 'Hello World!'

@app.route('/send-sms', methods=['GET'])
def send_sms():
  text = request.args.get('Text')
  to = request.args.get('To')
  sms.send(to, text)
  return 'Message sent!'

@app.route("/receive-sms", methods=['GET'])
def receive_sms():
  text = request.args.get('Text')
  _from = request.args.get('From')
  sms.send(TEST_NUMBER, 'Text received: %s - From: %s' % (text, _from))
  return 'Message received!'

if __name__ == '__main__':
  app.run()

#http://maps.googleapis.com/maps/api/directions/json?origin=:origin&destination=:destination
