# -*- coding: utf-8 -*-
from xml import sax
from app.parser.record import RecordObject


class AbstractParser(object):
    def __init__(self, logfile):
        self.file = logfile
        self.results = []

    def parse(self):
        raise NotImplementedError


class AbstractGPXParser(AbstractParser):
    handler = None
    handler_class = None

    def __init__(self, logfile):
        super(AbstractGPXParser, self).__init__(logfile)
        self.handler = self.handler_class()

    def parse(self):
        parser = sax.make_parser()
        parser.setContentHandler(self.handler)
        parser.setFeature(sax.handler.feature_external_ges, 0)

        try:
            parser.parse(self.file)
        except sax.SAXParseException:
            raise Exception('Could not parse file.')

        for result in self.handler.results:
            tm, lon, lat, ele = result
            self.results.append(RecordObject(
                timestamp=tm,
                longitude=lon,
                latitude=lat,
                altitude=ele,
            ))

        return True
