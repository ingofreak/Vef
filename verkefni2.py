from bottle import *
import os

@route('/')
def index():
    return "Verkefni 2A<br><a href='/a'> Verkefni A </a>&nbsp;<a href='/b'> Verkefni B </a>"

@route('/a')
def index():
    return "<a href='/a/sida/1'> Síða 1 </a>&nbsp;<a href='/a/sida/2'> Síða 2 </a>&nbsp;<a href='/a/sida/3'> Síða 3 </a>"

@route('/b')
def index():
    return "Verkefni b<br><a href='/b/sida?bokstafur=b'><img src='myndir/b.png'></a>&nbsp;<a href='/b/sida?bokstafur=a'><img src='myndir/a.png'></a>&nbsp;<a href='/b/sida?bokstafur=c'><img src='myndir/c.png'></a>"

@route('/a/sida/<id>')
def index(id):
    return 'þú ert kominn á síðu ', id

@route('/b/sida')
def page():
    print("virkar")
    a = request.query.bokstafur
    print(a)
    if a == 'a':
        return "Þetta er bókstafur:<br><img src='/myndir/a.png'>"
    if a == 'b':
        return "Þetta er bókstafur:<br><img src='/myndir/b.png'>"
    if a == 'c':
        return "Þetta er bókstafur:<br><img src='/myndir/c.png'>"

@error(404)
def villa(error):
    return "<h2>Þessi síða er ekki til</h2>"
"""
def show_pic():
    picture_name = 'a.png'
    return template('template', picture=picture_name)
"""

@route('/myndir/<filename>')
def server_static(filename):
    return static_file(filename, root='myndir')


run(host='0.0.0.0', port=os.environ.get('PORT'))

#if __name__== '__main__':
#    run()

#run(host='localhost', port=8080)
#run()
