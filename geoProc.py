import geopandas
import numpy as np
import pandas as pd
from shapely.geometry import Point


worldMap = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))

df = pd.read_csv("geodata/Sample1.csv")
df['coordinates'] = df[['Long', 'Lat']].values.tolist()
df['coordinates'] = df['coordinates'].apply(Point)
dfGeo = geopandas.GeoDataFrame(df, geometry='coordinates')
dfGeo.head()

import folium
from folium import Choropleth, Circle, Marker
from folium.plugins import HeatMap, MarkerCluster

m = worldMap[worldMap['name'].isin(['China','Japan','Malaysia','Philippines'])].explore(
    name="Country"
    #,width=500,height=500
)
folium.LayerControl().add_to(m)
for idx, row in dfGeo.iterrows():
    popTxt="<h2>Site&nbsp;Info&nbsp; </h2><br> Manager: {}<br> Email: {}<br> Local Contact: {}".format(
        row["Manager"],row["Email"],row["Local Contact"])
    
    Marker(location=[row['Lat'], row['Long']],
           tooltip = row["Building Name"], 
           popup = popTxt).add_to(m)

m.save('geodata/map1.html')
