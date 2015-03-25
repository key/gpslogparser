# -*- coding: utf-8 -*-
from app import app


DEBUG = True
SECRET_KEY = 'fugahoge'
CSRF_ENABLED = False


app.config.from_object(__name__)
app.run(host='0.0.0.0', debug=DEBUG)
