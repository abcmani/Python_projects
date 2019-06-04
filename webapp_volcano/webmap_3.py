import folium as f
import pandas as pd


#Original map as it is
map= f.Map(location=[18.5204,73.8567], zoom_start=15, tiles='Stamen terrain')
#read the file and store in a  variable
df= pd.read_csv('/content/Volcanoes.txt')

#create a for loop to use the file data to  create markers
#useda zip finction since we have multiple iterators
for lat,lon,name in zip(df['LAT'],df['LON'],df['NAME']):
  f.Marker(location=[lat,lon], popup=name, icon=f.Icon(icon='cloud')).add_to(map)
map.save('test.html')
