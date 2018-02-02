from bottle import *
import os

@route('/')
def index():
    return "Verkefni 3<br><a href='/a'> Verkefni A </a>&nbsp;<a href='/b'> Verkefni B </a>"


@route('/a')
def index():
    return "Kennitala 1:&nbsp<a href='/a/1307826234'>1307826234</a><br> Kennitala 2:&nbsp<a href='/a/1027093994'> 1027093994</a>"

'''
@route('/b/<frettalist[0]')
def index(frettalist[0])
    return template('verkefni3b1.tpl')'''
    

@route('/a/<kt>')
def index(kt):
    return template('verkefni3a.tpl',kt=kt)

@error(404)
def villa(error):
    return "<h2>Þessi síða er ekki til</h2>"

run(host='0.0.0.0', port=os.environ.get('PORT'))

#if __name__== '__main__':
 #   run()

#run(host='localhost', port=8080)
#run()
