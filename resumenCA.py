import requests
import json
import numpy as np  # Added NumPy import
from datetime import datetime, timedelta

def analyze_environment(ibero1):
    today = datetime.today()
    year_month_day = today.strftime("%Y%m%d")
    year = int(year_month_day[:4])
    month = int(year_month_day[4:6])
    day = int(year_month_day[6:8])

    one_week_ago = today - timedelta(days=1)
    year_month_day1 = one_week_ago.strftime('%Y%m%d')
    year1 = int(year_month_day1[0:4])
    month1 = int(year_month_day1[4:6])
    day1 = int(year_month_day1[6:8])

    start_time = datetime(year1, month1, day1, 13, 0, 0)
    end_time = datetime(year, month, day, 13, 0, 0)
    url = 'http://smability.sidtecmx.com/SmabilityAPI/GetData?'

    def analyze_sensor(idSensor):
        query = {'dtStart': start_time, 'dtEnd': end_time, 'token': ibero1, 'idSensor': idSensor}
        response = requests.get(url, params=query)
        y = json.dumps(response.json())
        sensor_list = json.loads(y)
        data = [float(x["Data"]) for x in sensor_list]
        num_days = end_time.toordinal() - start_time.toordinal() + 1
        avg_per_day = np.zeros(num_days)
        for n in range(num_days):
            start = n * 288
            end = (n + 1) * 288
            avg_per_day[n] = np.mean(data[start:end])
        return avg_per_day[-1]

    pm25 = analyze_sensor('9')  # P.M. 2.5
    pm10 = analyze_sensor('8')  # P.M. 10
    ozone = analyze_sensor('7')  # Ozono
    co = analyze_sensor('2')  # CO
    temperature = analyze_sensor('12')  # Temperatura
    humidity = analyze_sensor('3')  # Humedad

    # Calculate evaluation scores for each parameter
    pm25eval = evaluate_pm25(pm25)
    pm10eval = evaluate_pm10(pm10)
    ozonoeval = evaluate_ozone(ozone)
    coeval = evaluate_co(co)
    temperaturaeval = evaluate_temperature(temperature)
    humedadeval = evaluate_humidity(humidity)

    # Calculate total score and corresponding quality
    total = pm25eval + pm10eval + ozonoeval + coeval + temperaturaeval + humedadeval
    calidadA = calculate_quality(total)

    return calidadA

def evaluate_pm25(pm25):
    if pm25 < 12:
        return 1  # Bueno
    elif 12 <= pm25 <= 35.4:
        return 2  # Moderado
    elif 35.5 <= pm25 <= 55.4:
        return 3  # Insalubre para grupos sensibles
    else:
        return 4  # Insalubre para todos

def evaluate_pm10(pm10):
    if pm10 < 54:
        return 1  # Bueno
    elif 54 <= pm10 <= 154:
        return 2  # Moderado
    elif 155 <= pm10 <= 254:
        return 3  # Insalubre para grupos sensibles
    else:
        return 4  # Insalubre para todos

def evaluate_ozone(ozone):
    if ozone < 50:
        return 1  # Bueno
    elif 50 <= ozone <= 100:
        return 2  # Moderado
    elif 101 <= ozone <= 168:
        return 3  # Insalubre para grupos sensibles
    else:
        return 4  # Insalubre para todos

def evaluate_co(co):
    if co < 400:
        return 1  # Bueno
    elif 400 <= co <= 1000:
        return 2  # Moderado
    elif 1001 <= co <= 2000:
        return 3  # Insalubre para grupos sensibles
    else:
        return 4  # Insalubre para todos

def evaluate_temperature(temperature):
    if 20 <= temperature <= 25:
        return 1
    elif temperature > 25:
        return 2
    else:
        return 3

def evaluate_humidity(humidity):
    if 30 <= humidity <= 60:
        return 1
    else:
        return 2

def calculate_quality(total):
    if total < 11:
        return 'Resumen del día: Calidad buena 😀.'
    elif 11 <= total < 16:
        return 'Resumen del día: Calidad regular 😐.'
    else:
        return 'Resumen del día: Calidad mala 🙁.'

