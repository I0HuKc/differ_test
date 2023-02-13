from __future__ import annotations

import math


class Place:
    def __init__(self, name: str, latitude: float, longitude: float):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

    def get_latitude_radian(self) -> float:
        return self.latitude*math.pi/180

    def get_longitude_radian(self) -> float:
        return self.longitude*math.pi/180

    def distance(self, to: Place) -> float:
        # Sphere radius (Earth)
        rad = 6372795

        # In radians
        lat1 = self.get_latitude_radian()
        lat2 = to.get_latitude_radian()
        long1 = self.get_longitude_radian()
        long2 = to.get_longitude_radian()

        # Cosines and sines of latitudes and longitude differences
        cl1 = math.cos(lat1)
        cl2 = math.cos(lat2)
        sl1 = math.sin(lat1)
        sl2 = math.sin(lat2)
        delta = long2 - long1
        cdelta = math.cos(delta)
        sdelta = math.sin(delta)

        # Great circle distance
        y = math.sqrt(math.pow(cl2*sdelta, 2) +
                      math.pow(cl1*sl2-sl1*cl2*cdelta, 2))
        x = sl1*sl2+cl1*cl2*cdelta
        ad = math.atan2(y, x)
        dist = ad*rad

        return round(dist/1000, 2)
