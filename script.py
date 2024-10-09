import pandas as pd
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

# Load data from CSV file
df = pd.read_csv('query.csv')

# Check if the required columns exist
if 'latitude' not in df.columns or 'longitude' not in df.columns:
    raise ValueError("The CSV file must contain 'latitude' and 'longitude' columns.")

# Function to get country name
def get_country(lat, lon):
    geolocator = Nominatim(user_agent="geoapiExercises")
    try:
        location = geolocator.reverse((lat, lon), exactly_one=True)
        address = location.raw['address']
        return address.get('country', None)
    except (GeocoderTimedOut, AttributeError):
        return None

# Apply function to get country
df['country'] = df.apply(lambda row: get_country(row['latitude'], row['longitude']), axis=1)

# Export results to country.txt file
df[['country']].to_csv('country.txt', index=False, header=False)

# Display confirmation message
print("Countries have been exported to country.txt")

# Display the DataFrame
print(df)