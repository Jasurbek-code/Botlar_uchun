from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, CallbackContext

# Tokeningni o'zgartiring
TOKEN = '7720070992:AAGaLHb5zRJ7puEgEKWOkdaeVzxT3aYpVwk'            # Bot token
kanal = 'https://t.me/chdpu_ziyo_kanali'                            # A'zo buladigan kanal
userlar = []                                                        # Userlani idsini saqlaydi. (Qayta ovoz bermaslik uchun)
poll_active = False                                                 # 1 marta ovoz berishni yoqib uchirish. True = ovoz berish mumkin

# Ovozlar
votes = {"Xamrayev Rustam Juraqulovich": 0,
    "Muhammadiyev Lochin G'ayratovich": 0,
    "G'aniyev Ilhom Dustnazarovich": 0,
    "Ismailova Dilafruz Muxiddinovna": 0,
    "Yuldashev Xusan Burxonovich": 0,
    "Azimov Davron G'ayratovich": 0,
    "Jo'rayev Sherali Mahmudovich": 0,
    "Atabekov Fozil O`razaliyevich": 0,
    "Matlibova Nilufar Xamid qizi": 0,
    "Narmanov Alisher Xasanovich": 0
    }

# Foydalanuvchi kanalga a'zo bo'lsa
def check_channels(update: Update, context: CallbackContext):
    return True  # O'zingizning shartlaringizga ko'ra o'zgartiring


# Botni ishga tushirish
def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Kanalimiz", url=kanal)],
        [InlineKeyboardButton("✅ Tasdiqlash", callback_data='confirm')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("🤝 Ovoz berish uchun va yangiliklardan habardor bo'lish uchun bizning kanalimizga ulaning va tasdiqlang:", reply_markup=reply_markup)


def confirm(update: Update, context: CallbackContext):
    global poll_active
    query = update.callback_query
    query.answer()

    user = query.from_user
    try:
        if not user.id in userlar:                      # userlar avval kirganligini tekshirish
            poll_active = True
            userlar.append(user.id)

        # Tekshirish: foydalanuvchi kanalda bormi   chdpu_ziyo_kanali
        chat_member = context.bot.get_chat_member(chat_id='@shaxsiy_bloger', user_id=user.id)

        if chat_member.status in ['member', 'administrator', 'creator']:
            # Ovoz berish uchun tugmalarni jo'natish
            keyboard = [
                [InlineKeyboardButton(f"""Xamrayev Rustam Juraqulovich - {votes["Xamrayev Rustam Juraqulovich"]}""", callback_data='vote_Rustam')],
                [InlineKeyboardButton(f"""Muhammadiyev Lochin G'ayratovich - {votes["Muhammadiyev Lochin G'ayratovich"]}""", callback_data='vote_Lochin')],
                [InlineKeyboardButton(f"""G'aniyev Ilhom Dustnazarovich - {votes["G'aniyev Ilhom Dustnazarovich"]}""", callback_data='vote_Ilhom')],
                [InlineKeyboardButton(f"""Ismailova Dilafruz Muxiddinovna - {votes["Ismailova Dilafruz Muxiddinovna"]}""", callback_data='vote_Dilafruz')],
                [InlineKeyboardButton(f"""Yuldashev Xusan Burxonovich - {votes["Yuldashev Xusan Burxonovich"]}""", callback_data='vote_Xusan')],
                [InlineKeyboardButton(f"""Azimov Davron G'ayratovich - {votes["Azimov Davron G'ayratovich"]}""", callback_data='vote_Davron')],
                [InlineKeyboardButton(f"""Jo'rayev Sherali Mahmudovich - {votes["Jo'rayev Sherali Mahmudovich"]}""", callback_data='vote_Sherali')],
                [InlineKeyboardButton(f"""Atabekov Fozil O`razaliyevich - {votes["Atabekov Fozil O`razaliyevich"]}""", callback_data='vote_Fozil')],
                [InlineKeyboardButton(f"""Matlibova Nilufar Xamid qizi - {votes["Matlibova Nilufar Xamid qizi"]}""", callback_data='vote_Nilufar')],
                [InlineKeyboardButton(f"""Narmanov Alisher Xasanovich - {votes["Narmanov Alisher Xasanovich"]}""", callback_data='vote_Alisher')],
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)

            query.edit_message_text(text="✅ Ovoz berishingiz mumkin 🙂")
            query.message.reply_photo(photo=open('Ishtirokchilar.jpg', 'rb'), caption="""#Soʻrovnoma

DIQQAT, YIL SO‘ROVNOMASI BOSHLANMOQDA: SIZNINGCHA, UNIVERSITETIMIZDA  2024-YILDA ENG FAOL YOSHLAR BILAN ISHLASH BOʻYICHA DEKAN OʻRINBOSARI KIM BO‘LDI?

"MA'RIFAT ZIYOSI" kanali yilning eng yaxshilarini aniqlashni oʻziga maqsad qildi. Yuqoridagi suratda universitetimizdagi yoshlar bilan ishlash boʻyicha dekan oʻrinbosarlari oʻrin olgan.

Yoshlar bilan ishlash, ma'naviyat va ma'rifat boʻlimi  tomonidan tavsiya etilgan ushbu nomzodlarning faoliyatini qanday baholaysiz? Kim yilning eng yaxshisi boʻlishga loyiq? Munosib nomzodlarni qoʻllab-quvvatlaymiz!

ESLATMA: turli botlar orqali sun'iy ovoz jamgʻarishga harakat qilgan nomzodlar soʻrovnomadan chetlashtiriladi.

Biz sizga eng yaxshilarini ilinamiz. "MA'RIFAT ZIYOSI" kanali.

Soʻrovnoma 21.12.2024 - yil soat 09:00 dan 28.12.2024 - yil soat 18:00 ga qadar davom etadi. Eng koʻp ovoz toʻplagan ishtirokchi yil yakunida universitetimizning maxsus sovgʻasi bilan taqdirlanadi.

Bizni ijtimoiy tarmoqlarda kuzatib boring:
@chdpu_ziyo_kanali""",
                                reply_markup=reply_markup)
        else:
            query.message.reply_text("❗️ Avval kanalga ulanganingizni tekshirib oling!")
    except:
        pass

def vote(update: Update, context: CallbackContext):
    global poll_active

    query = update.callback_query
    query.answer()

    if not poll_active:
        return                                          # Agar ovoz berish tugasa, hech narsa qilmaymiz

    user = query.from_user
    #chat_member = context.bot.get_chat_member(chat_id='@shaxsiy_bloger', user_id=user.id)

    # Ovoz berish
    if query.data == 'vote_Rustam':
        votes["Xamrayev Rustam Juraqulovich"] += 1
        query.message.reply_text(f"Foydalanuvchi: {user.username}\nSiz Xamrayev Rustam Juraqulovich ga ovoz berdingiz.")
    elif query.data == 'vote_Lochin':
        votes["Muhammadiyev Lochin G'ayratovich"] += 1
        query.message.reply_text(f"Foydalanuvchi: {user.username}\nSiz Muhammadiyev Lochin G'ayratovich ga ovoz berdingiz.")
    elif query.data == 'vote_Ilhom':
        votes["G'aniyev Ilhom Dustnazarovich"] += 1
        query.message.reply_text(f"Foydalanuvchi: {user.username}\nSiz G'aniyev Ilhom Dustnazarovich ga ovoz berdingiz.")
    elif query.data == 'vote_Dilafruz':
        votes["Ismailova Dilafruz Muxiddinovna"] += 1
        query.message.reply_text(f"Foydalanuvchi: {user.username}\nSiz Ismailova Dilafruz Muxiddinovna ga ovoz berdingiz.")
    elif query.data == 'vote_Xusan':
        votes["Yuldashev Xusan Burxonovich"] += 1
        query.message.reply_text(f"Foydalanuvchi: {user.username}\nSiz Yuldashev Xusan Burxonovich ga ovoz berdingiz.")
    elif query.data == 'vote_Davron':
        votes["Azimov Davron G'ayratovich"] += 1
        query.message.reply_text(f"Foydalanuvchi: {user.username}\nSiz Azimov Davron G'ayratovich ga ovoz berdingiz.")
    elif query.data == 'vote_Sherali':
        votes["Jo'rayev Sherali Mahmudovich"] += 1
        query.message.reply_text(f"Foydalanuvchi: {user.username}\nSiz Jo'rayev Sherali Mahmudovich ga ovoz berdingiz.")
    elif query.data == 'vote_Fozil':
        votes["Atabekov Fozil O`razaliyevich"] += 1
        query.message.reply_text(f"Foydalanuvchi: {user.username}\nSiz Atabekov Fozil O`razaliyevich ga ovoz berdingiz.")
    elif query.data == 'vote_Nilufar':
        votes["Matlibova Nilufar Xamid qizi"] += 1
        query.message.reply_text(f"Foydalanuvchi: {user.username}\nSiz Matlibova Nilufar Xamid qizi ga ovoz berdingiz.")
    elif query.data == 'vote_Alisher':
        votes["Narmanov Alisher Xasanovich"] += 1
        query.message.reply_text(f"Foydalanuvchi: {user.username}\nSiz Narmanov Alisher Xasanovich ga ovoz berdingiz.")

    keyboard = [
        [InlineKeyboardButton(f"""Xamrayev Rustam Juraqulovich - {votes["Xamrayev Rustam Juraqulovich"]}""",
                              callback_data='vote_Rustam')],
        [InlineKeyboardButton(f"""Muhammadiyev Lochin G'ayratovich - {votes["Muhammadiyev Lochin G'ayratovich"]}""",
                              callback_data='vote_Lochin')],
        [InlineKeyboardButton(f"""G'aniyev Ilhom Dustnazarovich - {votes["G'aniyev Ilhom Dustnazarovich"]}""",
                              callback_data='vote_Ilhom')],
        [InlineKeyboardButton(f"""Ismailova Dilafruz Muxiddinovna - {votes["Ismailova Dilafruz Muxiddinovna"]}""",
                              callback_data='vote_Dilafruz')],
        [InlineKeyboardButton(f"""Yuldashev Xusan Burxonovich - {votes["Yuldashev Xusan Burxonovich"]}""",
                              callback_data='vote_Xusan')],
        [InlineKeyboardButton(f"""Azimov Davron G'ayratovich - {votes["Azimov Davron G'ayratovich"]}""",
                              callback_data='vote_Davron')],
        [InlineKeyboardButton(f"""Jo'rayev Sherali Mahmudovich - {votes["Jo'rayev Sherali Mahmudovich"]}""",
                              callback_data='vote_Sherali')],
        [InlineKeyboardButton(f"""Atabekov Fozil O`razaliyevich - {votes["Atabekov Fozil O`razaliyevich"]}""",
                              callback_data='vote_Fozil')],
        [InlineKeyboardButton(f"""Matlibova Nilufar Xamid qizi - {votes["Matlibova Nilufar Xamid qizi"]}""",
                              callback_data='vote_Nilufar')],
        [InlineKeyboardButton(f"""Narmanov Alisher Xasanovich - {votes["Narmanov Alisher Xasanovich"]}""",
                              callback_data='vote_Alisher')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    query.message.delete()
    query.message.reply_photo(photo=open('Ishtirokchilar.jpg', 'rb'), caption="""#Soʻrovnoma

DIQQAT, YIL SO‘ROVNOMASI BOSHLANMOQDA: SIZNINGCHA, UNIVERSITETIMIZDA  2024-YILDA ENG FAOL YOSHLAR BILAN ISHLASH BOʻYICHA DEKAN OʻRINBOSARI KIM BO‘LDI?

"MA'RIFAT ZIYOSI" kanali yilning eng yaxshilarini aniqlashni oʻziga maqsad qildi. Yuqoridagi suratda universitetimizdagi yoshlar bilan ishlash boʻyicha dekan oʻrinbosarlari oʻrin olgan.

Yoshlar bilan ishlash, ma'naviyat va ma'rifat boʻlimi  tomonidan tavsiya etilgan ushbu nomzodlarning faoliyatini qanday baholaysiz? Kim yilning eng yaxshisi boʻlishga loyiq? Munosib nomzodlarni qoʻllab-quvvatlaymiz!

ESLATMA: turli botlar orqali sun'iy ovoz jamgʻarishga harakat qilgan nomzodlar soʻrovnomadan chetlashtiriladi.

Biz sizga eng yaxshilarini ilinamiz. "MA'RIFAT ZIYOSI" kanali.

Soʻrovnoma 21.12.2024 - yil soat 09:00 dan 28.12.2024 - yil soat 18:00 ga qadar davom etadi. Eng koʻp ovoz toʻplagan ishtirokchi yil yakunida universitetimizning maxsus sovgʻasi bilan taqdirlanadi.

Bizni ijtimoiy tarmoqlarda kuzatib boring:
@chdpu_ziyo_kanali""",
                              reply_markup=reply_markup)

    poll_active = False                       # Ovoz berish tugallandi


def yakun(update: Update, context: CallbackContext):
        query = update.callback_query
        query.answer()

        query.message.reply_text("👍 Ovoz berganingiz uchun rahmat. 👍")


def main():
    global poll_active
    poll_active = True
    updater = Updater(TOKEN)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(confirm, pattern='confirm'))
    dp.add_handler(CallbackQueryHandler(vote, pattern='vote'))
    dp.add_handler(CallbackQueryHandler(yakun, pattern='yakun'))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()


