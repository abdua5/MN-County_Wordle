#import the modules that will be needed
import random
import geopy.distance
from geopy.geocoders import Nominatim

def play_wordle():
    geolocator = Nominatim(user_agent="mn-county-wordle")
    county_coordinates = {}
    counties = ["Hennepin County", "Ramsey County", "Dakota County", "Anoka County", "Washington County", "St. Louis "
                                                                                                          "County",
                "Olmsted County", "Stearns County", "Scott County", "Wright County"]
    for county in counties:
        location = geolocator.geocode(county)
        county_coordinates[county] = (location.latitude, location.longitude)
    target_county = random.choice(counties)

    # Prompt user to keep trying or give up
    while True:
        county = input("Enter a county in Minnesota or type 'I give up' to reveal the correct answer: ")
        if county.lower() == "i give up":
            print("The correct answer was " + target_county + ".")
            break
        elif county == target_county:
            print("Congratulations! You guessed the correct county in Minnesota in the Wordle game!")
            break
        else:
            entered_county_coordinates = county_coordinates[county]
            target_county_coordinates = county_coordinates[target_county]
            distance = geopy.distance.geodesic(entered_county_coordinates, target_county_coordinates)
            print("The entered county is ", distance.miles, " miles away from the target county.")

# Start game
play_wordle()
