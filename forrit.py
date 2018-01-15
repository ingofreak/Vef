from bottle import *
import os

@route('/')
def index():
  return "Bottlepy virkar, alveg rosa gaman...<a href="www.vefsida-ingo.herokuapp.com/about">about</a><a href="www.vefsida-ingo.herokuapp.com/pic">pic</a><a href="www.vefsida-ingo.herokuapp.com/bio">bio</a>"
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
