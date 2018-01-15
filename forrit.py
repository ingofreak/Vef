from bottle import *
import os

@route('/')
def index():
  return "Bottlepy virkar, alveg rosa gaman...<br><a href='/about'>about </a><a href='/pic'>pic </a><a href='/bio'>bio </a>"
@route('/about')
def about():
  return "þetta er about"
@route('/pic')
def pic():
  return "Þetta er fyrir myndir"
@route('/bio')
def bio():
  return "Þetta er bio"
  
#run()
run(host="0.0.0.0", port=os.environ.get('PORT'))
