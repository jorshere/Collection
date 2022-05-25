import folium
import pandas

I_map = folium.Map(location=[24,76],zoom_start=5.5, tiles="Stamen Terrain")
fg= folium.FeatureGroup(name="International airport INDIA")

data = pandas.read_csv("india_airport.txt",sep=";")

latitude = list(data["Latitude"])
longitude = list(data["Longitude"])
P_name = list(data["Place Name"])

def mounts(name):
    if "Airport" in str(name):
        return "green"
    else:
        return "blue"

htmls = """ <h3>Airport Info:<h5>%s"""
        


for lt,lg,nm in zip(latitude,longitude,P_name):
    iframes=folium.IFrame(html=htmls % nm, width=200,height=100)
    fg.add_child(folium.Marker(location=[lt,lg],popup=folium.Popup(iframes), icon=folium.Icon(mounts(nm)),tooltip="click me"))

I_map.add_child(fg)
I_map.save("Indian_airport.htm")