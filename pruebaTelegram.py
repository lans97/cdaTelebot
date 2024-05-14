import telebot
from telebot import types
from resumenAmbiental import analyze_environment
from CategoriaHoy import analyze_air_quality
from reporteOzono import generar_report_ozono_diario, generar_report_ozono_semana 
from reporteTemperatura import generar_report_temperatura_diario, generar_report_temperatura_semana 

ibero1 = '349b1230277f1c67577e4f5bee6ba486'
sensor1 = '7' 
sensor2 = '12' 

#Conexión con Telegram
TOKEN = '6952197771:AAHmQkQHOp-H7OhzH9667gF-SWZue742MD4'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    text = ('🐺 Hola, soy tu asistente para tener información del tiempo y clima. Mi tarea es proporcionarte información sobre todos los aspectos que enfocan el ambiente en la Universidad Iberoamericana.\n\n'
    'Los comandos con los cuales haces solicitudes son los siguientes:\n\n'
    '/help - Te muestra la lista de comandos 📖.\n'
    '/temperatura - Te muestra información sobre la temperatura 🌡️. \n'
    '/ozono - Te muestra la información sobre la calidad del ozono 🌎.\n'
    '/resumen - Te mostrará un resumen sobre la calidad del aire 🌫.')
    bot.reply_to(message, text)
    send

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, 'Recuerda abrir el menú para conocer más comandos')

#Hacer llamada de temperatura - - - - - - - - - - - - - - -
@bot.message_handler(commands=['temperatura'])
def send_temperatura(message):
    markup = types.InlineKeyboardMarkup(row_width=2)

    # Creación de los botones
    btn_temp_dia = types.InlineKeyboardButton('Hoy', callback_data='temp_hoy')
    btn_temp_semana = types.InlineKeyboardButton('Semana', callback_data='temp_semana')

    # Agrega botones al Markup
    markup.add(btn_temp_dia, btn_temp_semana)

    # Enviar mensaje con los botones
    bot.send_message(message.chat.id, "¿Qué rango te gustaría analizar? 🌡️", reply_markup=markup)

#Hacer llamada de ozono - - - - - - - - - -
@bot.message_handler(commands=['ozono'])
def send_ozono(message):
    markup = types.InlineKeyboardMarkup(row_width=2)

    # Creación de los botones
    btn_ozono_dia = types.InlineKeyboardButton('Hoy', callback_data='ozono_hoy')
    btn_ozono_semana = types.InlineKeyboardButton('Semana', callback_data='ozono_semana')

    # Agrega botones al Markup
    markup.add(btn_ozono_dia, btn_ozono_semana)

    # Enviar mensaje con los botones
    bot.send_message(message.chat.id, "¿Qué rango te gustaría analizar? 🌎", reply_markup=markup)

#Hacer llamada de Resumen - - - - - - - - - -
@bot.message_handler(commands=['resumen'])
def send_resumen(message):
    markup = types.InlineKeyboardMarkup(row_width=2)

    # Creación de los botones
    btn_calidad_resumen = types.InlineKeyboardButton('Calidad del aire', callback_data='calidad_aire')
    btn_categoria = types.InlineKeyboardButton('Categoria del día', callback_data='categoria_hoy')

    # Agrega botones al Markup
    markup.add(btn_calidad_resumen, btn_categoria)

    # Enviar mensaje con los botones
    bot.send_message(message.chat.id, "¿Qué te gustaría conocer? 🔮", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    
    if call.data == 'calidad_aire':
        summary = analyze_environment(ibero1, sensor1, sensor2)
        bot.send_message(message, 'Hola')
    elif call.data == 'categoria_hoy':
        tweet_text = analyze_air_quality()
        if tweet_text is not None:
            bot.send_message(message, tweet_text)
        else:
            bot.send_message(message, 'Error al categorizar la calidad del aire.')

    elif call.data == 'ozono_hoy':
        bot.answer_callback_query(call.id, '¡Esta es la información del día!')
        max_value, image_filename = generar_report_ozono_diario()
        bot.send_photo(chat_id=call.chat.id, photo=image_filename, caption= 'El valor maximo es:' + max_value)
        
    elif call.data == 'ozono_semana':
        bot.answer_callback_query(call.id, '¡Esta es la información de la semana!')
        max_value, image_filename = generar_report_ozono_semana()
        bot.send_photo(chat_id=call.chat.id, photo=image_filename, caption= 'El valor maximo es:' + max_value)
        
    elif call.data == 'temp_hoy':
        bot.answer_callback_query(call.id, '¡Esta es la información del día!')
        max_value, image_filename = generar_report_temperatura_diario()
        bot.send_photo(chat_id=call.chat.id, photo=image_filename, caption= 'El valor maximo es:' + max_value)
        
    elif call.data == 'temp_semana':
        bot.answer_callback_query(call.id, '¡Esta es la información de la semana!')
        max_value, image_filename = generar_report_temperatura_semana()
        bot.send_photo(chat_id=call.chat.id, photo=image_filename, caption= 'El valor maximo es:' + max_value)


#Funcion para enviar una imagen
@bot.message_handler(commands=['foto'])
def send_image(message):
    img_url='ozonoimagen.jpg'
    bot.send_photo(chat_id=message.chat.id, photo=img_url, caption='Aqui tienes tu imagen')

if __name__ == "__main__":
    bot.polling(none_stop=True)

