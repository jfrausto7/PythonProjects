# imports
import requests
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim
import numpy as np

# create geopy object and function for finding long and lat
gn = Nominatim(user_agent="weather-Scraper")

def geolocate(city=None, country=None):
    '''
    Inputs city and country, or just country. Returns the lat/long coordinates of
    either the city if possible, if not, then returns lat/long of the center of the country.
    '''

    # If the city exists,
    if city != None:
        # Try
        try:
            # To geolocate the city and country
            loc = gn.geocode(str(city + ',' + country))
            # And return latitude and longitude
            return (loc.latitude, loc.longitude)
        # Otherwise
        except:
            # Return missing value
            return np.nan
    # If the city doesn't exist
    else:
        # Try
        try:
            # Geolocate the center of the country
            loc = gn.geocode(country)
            # And return latitude and longitude
            return (loc.latitude, loc.longitude)
        # Otherwise
        except:
            # Return missing value
            return np.nan

# hashmap of all US states
states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}


# ask for input from the user and store as variables
resultCity = input("Enter a US city: ")
resultState = input("Enter the state: ")
result = geolocate(city=resultCity, country="USA")
# location = input("Enter a location (city, state ZIP): ")
# print(location)

# Provide the latitude and longitude for the location you would like to check the weather for
# Lat/lon in decimal degrees provided by input
# Try/except catches if city doesn't exist or if input was wrong
try:
    lat = result[0]

except:
    print("Error: Input was invalid or does not exist.")
    exit()

if(states.get(resultState)):
    lon = result[1]
else:
    try:
        if(states[resultState]):
            lon = result[1]
    except:
        print("Error: Input was invalid or does not exist.")
        exit()



# Create url for the requested location through string concatenation
url = 'https://forecast.weather.gov/MapClick.php?lat='+str(lat)+"&lon="+str(lon)
# Check if the URL exists
# print url

# Send request to retrieve the web-page using the get() function from the requests library
# The page variable stores the response from the web-page
page = requests.get(url)

# Create a BeautifulSoup object with the response from the URL
# Access contents of the web-page using .content
# html_parser is used since our page is in HTML format
soup=BeautifulSoup(page.content,"html.parser")

# Locate element on page to be scraped
# This element is located within an id tag called current_conditions-summary
# find() locates the element in the BeautifulSoup object
cur_weather_conditions = soup.find(id="current_conditions-summary")

#get details
cur_weather_details = soup.find(id = "current_conditions_detail")

# Extract text from the selected BeautifulSoup objects using .text
cur_weather_conditions = cur_weather_conditions.text
cur_weather_details = cur_weather_details.text

# Final Output
# Return scraped information
print('The Current Weather Conditions in '+ resultCity +  ", " + resultState + " is:" + cur_weather_conditions)
print('More details: ' + cur_weather_details )
