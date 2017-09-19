# Import GoogleMaps and JSON module
import googlemaps, json

# Initialize the google map Api with your public key
# A public key could be created at [ https://developers.google.com/maps/documentation/javascript/get-api-key ]
gmaps = googlemaps.Client(key='API_KEY')

# Specify all the cities you want to access
cities = { 
      "Agege": "",
      "Ajeromi-Ifelodun": "" ,
      "Alimosho": "",
      "Amuwo-Odofin": "",
      "Apapa": "",
      "Eti-Osa": "",
      "Ifako-Ijaiye": "",
      "Ikeja": "",
      "Kosofe": "",
      "Lagos Island": "",
      "Lagos Mainland": "",
      "Mushin": "",
      "Ojo": "",
      "Oshodi-Isolo": "",
      "Somolu": "",
      "Surulere": "",
    }

# Specify all the key centres you want to access
# Visit [ https://developers.google.com/places/supported_types ] for the Supported types
keywords = ["hospital", "restaurant", "store"]

# Get latitude of each cities
for city in cities:
  
  # Get the geocoding address from google map
  data = gmaps.geocode('%s, Lagos, NG' % city)[0]

  # Update dictionary with each cities latitude and longitude value
  cities[city] = str(data["geometry"]["location"]["lat"]) + ", " + str(data["geometry"]["location"]["lng"])
  
  # Notify of progress
  print("GOTTEN LOCATION FOR %s" % city)


# Loop through cities and get the respective data for keywords and write to file
with open("result.txt", "w") as file:
    # Loop through all cities in Lagos 
    for (index, (city, lat_long) ) in enumerate(cities.items()):

      # Properly label the heading of the file with the city's name
      file.write("*"*50 + "\n" + city.upper() + "\n" + "*"*50)

      # Get keyword data
      for keyword in keywords:
        #write keyword to file
        file.write("\n\n" + keyword.upper() + "\n\n" + "*"*50)

        # Get the places from google map
        data = gmaps.places(radius = 50000, location = lat_long, type = keyword, query = keyword)
        
        # [UNCOMMENT] ==>>> If you want to see the ouput on the Python console
        #print(''.join('{}{}'.format(key, val) for key, val in data.items()))
        
        # Write the places details recieved into text file
        file.write(json.dumps(data) + "\n\n")

        # Notify of progress
        print("DONE FOR %s - %s" % (city, keyword))


# Notify when done, and begin your Lagos Journey
print("<---- COMPLETED ---->")