import folium
from jinja2 import Template
import base64

from DBClient import DBClient


db_client = DBClient('arh_map', 'map_user', 'mapper', 'localhost')

map = folium.Map(location=(64.54397606229037, 40.510735463353384), zoom_start=18,)

# folium.Marker(
#     location=[45.3288, -121.6625],
#     tooltip="Click me!",
#     popup="Mt. Hood Meadows",
#     icon=folium.Icon(icon="cloud"),
# ).add_to(m)

# encoded = base64.b64encode(open(f'../media/{i["img"]}', 'rb').read())
# html = ('<img src="data:image/png;base64,{}" style="width: 70px; height: 70px; border-radius: 30px">'
#         '<a href="/{{ url }}/">{{ name }}</a>').format
# iframe = IFrame(html(encoded.decode('UTF-8')), width=100, height=100)
# template = folium.Popup(iframe, max_width=140,)

if __name__ == '__main__':
    db_client.connect()
    data = db_client.get_coords()
    for i in data:
        encoded = base64.b64encode(open(f'../media/{i["img"]}', 'rb').read())
        html = ('<img src="data:image/png;base64,{}" style="width: 70px; height: 70px; border-radius: 30px">'
                '<a href="/{{ url }}/">{{ name }}</a>').format
        temp = Template(html).render(name=i['name'], url=i['url'])
        template = folium.Popup(temp, max_width=140)
        if i['category'] == 1:
            folium.Marker(
                location=i['coords'],
                popup=template,
                tooltip=i["addr"],
                icon=folium.Icon(color="green")
            ).add_to(map)
        if i['category'] == 2:
            folium.Marker(
                location=i['coords'],
                popup=template,
                tooltip=i["addr"],
                icon=folium.Icon(color="orange")
            ).add_to(map)
        if i['category'] == 3:
            folium.Marker(
                location=i['coords'],
                popup=template,
                tooltip=i["addr"],
                icon=folium.Icon(color="blue")
            ).add_to(map)
        if i['category'] == 4:
            folium.Marker(
                location=i['coords'],
                popup=template,
                tooltip=i["addr"],
                icon=folium.Icon(color="gray")
            ).add_to(map)
        if i['category'] == 5:
            folium.Marker(
                location=i['coords'],
                popup=template,
                tooltip=i["addr"],
                icon=folium.Icon(color="purple")
            ).add_to(map)

    map.save('../templates/map_app/map_test.html')
    db_client.shutdown()