from geopy.geocoders import Nominatim

#transform lat, log to distance
from numpy import sin, cos, arccos, pi, round

def rad2deg(radians):
    degrees = radians * 180 / pi
    return degrees

def deg2rad(degrees):
    radians = degrees * pi / 180
    return radians

def getDistanceBetweenPointsNew(latitude1, longitude1, latitude2, longitude2):
    
    theta = longitude1 - longitude2
    
    distance = 60 * 1.1515 * rad2deg(
        arccos(
            (sin(deg2rad(latitude1)) * sin(deg2rad(latitude2))) + 
            (cos(deg2rad(latitude1)) * cos(deg2rad(latitude2)) * cos(deg2rad(theta)))
        )
    )
    
    return round(distance * 1.609344, 2)
#-----



# Initialize the geolocator
geolocator = Nominatim(user_agent="travel_optimizer")

# Function to get coordinates of a place
def get_location(place):
    location = geolocator.geocode(place, exactly_one=False)
    print(location)
    if location:
        return {
            "name": location.address,
            "latitude": location.latitude,
            "longitude": location.longitude
        }
    else:
        return "Location not found."

# Example usage
place_name = "uniqlo, Tokyo"
location_data = get_location(place_name)

print("Search result:", location_data)
