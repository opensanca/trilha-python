"""
Uma simplíssima aplicação web que gera uma página de Hello World
usando o framework web [Bottle](http://bottlepy.org)

Para instalar o framework use o pip:
    $ pip install bottle
"""

from bottle import route, run, template


@route('/hello/<name>')
def hello(name):
    return template('<b>Hello {{name}}</b>', name=name)

run(host='localhost', port='8888')
