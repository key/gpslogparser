# -*- coding: utf-8 -*-
class RecordObject(object):
    timestamp = None
    distance = None
    temperature = None
    heartratebpm = None
    cadence = None
    power = None
    speed = None
    altitude = None
    latitude = None
    longitude = None

    def __init__(self, timestamp, temperature=None, distance=None, heartratebpm=None,
                 cadence=None, power=None, speed=None, altitude=None, latitude=None, longitude=None):
        self.timestamp = timestamp  # str
        self.temperature = temperature
        self.distance = distance
        self.heartratebpm = heartratebpm
        self.cadence = cadence
        self.power = power
        self.speed = speed
        self.altitude = altitude
        self.latitude = latitude
        self.longitude = longitude

    def as_dict(self):
        return {
            'timestamp': self.timestamp,
            'distance': self.distance,
            'temperature': self.temperature,
            'heartratebpm': self.heartratebpm,
            'cadence': self.cadence,
            'power': self.power,
            'altitude': self.altitude,
            'speed': self.speed,
            'latitude': self.latitude,
            'longitude': self.longitude,
        }
