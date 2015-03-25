# -*- coding: utf-8 -*-

from . import AbstractGPXParser
from .gpx_handlers import TrackPointHandler
from .gpx_handlers import WayPointHandler


class GPXTrackPointParser(AbstractGPXParser):
    handler_class = TrackPointHandler


class GPXWayPointParser(AbstractGPXParser):
    handler_class = WayPointHandler
