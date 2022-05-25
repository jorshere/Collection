import folium
import pandas


map= folium.Map(location=[38,-99],zoom_start=5,tiles="Stamen Terrain")
fg=folium.FeatureGroup(name="my_map")

data= pandas.read_csv("Volcanoes.txt")
lat= list(data["LAT"])
lon= list(data["LON"])
elv= list(data["ELEV"])

for lt,lg,el in zip(lat,lon,elv):
    fg.add_child(folium.Marker(location=[lt,lg],popup=str(el)+" m",icon=folium.Icon(color="blue"),tooltip="click me")) 
map.add_child(fg)
map.save("map2.html")