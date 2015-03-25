# -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from wtforms import FileField, StringField
from wtforms.validators import DataRequired


class FileForm(Form):
    logfile = FileField('logfile', validators=[DataRequired()])
    fields = StringField(default='')
    format = StringField(default='json')
