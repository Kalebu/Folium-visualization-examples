import folium
import base64
from folium import IFrame

description = '<p><b><a href = "https://en.wikipedia.org/wiki/Dar_es_Salaam"> Dar-es-Salaam</a></b> is the largest city and former capital of Tanzania. With over six million people, it is the largest city in East Africa and the fifth-largest in Africa.</p>'


def get_popup_image(path_to_img: str, resolution=1, height=400, width=500):
    with open(path_to_img, 'rb') as img:
        pop_img = base64.b64encode(img.read()).decode('utf-8')
        html_img = '<div><img src="data:image/png;base64,{}">{}</div>'.format(
            pop_img, description)
        iframe = IFrame(html_img, width=(width*resolution) +
                        20, height=(height*resolution)+20)
        popup = folium.Popup(iframe, max_width=2650)
        return popup


popup_img = get_popup_image('ubungo-interchange.jpg')
dar_cordinates = [-6.776012, 39.178326]
dar_map = folium.Map(location=[-6.3728253, 34.8924826], zoom_start=7)
folium.CircleMarker(location=[*dar_cordinates], radius=10, popup=popup_img,
                    color='#3186cc', fill=True, fill_color='#3186cc').add_to(dar_map)
dar_map.save('index.html')

print("Map Saved")
