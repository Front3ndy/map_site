import folium
from jinja2 import Template

from DBClient import DBClient


db_client = DBClient('arh_map', 'map_user', 'mapper', 'localhost')

map = folium.Map(location=(64.54397606229037, 40.510735463353384), zoom_start=13)

# folium.Marker(
#     location=[45.3288, -121.6625],
#     tooltip="Click me!",
#     popup="Mt. Hood Meadows",
#     icon=folium.Icon(icon="cloud"),
# ).add_to(m)

if __name__ == '__main__':
    db_client.connect()
    data = db_client.get_coords()
    for i in data:
        html = """ 
         <img src="{{ img }}" class="cover" 
         style="height: 100%; width:100%; object-fit:cover">
         <a href="/">{{ name }}</a>
         """
        template = Template(html).render(name=i['name'], img=i['img'])
        folium.Marker(
            location=i['coords'],
            popup=template,
            tooltip=i["addr"],
            icon=folium.Icon(color='green')
        ).add_to(map)
    map.save('C:/Users/Vadim/PycharmProjects/site_for_hack/site_for_hack/static/templates/map.html')
    db_client.shutdown()