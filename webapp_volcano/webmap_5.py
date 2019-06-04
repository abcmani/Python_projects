import folium as f
import pandas as pd

# if we would like to open the map around our area of data.,we can average our data lat and lon
df= pd.read_csv('/content/Volcanoes.txt')

#taking average
latmean =df['LAT'].mean()
lonmean =df['LON'].mean()

map= f.Map(location=[latmean,lonmean], zoom_start=6, tiles='Stamen terrain')

for lat,lon,name,elev in zip(df['LAT'],df['LON'],df['NAME'],df['ELEV']):
#adding the icon color
  f.Marker(location=[lat,lon], popup=name, icon=f.Icon(color=colour(elev), icon='cloud', icon_color='purple')).add_to(map)
map.save('test.html')



def colour(elev):
  if elev in range(0,1000):
    return 'green'
  elif elev in range(1001,2000):
    return 'orange'
  elif elev in range(2001,3000):
    return 'blue'
  else:
    return 'red'
