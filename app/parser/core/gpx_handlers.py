# -*- coding: utf-8 -*-
from xml.sax import ContentHandler


class TrackPointHandler(ContentHandler):
    def __init__(self):
        self.results = []
        self.initialize()

    def startElement(self, name, attrs):
        if name == 'trkpt':
            self.initialize()

            self.lon = attrs['lon']
            self.lat = attrs['lat']
        elif name == 'time':
            self.inTime = True
        elif name == 'ele':
            self.inEle = True

    def endElement(self, name):
        if name == 'trkpt':
            self.results.append([self.time, self.lon, self.lat, self.ele])
        elif name == 'time':
            self.inTime = False
        elif name == 'ele':
            self.inEle = False

    def characters(self, content):
        if self.inTime:
            self.time += content.strip()
        if self.inEle:
            self.ele += content.strip()

    def initialize(self):
        self.lon = ''
        self.lat = ''
        self.time = ''
        self.ele = ''

        self.inEle = False
        self.inTime = False


class WayPointHandler(ContentHandler):
    def __init__(self):
        self.results = []
        self.initialize()

    def startElement(self, name, attrs):
        if name == 'wpt':
            self.initialize()

            self.lon = attrs['lon']
            self.lat = attrs['lat']
        elif name == 'ele':
            self.inEle = True

    def endElement(self, name):
        if name == 'wpt':
            self.results.append([None, self.lon, self.lat, self.ele])
        elif name == 'ele':
            self.inEle = False

    def characters(self, content):
        if self.inEle:
            self.ele += content.strip()

    def initialize(self):
        self.lon = ''
        self.lat = ''
        self.ele = ''
        self.inEle = False