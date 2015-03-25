# -*- coding: utf-8 -*-
import unittest
import os


class ViewTestCase(unittest.TestCase):
    def setUp(self):
        from app import app

        app.config['CSRF_ENABLED'] = False
        app.config['SECRET_KEY'] = 'foobar'

        self.client = app.test_client()

    def test_index(self):
        result = self.client.get('/')
        assert result.status_code == 200

    def test_parse(self):
        result = self.client.get('/parse')
        assert result.status_code == 405

        result = self.client.post('/parse')
        assert result.status_code == 200


class GPSLogParserTestCase(unittest.TestCase):
    def setUp(self):
        self.fit_file = open(os.path.join(os.path.dirname(__file__), 'tests', 'test.fit'), 'r')
        self.gpx_waypoint = open(os.path.join(os.path.dirname(__file__), 'tests', 'test_wpt.gpx'), 'r')
        self.gpx_trackpoint = open(os.path.join(os.path.dirname(__file__), 'tests', 'test_trk.gpx'), 'r')

    def test_detect(self):
        from app.parser import detector
        from app.parser import consts

        self.assertEqual(detector(self.fit_file), consts.FILE_TYPE_FIT)
        self.assertEqual(detector(self.gpx_waypoint), consts.FILE_TYPE_GPX_WAYPOINT)
        self.assertEqual(detector(self.gpx_trackpoint), consts.FILE_TYPE_GPX_TRACKPOINT)
        self.assertIsNone(detector(''))

    def test_parse_fit(self):
        from app.parser import GPSLogParser

        instance = GPSLogParser(self.fit_file)
        result = instance.parse()
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 4821)

    def test_parse_gpx_wpt(self):
        from app.parser import GPSLogParser

        instance = GPSLogParser(self.gpx_waypoint)
        result = instance.parse()
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 2)

        a, b = result
        self.assertIsNone(a.timestamp)
        self.assertIsNone(b.timestamp)

    def test_parse_gpx_trk(self):
        from app.parser import GPSLogParser

        instance = GPSLogParser(self.gpx_trackpoint)
        result = instance.parse()
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 2)

        a, b = result
        self.assertEqual(a.timestamp, '2014-01-07T05:38:54Z')
        self.assertEqual(b.timestamp, '2014-01-07T06:03:55Z')


if __name__ == '__main__':
    unittest.main()
