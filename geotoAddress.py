from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="hamza")
location = geolocator.geocode("عمان شفا بدران")
print(location.address)
print((location.latitude, location.longitude))
print(location.raw)