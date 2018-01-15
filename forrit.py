from bottle import *
import os

@route('/')
def index():
  return "Bottlepy virkar"
  
run(host="0.0.0.0", port=os.environ.get('PORT'))
