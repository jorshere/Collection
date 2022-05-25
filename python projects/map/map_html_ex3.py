
import folium
import pandas
 
data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def elv_fun(elevation):
    if elevation <= 1000:
        return "green"
    elif 1000 < elevation <= 3000:
        return "orange"
    else: 
        return "red"
 
html = """<h4>Volcano information:</h4>Height: %s m"""

 
map = folium.Map(location=[38.58, -99.09], zoom_start=5)#,tiles="Stamen Terrain")
fg1 = folium.FeatureGroup(name = "volcanoes")
 
for lt, ln, el in zip(lat, lon, elev):
    iframe = folium.IFrame(html=html % str(el), width=200, height=100)
    #fg.add_child(folium.CircleMarker(location=[lt, ln],radius=6, popup=folium.Popup(iframe),fill_color= elv_fun(el),color= "grey",color_opacity=0.7))
    fg1.add_child(folium.Marker(location=[lt,ln],popup=folium.Popup(iframe),tooltip="click me",icon=folium.Icon(elv_fun(el))))

fg2= folium.FeatureGroup(name="population")

fg2.add_child(folium.GeoJson(data=open('1234.json','r',encoding='utf-8-sig').read(),style_function= lambda x:{'fillColor':'yellow' if x['properties']['POP2005']<10000000
else 'green' if 10000000<= x['properties']["POP2005"] < 20000000
else 'red'}))

map.add_child(fg1)
map.add_child(fg2)
map.add_child(folium.LayerControl())
map.save("Map_html_popup_simple.html")