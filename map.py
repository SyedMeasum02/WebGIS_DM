import folium

m = folium.map(location=[30.375320,69.345116], zoom_start=12)

m.save('map.html')
