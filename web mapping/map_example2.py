import folium
map= folium.Map(location=[22.68,85.62],zoom_start=8,tiles="Stamen Terrain")
fg=folium.FeatureGroup("my_map")
#fg.add_child(folium.Marker(location=[22.682312,85.629048],popup="my home",icon=folium.Icon(color="blue"),tooltip="hover over me")) 
#fg.add_child(folium.Marker(location=[22.672970,85.642615],popup="my school",icon=folium.Icon(color="blue"),tooltip="hover over me")) 




#OR......


for coordinates in [[22.682312,85.629048],[22.672970,85.642615]]:        # to get multiple coordinates;
    fg.add_child(folium.Marker(location=coordinates,popup="my place",icon=folium.Icon(color="blue"),tooltip="hover over me"))

map.add_child(fg)
map.save("maps2.html")