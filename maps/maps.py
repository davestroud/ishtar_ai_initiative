import folium

# Coordinates for the capitals or significant cities of the Middle East countries, with English names
locations = {
    'Afghanistan': (34.5553, 69.2075),  # Kabul
    'Iraq': (33.3128, 44.3615),         # Baghdad
    'Syria': (33.5138, 36.2765),        # Damascus
    'Yemen': (15.3694, 44.1910),        # Sana'a
    'Somalia': (2.0469, 45.3182),       # Mogadishu
    'Libya': (32.8872, 13.1913),        # Tripoli
    'Saudi Arabia': (24.7136, 46.6753), # Riyadh
    'Iran': (35.6892, 51.3890),         # Tehran
    'Jordan': (31.9566, 35.9457),       # Amman
    'Lebanon': (33.8938, 35.5018),      # Beirut
    'Israel': (31.7683, 35.2137),       # Jerusalem
    'Palestine': (31.9466, 35.3027),    # Ramallah
    'United Arab Emirates': (24.4539, 54.3773),  # Abu Dhabi
    'Qatar': (25.276987, 51.520008),    # Doha
    'Bahrain': (26.2235, 50.5876),      # Manama
    'Kuwait': (29.3759, 47.9774),       # Kuwait City
    'Oman': (23.5859, 58.4059),         # Muscat
    'Egypt': (30.0444, 31.2357),        # Cairo
    'Turkey': (39.9334, 32.8597),       # Ankara
    'Cyprus': (35.1856, 33.3823)        # Nicosia
}

# Create a map centered around the Middle East
middle_east_map = folium.Map(location=[29.2985, 42.5510], zoom_start=5)

# Add markers for each country with the country name in English
for country, coords in locations.items():
    folium.Marker(location=coords, popup=f'{country}', tooltip=country).add_to(middle_east_map)

# Define the save path (adjust this path according to your local environment)
save_path = "/home/sagemaker-user/ishtar_ai_initiative/maps/middle_east_map.html"

# Save the map to the specified path
middle_east_map.save(save_path)

# Print completion message
print(f"Map saved to {save_path}")
