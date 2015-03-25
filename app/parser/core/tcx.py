# -*- coding: utf-8 -*-
from xml.sax import ContentHandler


class TCXHistoryHandler(ContentHandler):
    def __init__(self):
        self.results = []

        self._init_data()
        self._init_flags()

        self.inActivities = False
        self.inActivity = False
        self.inLap = False
        self.inTrack = False

    def startElement(self, name, attrs):
        if name == 'Activities':
            self.inActivities = True
        elif name == 'Activity':
            self.inActivity = True
        elif name == 'Lap':
            self.inLap = True
        elif name == 'Track':
            self.inTrack = True
        elif name == 'Trackpoint':
            self.inTrackpoint = True
        elif name == 'Time':
            self.inTime = True
        elif name == 'Position':
            self.inPosition = True
        elif name == 'LatitudeDegrees':
            self.inLatitude = True
        elif name == 'LongitudeDegrees':
            self.inLongitude = True
        elif name == 'AltitudeMeters':
            self.inAltitude = True

    def endElement(self, name):
        if name == 'Trackpoint':
            self.results.append([self.time, self.lon, self.lat, self.ele])

            self._init_data()
            self._init_flags()
        elif name == 'Time':
            self.inTime = False
        elif name == 'Position':
            self.inPosition = False
            self.inLatitude = False
            self.inLongitude = False
        elif name == 'LatitudeDegrees':
            self.inLatitude = False
        elif name == 'LongitudeDegrees':
            self.inLongitude = False
        elif name == 'AltitudeMeters':
            self.inAltitude = False

    def characters(self, content):
        if self.inTime:
            self.time += content.strip()
        if self.inLatitude:
            self.lat += content.strip()
        if self.inLongitude:
            self.lon += content.strip()
        if self.inAltitude:
            self.ele += content.strip()

    def _init_data(self):
        self.time = ''
        self.lon = ''
        self.lat = ''
        self.ele = ''

    def _init_flags(self):
        """Trackpoint要素より配下のフラグを全て落とす

        :return:
        """
        self.inTrackpoint = False
        self.inTime = False
        self.inPosition = False
        self.inLatitude = False
        self.inLongitude = False
        self.inAltitude = False
