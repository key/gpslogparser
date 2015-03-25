# coding: utf-8
import json

from flask import render_template, Response
from . import app
from . import consts
from .forms import FileForm
from .parser import GPSLogParser


RESPONSE_FORMAT = {
    'csv': 'text/csv',
    'json': 'application/json',
}


@app.route('/', methods=('GET', ))
def index():
    return render_template('form.html', form=FileForm())


@app.route('/parse', methods=('POST', ))
def parser():
    form = FileForm()
    if form.validate_on_submit():
        logfile = form.logfile.data.stream
        p = GPSLogParser(logfile)
        records = [record.as_dict() for record in p.parse()]

        output_format = form.format.data
        if not output_format:
            output_format = 'json'
        mimetype = RESPONSE_FORMAT[output_format]

        if output_format == 'json':
            def restrict_fields(v):
                fields = form.fields.data
                if not fields:
                    fields = ','.join(consts.DEFAULT_FIELDS)

                ret = {}
                for field in fields.split(','):
                    field = field.strip()
                    if field in v:
                        ret[field] = v[field]
                return ret

            return Response(json.dumps(map(restrict_fields, records)), mimetype=mimetype)

        if output_format == 'csv':
            def restrict_fields(v):
                fields = form.fields.data
                if not fields:
                    fields = ','.join(consts.DEFAULT_FIELDS)

                ret = []
                for field in fields.split(','):
                    if field in v:
                        ret.append(str(v[field]) if v[field] is not None else '')
                return ','.join(ret)

            fields = form.fields.data
            if fields == '' or fields is None:
                fields = ','.join(consts.DEFAULT_FIELDS)

            output = fields + '\n'  # HEADER
            output += '\n'.join(map(restrict_fields, records))
            return Response(output, mimetype=mimetype)
    return render_template('form.html', form=form)
