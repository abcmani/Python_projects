import folium as f
import pandas as pd


map= f.Map(location=[18.5204,73.8567], zoom_start=15, tiles='Stamen terrain')

'''df= pd.read_csv('/content/Volcanoes.txt')
# added elev iterator in for loop for iteration
for lat,lon,name,elev in zip(df['LAT'],df['LON'],df['NAME'],df['ELEV']):
#we want to segregate  and color code as  per the elevation of volcano., used one liner if statement
  f.Marker(location=[lat,lon], popup=name, icon=f.Icon(icon='cloud',color='green' if elev in range(0,1000) else 'orange' if elev in range(1001,2000) else 'blue' if elev in range(2001,3000) else 'red')).add_to(map)
map.save('test.html')'''


# added elev iterator in for loop for iteration
for lat,lon,name,elev in zip(df['LAT'],df['LON'],df['NAME'],df['ELEV']):
# we want to segregate  and color code as  per the elevation of volcano.,
  f.Marker(location=[lat,lon], popup=name, icon=f.Icon(icon='cloud',color=colour(elev))).add_to(map)
map.save('test.html')

#more organized code
def colour(elev):
  if elev in range(0,1000):
    return 'green'
  elif elev in range(1001,2000):
    return 'orange'
  elif elev in range(2001,3000):
    return 'blue'
  else:
    return 'red'
