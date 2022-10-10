import telebot
from telebot import types

bot = telebot.TeleBot("5382395357:AAEbtXt7OLGA6MrzhelNugrzBLVTuG_ATmc")

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button0 = types.KeyboardButton("🏠Домашняя тренировка🏠")
    button1 = types.KeyboardButton("🏋Тренировка в зале🏋")
    markup.add(button0,button1)
    bot.send_message(message.chat.id,text="Ну здарова, вижу решил подкачаться, ну давай, выбирай)".format(message.from_user),reply_markup=markup)

@bot.message_handler(content_types=["text"])
def bot_message0(message):
    if message.text == "🏠Домашняя тренировка🏠":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("♂ Мужик 🧔")
        button2 = types.KeyboardButton("♀ Леди 👩")
        button3 = types.KeyboardButton("Инфа о боте")
        button4 = types.KeyboardButton("Выбор места")
        markup.add(button1, button2, button3,button4,)
        bot.send_message(message.chat.id, "Домашняя тренировка", reply_markup=markup)

    if message.chat.type == "private":
        if message.text == "♂ Мужик 🧔":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton("💸Пресс🧔")
            button2 = types.KeyboardButton("🦵Ноги🧔")
            button3 = types.KeyboardButton("💪Руки🧔")
            button4 = types.KeyboardButton("Сиська🧔")
            button5 = types.KeyboardButton("Спина🧔")
            button6 = types.KeyboardButton("Назад")
            markup.add(button1, button2, button3,button4,button5,button6)
            bot.send_message(message.chat.id, "♂ Мужик 🧔", reply_markup=markup)

        elif message.text == "💸Пресс🧔":
                bot.send_message(message.chat.id,"────────────────────────")
                bot.send_video(message.chat.id,'https://goodlooker.ru/wp-content/uploads/2020/11/Skruchivanie_razvedenie_ruk_koleni_vverh.gif')
                bot.send_video(message.chat.id,"https://goodlooker.ru/wp-content/uploads/2021/01/Velosiped_new.gif")
                bot.send_video(message.chat.id,"https://goodlooker.ru/wp-content/uploads/2020/09/Opuskanie_pryamih_nog.gif")
                bot.send_video(message.chat.id,"https://goodlooker.ru/wp-content/uploads/2020/10/Ohotnichya_sobaka_obe_storony.gif")
                bot.send_video(message.chat.id,"https://goodlooker.ru/wp-content/uploads/2020/11/Situp_ruki_vpered.gif")
                bot.send_video(message.chat.id,"https://goodlooker.ru/wp-content/uploads/2020/04/Alpinist-1.gif")
                bot.send_message(message.chat.id,"────────────────────────")

        elif message.text == "🦵Ноги🧔":
                bot.send_message(message.chat.id,"────────────────────────")
                bot.send_video(message.chat.id,"https://goodlooker.ru/wp-content/uploads/2020/04/Prisedaniya_turemnye.gif")
                bot.send_video(message.chat.id,"https://goodlooker.ru/wp-content/uploads/2021/01/Vypady_vpered.gif")
                bot.send_video(message.chat.id,"https://goodlooker.ru/wp-content/uploads/2020/11/Mahi_nogami.gif")
                bot.send_video(message.chat.id,"https://goodlooker.ru/wp-content/uploads/2020/06/Prisedanie_pryzhok.gif")
                bot.send_video(message.chat.id,"https://goodlooker.ru/wp-content/uploads/2020/11/Vypad_na_meste_bez_inventarya.gif")
                bot.send_video(message.chat.id,"https://goodlooker.ru/wp-content/uploads/2020/04/Sumo_shirokie_nogi.gif")
                bot.send_message(message.chat.id, "────────────────────────")

        elif message.text == "💪Руки🧔":
                bot.send_message(message.chat.id,"────────────────────────")
                bot.send_video(message.chat.id, "https://goodlooker.ru/wp-content/uploads/2020/03/Sgibanie_ruk.gif")#Бинецпс
                bot.send_video(message.chat.id, "https://goodlooker.ru/wp-content/uploads/2020/03/Sgibanie_ruk_s_supinaciej_2.gif") #Бицепс
                bot.send_video(message.chat.id, "https://goodlooker.ru/wp-content/uploads/2020/03/Sgibanie_ruk_molotkom.gif") #Бицепс
                bot.send_video(message.chat.id, "https://goodlooker.ru/wp-content/uploads/2020/02/Zhim_ganteley_stoya.gif")  #Плечи
                bot.send_video(message.chat.id, "https://goodlooker.ru/wp-content/uploads/2020/04/Podem_ruki_pered_soboj.gif") #Плечи
                bot.send_video(message.chat.id, "https://goodlooker.ru/wp-content/uploads/2020/02/Zhim_ganteley_stoya.gif")#Плечи
                bot.send_video(message.chat.id, "https://goodlooker.ru/wp-content/uploads/2020/02/Razvedenie_ruk_v_naklone.gif")#Плечи
                bot.send_video(message.chat.id, "https://goodlooker.ru/wp-content/uploads/2020/04/Tyaga_gentelej_k_podborodku.gif")#Плечи
                bot.send_video(message.chat.id, "https://goodlooker.ru/wp-content/uploads/2020/04/Zhim_arnolda_sidya-300x300.gif")#Плечи
                bot.send_video(message.chat.id, "https://goodlooker.ru/wp-content/uploads/2020/04/Zhim_ganteley_neutral.gif")#Трицепс
                bot.send_video(message.chat.id, "https://goodlooker.ru/wp-content/uploads/2020/02/Razgibanie_ganteli_izza_golovy.gif")#Трицепс
                bot.send_video(message.chat.id, "https://goodlooker.ru/wp-content/uploads/2020/04/Razgibaniya_ruk_lezha.gif")#Трицепс
                bot.send_message(message.chat.id, "────────────────────────")

        elif message.text == "Сиська🧔":
                bot.send_message(message.chat.id, "────────────────────────")
                bot.send_video(message.chat.id,"")
                bot.send_video(message.chat.id,"")
                bot.send_video(message.chat.id,"")
                bot.send_video(message.chat.id,"")
                bot.send_video(message.chat.id,"")
                bot.send_message(message.chat.id, "────────────────────────")

        elif message.text == "Спина🧔":
                bot.send_message(message.chat.id, "────────────────────────")
                bot.send_video(message.chat.id,"")
                bot.send_video(message.chat.id,"")
                bot.send_video(message.chat.id,"")
                bot.send_video(message.chat.id,"")
                bot.send_message(message.chat.id, "────────────────────────")


        elif message.text =="♀ Леди 👩":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton("Пресс👩")
            button2 = types.KeyboardButton("Ноги👩")
            button3 = types.KeyboardButton("Руки👩")
            button4 = types.KeyboardButton("Жопа👩")
            button5 = types.KeyboardButton("Талия👩")
            button6 = types.KeyboardButton("Назад")
            markup.add(button1, button2, button3,button4,button5,button6)
            bot.send_message(message.chat.id,"♀ Леди 👩", reply_markup=markup)


        elif message.text == "Пресс👩":
            bot.send_message(message.chat.id, "────────────────")
            bot.send_video(message.chat.id, "https://goodlooker.ru/wp-content/uploads/2022/04/Skruchivanie_klassicheskoe.gif")
            bot.send_video(message.chat.id, "https://goodlooker.ru/wp-content/uploads/2020/12/Roll-in.gif")
            bot.send_video(message.chat.id, "https://goodlooker.ru/wp-content/uploads/2021/03/Naklony_lezha_new.gif")
            bot.send_video(message.chat.id, "https://goodlooker.ru/wp-content/uploads/2020/08/Obratnye_skruchivaniya_koleno_lokot_shiroko.gif")
            bot.send_video(message.chat.id, "https://goodlooker.ru/wp-content/uploads/2020/06/Velosiped_na_predplechyah.gif")
            bot.send_video(message.chat.id, "https://goodlooker.ru/wp-content/uploads/2021/11/Sgibanie_kolen_k_grudi_na_stule.gifЦ")
            bot.send_message(message.chat.id, "────────────────")

        elif message.text == "Ноги👩":
            bot.send_message(message.chat.id, "────────────────")
            bot.send_video(message.chat.id, "")
            bot.send_video(message.chat.id, "")
            bot.send_video(message.chat.id, "")
            bot.send_video(message.chat.id, "")
            bot.send_message(message.chat.id, "────────────────")

        elif message.text == "Руки👩":
            bot.send_message(message.chat.id, "────────────────")
            bot.send_video(message.chat.id, "")
            bot.send_video(message.chat.id, "")
            bot.send_video(message.chat.id, "")
            bot.send_video(message.chat.id, "")
            bot.send_message(message.chat.id, "────────────────")

        elif message.text == "Жопа👩":
            bot.send_message(message.chat.id, "────────────────")
            bot.send_video(message.chat.id, "https://goodlooker.ru/wp-content/uploads/2020/11/Prised_uzkij_shirokij.gif")
            bot.send_video(message.chat.id, "https://goodlooker.ru/wp-content/uploads/2020/12/Pulsirujushij_vypad_shirokij.gif")
            bot.send_video(message.chat.id, "https://goodlooker.ru/wp-content/uploads/2020/12/Otvedenie_nogi_nazad_new.gif")
            bot.send_video(message.chat.id, "https://goodlooker.ru/wp-content/uploads/2020/12/Prised_shirokij_pulsacia-1.gif")
            bot.send_message(message.chat.id, "────────────────")

        elif message.text == "Талия👩":
            bot.send_message(message.chat.id, "────────────────")
            bot.send_video(message.chat.id, "https://goodlooker.ru/wp-content/uploads/2022/01/Naklony_odna_ruka_nad_golovoj.gif")
            bot.send_video(message.chat.id, "https://goodlooker.ru/wp-content/uploads/2022/04/Koleno_lokot_dvojnie.gif")
            bot.send_video(message.chat.id, "https://goodlooker.ru/wp-content/uploads/2022/01/Mah_nogoj_vbok_ruki_vverh_nad_golovoj.gif")
            bot.send_video(message.chat.id, "https://goodlooker.ru/wp-content/uploads/2022/06/Podem_kolenej_s_povorotom_za_rukami.gif")
            bot.send_video(message.chat.id, "https://goodlooker.ru/wp-content/uploads/2022/01/Bistrie_povoroty_ruki_u_grudi.gif")
            bot.send_message(message.chat.id, "────────────────")


        elif message.text == "Инфа о боте":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton("Дата создания")
            button2 = types.KeyboardButton("Назад")
            markup.add(button1, button2,)
            bot.send_message(message.chat.id, "Инфа о боте", reply_markup=markup)
        elif message.text == "Дата создания":
            bot.send_message(message.chat.id,"25.09.2022")



        elif message.text == "Назад":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton("♂ Мужик 🧔")
            button2 = types.KeyboardButton("♀ Леди 👩")
            button3 = types.KeyboardButton("Инфа о боте")
            button4 = types.KeyboardButton("Выбор места")
            markup.add(button1, button2, button3,button4)
            bot.send_message(message.chat.id, "Назад", reply_markup=markup)

        elif message.text == "Выбор места":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button0 = types.KeyboardButton("🏠Домашняя тренировка🏠")
            button1 = types.KeyboardButton("🏋Тренировка в зале🏋")
            markup.add(button0, button1)
            bot.send_message(message.chat.id, "Выбор места", reply_markup=markup)


bot.polling(none_stop=True)


#ГИФКА  https://goodlooker.ru/wp-content/uploads/2021/11/Sgibanie_kolen_k_grudi_na_stule.gif
