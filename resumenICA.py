import time
from datetime import datetime
import requests
import json
from googletrans import Translator

def categoria_aire_f(ibero1):
    today = datetime.today()
    year_month_day = today.strftime("%Y%m%d")
    year = int(year_month_day[:4])
    month = int(year_month_day[4:6])
    day = int(year_month_day[6:8])

    start_time = datetime(year, month, day, 13, 0, 0)
    end_time = datetime(year, month, day, 13, 0, 0)
    url = 'http://smability.sidtecmx.com/SmabilityAPI/GetData?'

    query = {'dtStart': start_time, 'dtEnd': start_time, 'token': ibero1, 'idSensor': '1001'}
    response = requests.get(url, params=query)
    data = response.json()

    json_data = data[0]["Data"]

    data_dict = json.loads(json_data)
    
    descrip = data_dict["Description"]

    descrip = str(descrip)
    
    # Translate the description to Spanish
    translator = Translator()
    translated_descrip = translator.translate(descrip, dest='es').text

    colores = data_dict["Color"]
    colores = str(colores)

    if colores == '00E400':
        combined_info = f"🟩 Categoría: Buena. {translated_descrip} "
    elif colores == "#00E400":
        combined_info = f"🟨 Categoría: Moderada. {translated_descrip} "
    elif colores == "#FF7E00":
        combined_info = f"🟧 Categoría: Insalubre para grupos sensibles. {translated_descrip} "
    elif colores == "#FF0000":
        combined_info = f"🟥 Categoría: Insalubre. {translated_descrip} "
    elif colores == "#8F3F97":
        combined_info = f"🟪 Categoría: Muy insalubre. {translated_descrip} "
    elif colores == "#7E0023":
        combined_info = f"⚠️ Categoría: Peligroso. {translated_descrip} "

    tweet_text = f"{start_time} {combined_info}"

    return tweet_text


