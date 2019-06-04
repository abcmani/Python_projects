import folium as f

#existing standard map object from previous program
map= f.Map(location=[18.5204,73.8567], zoom_start=15, tiles='Stamen terrain')
# we want to add some markers to the map
f.Marker(location=[18.5204,73.8567], icon=f.Icon(icon='cloud'), popup='I am so lost').add_to(map)
f.Marker(location=[18.5404,73.8767], icon=f.Icon(icon='cloud'), popup='But I can see you').add_to(map)
map.save('test.html')
