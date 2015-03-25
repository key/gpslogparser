# -*- coding: utf-8 -*-
import isodate
import fitparse
import pytz

from app.parser.record import RecordObject
from . import AbstractParser


class FitFileParser(AbstractParser):
    def parse(self):
        activity = fitparse.FitFile(self.file)
        activity.parse()

        # TODO lap, device_infoをサポートする(profile.defより)
        for data in activity.get_messages('record'):
            # Get field names in record
            valid_field_names = [field.name for field in data.fields]
            # ['timestamp', 'position_lat', 'position_long', 'distance', 'altitude', 'speed', 'power', 'heart_rate', 'cadence', 'temperature']

            record = data.get_values()
            timestamp = isodate.datetime_isoformat(record['timestamp'].replace(tzinfo=pytz.UTC)) if 'timestamp' in valid_field_names else None
            temperature = record['temperature'] if 'temperature' in valid_field_names else None
            distance = record['distance'] if 'distance' in valid_field_names else None
            heartratebpm = record['heart_rate'] if 'heart_rate' in valid_field_names else None
            cadence = record['cadence'] if 'cadence' in valid_field_names else None
            power = record['power'] if 'power' in valid_field_names else None
            altitude = record['altitude'] if 'altitude' in valid_field_names else None
            speed = record['speed'] if 'speed' in valid_field_names else None

            # semicircles to degrees -> semicircles * ( 180 / 2^ 31 )
            lat = record['position_lat'] * (180.0 / pow(2, 31)) if 'position_lat' in valid_field_names else None
            lon = record['position_long'] * (180.0 / pow(2, 31)) if 'position_long' in valid_field_names else None

            self.results.append(RecordObject(
                timestamp,
                temperature=temperature,
                distance=distance,
                heartratebpm=heartratebpm,
                cadence=cadence,
                power=power,
                altitude=altitude,
                speed=speed,
                latitude=lat,
                longitude=lon,
            ))

        return True
