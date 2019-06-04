import folium
#create a map object
#at location=[] field you can place latitude and longitude values of your city.
map= folium.Map(location=[18.5204,73.8567], zoom_start=7)
print(map)

# need html file out of this object - to create/see the map
#look the directory of the map method to  see all method we can apply to map
print(dir(folium.Map))
map.save('test.html')

# go to project file section for the test.html file
#right click and open in browser

#change zoom to 15 and add tiles ='Stamen Terrain' and recreate the html file
map2=folium.Map(location=[18.5204,73.8567], zoom_start=15, tiles='Stamen Terrain')
print(map2)
print(map2.save(test1.html))
