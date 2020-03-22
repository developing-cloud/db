import os

save_event = {'action': 'save', 'input': {
    'registration-number': 'SB8392Y', 'timestamp': '2020:02:27 16:31:36', 'bucket': 'a', 'key': 'b',
    'device': 'samsung SM-J610FN', 'GPSVersionID': '\x02\x02\x00\x00', 'GPSLatitudeRef': 'N',
    'GPSLatitude': [[50, 1], [2, 1], [380457, 10000]], 'GPSLongitudeRef': 'E',
    'GPSLongitude': [[18, 1], [41, 1], [62080, 10000]], 'GPSAltitudeRef': '\x00', 'GPSAltitude': [0, 1000],
    'GPSTimeStamp': [[15, 1], [31, 1], [25, 1]], 'GPSDateStamp': '2020:02:27'
}}

query_event = {'action': 'query', 'input': {
    'registration-number': 'SB8392Y'
}}

os.environ['VEHICLE_REGISTRY_TABLE_NAME_PARAM'] = '/toll-registry/table-name/vehicle-registry-dev'

from db import lambda_handler

lambda_handler(save_event, None)
