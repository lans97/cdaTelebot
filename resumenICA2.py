import time
from datetime import datetime
import requests
import json
from googletrans import Translator
from io import BytesIO
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib as mpl

def categoria_aire_f(ibero1):
    today = datetime.today()
    year_month_day = today.strftime("%Y%m%d")
    year = int(year_month_day[:4])
    month = int(year_month_day[4:6])
    day = int(year_month_day[6:8])

    start_time = datetime(year, month, day, 13, 0, 0)
    end_time = datetime(year, month, day, 13, 0, 0)
    url = 'http://smability.sidtecmx.com/SmabilityAPI/GetData?'

    query = {'dtStart': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
             'dtEnd': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
             'token': ibero1,
             'idSensor': '1001'}
    response = requests.get(url, params=query)
    data = response.json()

    json_data = data[0]["Data"]
    data_dict = json.loads(json_data)
    descrip = data_dict["Description"]
    descrip = str(descrip)

    translator = Translator()
    translated_descrip = translator.translate(descrip, dest='es').text

    colores = data_dict["Color"]
    colores = str(colores)

    if colores == '00E400':
        combined_info = f"🟩 Categoría: Buena. {translated_descrip} "
        value_to_annotate = 25
    elif colores == "#00E400":
        combined_info = f"🟨 Categoría: Moderada. {translated_descrip} "
        value_to_annotate = 75
    elif colores == "#FF7E00":
        combined_info = f"🟧 Categoría: Insalubre para grupos sensibles. {translated_descrip} "
        value_to_annotate = 120
    elif colores == "#FF0000":
        combined_info = f"🟥 Categoría: Insalubre. {translated_descrip} "
        value_to_annotate = 175
    elif colores == "#8F3F97":
        combined_info = f"🟪 Categoría: Muy insalubre. {translated_descrip} "
        value_to_annotate = 250
    elif colores == "#7E0023":
        combined_info = f"⚠️ Categoría: Peligroso. {translated_descrip} "
        value_to_annotate = 400

    tweet_text = f"{start_time} {combined_info}"

    mpl.rcParams['text.color'] = 'white'

    translated_descrip_jump = insert_line_breaks(combined_info)

    fig = plt.figure(figsize=(8, 2), facecolor='black')
    ax2 = fig.add_axes([0.05, 0.8, 0.9, 0.15])

    cmap = mpl.colors.ListedColormap(['#00E400', '#FFFF00', '#FF7E00', '#FF0000', '#8F3F97', '#7E0023'])
    bounds = [0, 50, 100, 150, 200, 300, 500]
    norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
    cb2 = mpl.colorbar.ColorbarBase(ax2, cmap=cmap,
                                    norm=norm,
                                    spacing='proportional',
                                    orientation='horizontal')

    texto = f"AQI del {start_time}"
    r = texto.rjust(20)

    plt.title('AQI', fontsize=25, fontweight='bold', fontfamily='sans-serif')

    ax2.spines['bottom'].set_color('white')
    ax2.spines['left'].set_color('white')
    ax2.tick_params(axis='both', colors='white')

    cb2.set_label(f'{translated_descrip_jump}', fontsize=15, fontfamily='sans-serif', color='white')

    ax2.annotate(f'AQI: {value_to_annotate}', xy=(value_to_annotate, 0), xytext=(value_to_annotate, 2), color='black',
                 arrowprops=dict(facecolor='black', arrowstyle='->', connectionstyle="arc3,rad=.5"))

    plt.savefig('output_image.png', format='png')  # Save the image
    plt.show()

    return tweet_text, 'output_image.png'


def insert_line_breaks(text, line_length=60):
    lines = []
    for i in range(0, len(text), line_length):
        lines.append(text[i:i + line_length])
    return '\n'.join(lines)
