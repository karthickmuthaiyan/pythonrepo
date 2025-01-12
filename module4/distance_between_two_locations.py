import math
import haversine as hs
from haversine import Unit

def haversine(lat1, lon1, lat2, lon2):
    # Convert latitude and longitude from degrees to radians
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.asin(math.sqrt(a))

    # Radius of Earth in kilometers. Use 3956 for miles
    r = 6371.0

    # Calculate the result
    distance = c * r

    return distance

# Example usage
lat1 = 52.2296756
lon1 = 21.0122287
lat2 = 41.8919300
lon2 = 12.5113300

print(f"Distance: {haversine(lat1, lon1, lat2, lon2)} km")
print("Distance is",hs.haversine((lat1, lon1), (lat2, lon2), unit=Unit.MILES),"miles")