#!/usr/bin/env python2
#-*- coding: utf-8 -*-

try:
    import config
except:
    sys.exit('Arquivo de configuração não foi encontrado!')

from flask import Flask, Response, request
app = Flask(__name__)

@app.route('/save/<id>')
def save(id):
    response = Response(str(request.args), status=200)
    return response

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9000, debug=config.debug)
