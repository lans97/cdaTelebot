from resumenCA import analyze_environment
from datoGraph import generar_grafica
from resumenICA2 import categoria_aire_f

# Importar bibliotecas
import telebot
from telebot import types
from io import BytesIO
from PIL import Image
from io import BytesIO

#Musica
import pygame
import time
import threading


# Inicializar constantes
bot = telebot.TeleBot('6952197771:AAHmQkQHOp-H7OhzH9667gF-SWZue742MD4')
equipo = 'b8c1bac206b358bde62cb25c374339c3' # Centro de datos
equipo2 = '349b1230277f1c67577e4f5bee6ba486' # Estación meteorológica

pm25 = '9'  # P.M. 2.5
pm10 = '8'  # P.M. 10
ozono = '7'  # Ozono
co = '2'  # CO
temperatura = '12'  # Temperatura
humedad = '3'

# - - - - - - - Definición de objetos - - - - - - -

# Definición de botones del menú principal
boton1 = types.KeyboardButton('🩺 Calidad del aire')
boton2 = types.KeyboardButton('🌎 Estación meteorológica')
boton3 = types.KeyboardButton('🎧 ¿Quiénes somos?')

# Definición de botones del menú "Calidad del aire"
boton4 = types.KeyboardButton('📚 Resumen')
boton5 = types.KeyboardButton('🚦 Categoria ICA')
boton6 = types.KeyboardButton('🚦 Contaminantes')

# Definición de botones de la estación meteorológica
boton7 = types.KeyboardButton('🌡 Temperatura')
boton8 = types.KeyboardButton('💧 Lluvia')
boton9 = types.KeyboardButton('💧 Viento')
boton10 = types.KeyboardButton('🛡️ Radiación')

# Definición de botones de la calidad (contaminantes)
boton11 = types.KeyboardButton('😤 PM 2.5')
boton12 = types.KeyboardButton('🧹 PM 10')
boton13 = types.KeyboardButton('🛡️ Ozono')
boton14 = types.KeyboardButton('🧯 Monóxido de carbono')

# Definición de botones del menú de "Temperatura"
boton15 = types.KeyboardButton('🌇 Hoy')
boton16 = types.KeyboardButton('🌃 Semanal')

# Definición de botones del menú de "Lluvia"
boton17 = types.KeyboardButton('🚿 Hoy')
boton18 = types.KeyboardButton('🌊 Semanal')

# Definición de botones del menú de "Viento"
boton19 = types.KeyboardButton('RV Hoy')
boton20 = types.KeyboardButton('RV Semanal')

# Definición de botones del menú de "Radiación"
boton21 = types.KeyboardButton('Ra Hoy')
boton22 = types.KeyboardButton('Ra Semanal')

# Definición de botones del menú de "PM 2.5"
boton23 = types.KeyboardButton('🕒 Hoy')
boton24 = types.KeyboardButton('📅 Semanal')

# Definición de botones del menú de "PM 10"
boton25 = types.KeyboardButton('😤 Hoy')
boton26 = types.KeyboardButton('🧹 Semanal')

# Definición de botones del menú de "Ozono"
boton27 = types.KeyboardButton('🕕 Hoy')
boton28 = types.KeyboardButton('🕡 Semanal')

# Definición de botones del menú de "Monoxido de carbono"
boton29 = types.KeyboardButton('🛵 Hoy')
boton30 = types.KeyboardButton('✈️ Semanal')

# Definición de botones del menú de "🎧"
boton31 = types.KeyboardButton('🎧 Reproducir Audio')
boton32 = types.KeyboardButton('⏹ Detener Audio')

# Definición de regreso al menu inicial
boton33 = types.KeyboardButton('Menú inicial 🏠')

# Creación del menu principal
menu_principal_inter = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
menu_principal_inter.add(boton1, boton2, boton3)

# Creación del menú secundario "Calidad del aire"
submenu_calidad_inter = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
submenu_calidad_inter.add(boton4, boton5, boton6, boton33)

# Creación del menú secundario "Estación meteorológica"
submenu_estacion_inter = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
submenu_estacion_inter.add(boton7, boton8, boton9, boton10, boton33)

# Creación del menú secundario "Estación meteorológica (Contaminantes)"
submenu_conta_inter = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
submenu_conta_inter.add(boton11, boton12, boton13, boton14, boton33)

# Creación del menú secundario "Temperatura"
submenu_tempe_inter = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
submenu_tempe_inter.add(boton15, boton16, boton33)

# Creación del menú secundario "Lluvia"
submenu_lluvia_inter = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
submenu_lluvia_inter.add(boton17, boton18, boton33)

# Creación del menú secundario "Viento"
submenu_viento_inter = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
submenu_viento_inter.add(boton19, boton20, boton33)

# Creación del menú secundario "Radiación"
submenu_viento_inter = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
submenu_viento_inter.add(boton21, boton22, boton33)

# Creación del menú secundario "PM2.5"
submenu_pm25_inter = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
submenu_pm25_inter.add(boton23, boton24, boton33)

# Creación del menú secundario "PM10"
submenu_pm10_inter = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
submenu_pm10_inter.add(boton25, boton26, boton33)

# Creación del menú secundario "O2"
submenu_o2_inter = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
submenu_o2_inter.add(boton27, boton28, boton33)

# Creación del menú secundario "CO"
submenu_co_inter = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
submenu_co_inter.add(boton29, boton30, boton33)

# Creación del menú secundario "🎧"
submenu_music_inter = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
submenu_music_inter.add(boton31, boton32, boton33)

# - - - - - - - Definición de Interfaces - - - - - - -

# Inicio de la interfaz principal
@bot.message_handler(commands=['start'])
def send_main_menu(message):
    bot.reply_to(message, '🐺 ¡Hola! Soy tu asistente meteorológico de la Universidad Iberoamericana. Mi objetivo es brindarte información detallada sobre el clima y el tiempo en nuestro campus y sus alrededores. Desde pronósticos diarios hasta datos climáticos históricos, estoy aquí para mantenerte informado y ayudarte a planificar tu día de manera eficiente. ¡Bienvenido y disfruta de la precisión meteorológica a tu alcance!')
    bot.send_message(message.chat.id, 'Este es el menú principal, selecciona con un boton aquello que deseas conocer:', reply_markup=menu_principal_inter)

# Definición de submenu "Calidad del aire"
@bot.message_handler(func=lambda message: message.text == '🩺 Calidad del aire')
def send_submenu_r(message):
    bot.send_message(message.chat.id, '¿Qué deseas conocer? 🪁.', reply_markup=submenu_calidad_inter)

# Definición de submenu "Estacion Mete"
@bot.message_handler(func=lambda message: message.text == '🌎 Estación meteorológica')
def send_submenu_o(message):
    bot.send_message(message.chat.id, '¿Qué dato es de tu interés? 🌎', reply_markup=submenu_estacion_inter)

# Definición de submenu "Contaminantes"
@bot.message_handler(func=lambda message: message.text == '🚦 Contaminantes')
def send_submenu_o(message):
    bot.send_message(message.chat.id, '¿Qué dato es de tu interés? ', reply_markup=submenu_conta_inter)

# Definición de submenu "Temperatura"
@bot.message_handler(func=lambda message: message.text == '🌡 Temperatura')
def send_submenu_t(message):
    bot.send_message(message.chat.id, '¿Qué rango te gustaría analizar? 🌡', reply_markup=submenu_tempe_inter)

# Definición de submenu "Humedad"
@bot.message_handler(func=lambda message: message.text == '💧 Lluvia')
def send_submenu_t(message):
    bot.send_message(message.chat.id, '¿Qué rango te gustaría analizar?', reply_markup=submenu_lluvia_inter)

# Definición de submenu "PM25"
@bot.message_handler(func=lambda message: message.text == '😤 PM 2.5')
def send_submenu_t(message):
    bot.send_message(message.chat.id, '¿Qué rango te gustaría analizar?', reply_markup=submenu_pm25_inter)

# Definición de submenu "PM10"
@bot.message_handler(func=lambda message: message.text == '🧹 PM 10')
def send_submenu_t(message):
    bot.send_message(message.chat.id, '¿Qué rango te gustaría analizar?', reply_markup=submenu_pm10_inter)

# Definición de submenu "Ozono"
@bot.message_handler(func=lambda message: message.text == '🛡️ Ozono')
def send_submenu_t(message):
    bot.send_message(message.chat.id, '¿Qué rango te gustaría analizar?', reply_markup=submenu_o2_inter)

# Definición de submenu "CO"
@bot.message_handler(func=lambda message: message.text == '🧯 Monóxido de carbono')
def send_submenu_t(message):
    bot.send_message(message.chat.id, '¿Qué rango te gustaría analizar?', reply_markup=submenu_co_inter)

# Definición de submenu "Resumen"
@bot.message_handler(func=lambda message: message.text == 'Menú inicial 🏠')
def send_hogar(message):
    bot.send_message(message.chat.id, '¿Qué te apetece conocer? 🔮', reply_markup=menu_principal_inter)

# Definición de submenu "Musica"
@bot.message_handler(func=lambda message: message.text == '🎧 ¿Quiénes somos?')
def send_musicc(message):
    bot.send_message(message.chat.id, '📻',reply_markup=submenu_music_inter)

# - - - - - - - Definición de controladores - - - - - - -

# Actividad Resumen
@bot.message_handler(func=lambda message: message.text == '📚 Resumen')
def boton4_controlador(message):
    chat_id = message.chat.id
    mensaje_pin_id = enviar_pin(chat_id)
    result = analyze_environment(equipo)
    bot.reply_to(message, result)
    quitar_pin(chat_id, mensaje_pin_id)

# Actividad ICA
@bot.message_handler(func=lambda message: message.text == '🚦 Categoria ICA')
def boton5_controlador(message):
    chat_id = message.chat.id
    mensaje_pin_id = enviar_pin(chat_id)
    dato, image = categoria_aire_f(equipo2)
    # Trabajar la imagen
    #img_buffer = BytesIO(image)
    #img_buffer.seek(0)
    bot.send_photo(message.chat.id, photo="/home/raspberry1/TelegramProyecto/output_image.png")
    
    # Se envía el valor máximo
    bot.send_message(message.chat.id, )
    quitar_pin(chat_id, mensaje_pin_id)

# Actividad Temperatura Hoy
@bot.message_handler(func=lambda message: message.text == '🌇 Hoy')
def boton12_controlador(message):
    chat_id = message.chat.id
    mensaje_pin_id = enviar_pin(chat_id)
    # Función para graficar
    image, max_value = generar_grafica(equipo, temperatura, 1)
    # Trabajar la imagen
    img_buffer = BytesIO(image)
    img_buffer.seek(0)
    bot.send_photo(message.chat.id, photo=img_buffer)

    # Se envía el valor máximo
    bot.send_message(message.chat.id, f"Temperatura más alta: {max_value} °C")
    quitar_pin(chat_id, mensaje_pin_id)

# Actividad Temperatura Semanal
@bot.message_handler(func=lambda message: message.text == '🌃 Semanal')
def boton13_controlador(message):
    chat_id = message.chat.id
    mensaje_pin_id = enviar_pin(chat_id)
    # Función para graficar
    image, max_value = generar_grafica(equipo, temperatura, 7)
    # Trabajar la imagen
    img_buffer = BytesIO(image)
    img_buffer.seek(0)
    bot.send_photo(message.chat.id, photo=img_buffer)

    # Se envía el valor máximo
    bot.send_message(message.chat.id, f"Temperatura más alta: {max_value} °C")
    quitar_pin(chat_id, mensaje_pin_id)

# Actividad Humedad Hoy
@bot.message_handler(func=lambda message: message.text == '🚿 Hoy')
def boton14_controlador(message):
    chat_id = message.chat.id
    mensaje_pin_id = enviar_pin(chat_id)
    # Función para graficar
    image, max_value = generar_grafica(equipo, humedad, 1)
    # Trabajar la imagen
    img_buffer = BytesIO(image)
    img_buffer.seek(0)
    bot.send_photo(message.chat.id, photo=img_buffer)

    # Se envía el valor máximo
    bot.send_message(message.chat.id, f"Valor más alto: {max_value}%")
    quitar_pin(chat_id, mensaje_pin_id)

# Actividad Humedad Semanal
@bot.message_handler(func=lambda message: message.text == '🌊 Semanal')
def boton15_controlador7(message):
    chat_id = message.chat.id
    mensaje_pin_id = enviar_pin(chat_id)
    # Función para graficar
    image, max_value = generar_grafica(equipo, humedad, 7)
    # Trabajar la imagen
    img_buffer = BytesIO(image)
    img_buffer.seek(0)
    bot.send_photo(message.chat.id, photo=img_buffer)

    # Se envía el valor máximo
    bot.send_message(message.chat.id, f"Valor más alto: {max_value}%")
    quitar_pin(chat_id, mensaje_pin_id)

# Actividad PM2.5 Hoy
@bot.message_handler(func=lambda message: message.text == '🕒 Hoy')
def boton16_controlador(message):
    chat_id = message.chat.id
    mensaje_pin_id = enviar_pin(chat_id)
    # Función para graficar
    image, max_value = generar_grafica(equipo, pm25, 1)
    # Trabajar la imagen
    img_buffer = BytesIO(image)
    img_buffer.seek(0)
    bot.send_photo(message.chat.id, photo=img_buffer)

    # Se envía el valor máximo
    bot.send_message(message.chat.id, f"Valor más alto: {max_value} ug/m3")
    quitar_pin(chat_id, mensaje_pin_id)

# Actividad PM25 Semanal
@bot.message_handler(func=lambda message: message.text == '📅 Semanal')
def boton17_controlador7(message):
    chat_id = message.chat.id
    mensaje_pin_id = enviar_pin(chat_id)
    # Función para graficar
    image, max_value = generar_grafica(equipo, pm25, 7)
    # Trabajar la imagen
    img_buffer = BytesIO(image)
    img_buffer.seek(0)
    bot.send_photo(message.chat.id, photo=img_buffer)

    # Se envía el valor máximo
    bot.send_message(message.chat.id, f"Valor más alto: {max_value} ug/m3")
    quitar_pin(chat_id, mensaje_pin_id)

# Actividad PM10 Hoy
@bot.message_handler(func=lambda message: message.text == '😤 Hoy')
def boton18_controlador(message):
    chat_id = message.chat.id
    mensaje_pin_id = enviar_pin(chat_id)
    # Función para graficar
    image, max_value = generar_grafica(equipo, pm10, 1)
    # Trabajar la imagen
    img_buffer = BytesIO(image)
    img_buffer.seek(0)
    bot.send_photo(message.chat.id, photo=img_buffer)

    # Se envía el valor máximo
    bot.send_message(message.chat.id, f"Valor más alto: {max_value} ug/m3")
    quitar_pin(chat_id, mensaje_pin_id)

# Actividad PM10 Semanal
@bot.message_handler(func=lambda message: message.text == '🧹 Semanal')
def boton19_controlador7(message):
    chat_id = message.chat.id
    mensaje_pin_id = enviar_pin(chat_id)
    # Función para graficar
    image, max_value = generar_grafica(equipo, pm10, 7)
    # Trabajar la imagen
    img_buffer = BytesIO(image)
    img_buffer.seek(0)
    bot.send_photo(message.chat.id, photo=img_buffer)

    # Se envía el valor máximo
    bot.send_message(message.chat.id, f"Valor más alto: {max_value} ug/m3")
    quitar_pin(chat_id, mensaje_pin_id)

# Actividad O2 Hoy
@bot.message_handler(func=lambda message: message.text == '🕕 Hoy')
def boton14_controlador(message):
    chat_id = message.chat.id
    mensaje_pin_id = enviar_pin(chat_id)
    # Función para graficar
    image, max_value = generar_grafica(equipo, ozono, 1)
    # Trabajar la imagen
    img_buffer = BytesIO(image)
    img_buffer.seek(0)
    bot.send_photo(message.chat.id, photo=img_buffer)

    # Se envía el valor máximo
    bot.send_message(message.chat.id, f"Valor más alto: {max_value} ppb")
    quitar_pin(chat_id, mensaje_pin_id)

# Actividad O2 Semanal
@bot.message_handler(func=lambda message: message.text == '🕡 Semanal')
def boton15_controlador7(message):
    chat_id = message.chat.id
    mensaje_pin_id = enviar_pin(chat_id)
    # Función para graficar
    image, max_value = generar_grafica(equipo, ozono, 7)
    # Trabajar la imagen
    img_buffer = BytesIO(image)
    img_buffer.seek(0)
    bot.send_photo(message.chat.id, photo=img_buffer)

    # Se envía el valor máximo
    bot.send_message(message.chat.id, f"Valor más alto: {max_value} ppb")
    quitar_pin(chat_id, mensaje_pin_id)

# Actividad CO Hoy
@bot.message_handler(func=lambda message: message.text == '🛵 Hoy')
def boton16_controlador(message):
    chat_id = message.chat.id
    mensaje_pin_id = enviar_pin(chat_id)
    # Función para graficar
    image, max_value = generar_grafica(equipo, co, 1)
    # Trabajar la imagen
    img_buffer = BytesIO(image)
    img_buffer.seek(0)
    bot.send_photo(message.chat.id, photo=img_buffer)

    # Se envía el valor máximo
    bot.send_message(message.chat.id, f"Valor más alto: {max_value} ppb")
    quitar_pin(chat_id, mensaje_pin_id)

# Actividad CO Semanal
@bot.message_handler(func=lambda message: message.text == '✈️ Semanal')
def boton17_controlador7(message):
    chat_id = message.chat.id
    mensaje_pin_id = enviar_pin(chat_id)
    # Función para graficar
    image, max_value = generar_grafica(equipo, co, 7)
    # Trabajar la imagen
    img_buffer = BytesIO(image)
    img_buffer.seek(0)
    bot.send_photo(message.chat.id, photo=img_buffer)

    # Se envía el valor máximo
    bot.send_message(message.chat.id, f"Valor más alto: {max_value} ppb")
    quitar_pin(chat_id, mensaje_pin_id)

# Actividad musica loop
@bot.message_handler(func=lambda message: message.text == '🎧 Reproducir Música')
def play_music(message):
    #play_obj = wave_obj.play()
    bot.send_message(message.chat.id, "🎵 Reproduciendo música...")

# Actividad detener musica
@bot.message_handler(func=lambda message: message.text == '⏹ Detener Música')
def stop_music(message):
    #mixer.music.stop()  # Stop playing the music
    bot.send_message(message.chat.id, "⏹ Música detenida")

# Actividad Opciones
@bot.message_handler(func=lambda message: True, content_types=['text'])
def handle_force_reply(message):
    #bot.send_message(message.chat.id, "⚙ Una disculpa, actualmente estanis trabajando en actualizaciones, pero selecciona una de las opciones del menú.")
    bot.send_message(message.chat.id, "🐺 Disculpa, actualmente no puedo generar una respuesta para tu solicitud. Sin embargo, puedo ayudarte con las opciones disponibles en este menú.", reply_markup=menu_principal_inter)

# Actividad Mensaje 'Computando'
def enviar_pin(chat_id):
    message_text = "🤖🧮 Computando ..."
    message = bot.send_message(chat_id=chat_id, text=message_text)
    bot.pin_chat_message(chat_id=chat_id, message_id=message.message_id)
    return message.message_id

# Desmarcar la funcion de 'Computar'
def quitar_pin(chat_id, message_id):
    bot.unpin_chat_message(chat_id=chat_id, message_id=message_id)

# Start the bot
bot.polling()
