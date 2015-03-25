# -*- coding: utf-8 -*-
from gevent.wsgi import WSGIServer
from app import app


DEBUG = True
SECRET_KEY = 'fugahoge'
WTF_CSRF_ENABLED = False


app.config.from_object(__name__)

http_server = WSGIServer(('', 5000), app)
http_server.serve_forever()
