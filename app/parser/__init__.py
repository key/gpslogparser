# -*- coding: utf-8 -*-
from io import BytesIO
import re

from . import consts
from .core.fit import FitFileParser
from .core.gpx import GPXWayPointParser
from .core.gpx import GPXTrackPointParser


class GPSLogParser(object):

    def __init__(self, logfile):
        """

        :param logfile: GPS Log file (or file path)
        :type logfile: str or file
        """
        if isinstance(logfile, str):
            logfile = open(logfile, 'r')
        self.logfile = logfile
        self._parser = self._parser_factory()(self.logfile)

    def _parser_factory(self):
        """Detect file type and returns parser class.

        :return: GPS Log parser class
        :rtype: class
        """
        result = detector(self.logfile)
        if not result:
            raise Exception('Could not detect type for specified log file.')

        if result == consts.FILE_TYPE_FIT:
            return FitFileParser
        # elif result == consts.FILE_TYPE_TCX_HISTORY:
        #     return TCXHistoryHandler
        elif result == consts.FILE_TYPE_GPX_TRACKPOINT:
            return GPXTrackPointParser
        elif result == consts.FILE_TYPE_GPX_WAYPOINT:
            return GPXWayPointParser

    def parse(self):
        """Parsing GPS Log file and returns parsed record list.

        :return:
        :rtype: list or RecordObject
        """
        if not self._parser:
            raise Exception('Parser is not set.')

        result = self._parser.parse()
        if result:
            return self._parser.results


def detector(f):
    """Detect file type

    :param f:
    :type f: str or bytes or file
    :return:
    """
    try:
        if isinstance(f, (file, BytesIO)):
            buf = f.read()
        else:
            buf = f

        if re.search('<gpx', buf):
            if re.search('<trkseg>', buf):
                return consts.FILE_TYPE_GPX_TRACKPOINT
            if re.search('<wpt', buf) and re.search('</wpt>', buf):
                return consts.FILE_TYPE_GPX_WAYPOINT
        if re.search('<TrainingCenterDatabase', buf):
            if re.search('<Activities', buf):
                return consts.FILE_TYPE_TCX_HISTORY
            if re.search('<Courses', buf):
                return consts.FILE_TYPE_TCX_COURSE
        if buf[8:12] == '.FIT':
            return consts.FILE_TYPE_FIT
    finally:
        if f:
            f.seek(0)
