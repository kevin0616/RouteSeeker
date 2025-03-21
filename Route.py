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
   
    if location:
        return location
    else:
        return []

city = 'Tokyo'
shops = ['uniqlo', 'GU', 'bic camera']
len_shops = len(shops)
queries = [s +", " + city for s in shops]
print(queries)

place_name = "uniqlo, Tokyo"
queries_results = []

for q in queries:
    queries_results.append(get_location(q))
l1, l2 = len(queries_results), len(queries_results[0])

ans = 0
detail = []
for i in range(len_shops):
    for j in range(len(queries_results[i])):
        res = 1
        de = [queries_results[i][j].address]
        lon, lat = queries_results[i][j].longitude, queries_results[i][j].latitude
        for k in range(i+1, len_shops):
            for l in range(len(queries_results[k])):
                lon_2, lat_2 = queries_results[k][l].longitude, queries_results[k][l].latitude
                if getDistanceBetweenPointsNew(lat, lon, lat_2, lon_2) <= 2:
                    res += 1
                    de.append(queries_results[k][l].address)
                    break
        if res >= ans:
            ans = res
            detail.append(de)
            
print(ans, detail)
#location_data = get_location(place_name)

#print("Search result:", location_data)
