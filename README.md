# About

This module provides feature for parsing gps log file.
Posting a GPS files via HTTP, you will be able to parse the GPS log file.

Supported GPS files:

* FIT (Record)
* GPX Waypoint
* GPX Trackpoint

You can get parsed data with specified format. Supported formats see below.

* CSV
* JSON

# Usage

## setup

```
pip install -r requirements.txt
```

## start instance

```
python run.py
```

## parse gps log file

```
curl \
  -F "logfile=@tests/test.fit" \
  -F "format=json" \
  -F "fields=timestamp,heartratebpm,cadence,latitude,longitude" \
  http://127.0.0.1:5000/parse
```

