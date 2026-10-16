import os
import telebot

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN is not configured")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(
        resize_keyboard=True
    )
    keyboard.row("🛍 خرید Mew Points", "🎁 گیفت‌ها")
    keyboard.row("💰 قیمت‌ها", "📞 پشتیبانی")
    bot.reply_to(
        message,
        "🐱 به MEW STORE خوش اومدی!\n"
        "Welcome to MEW STORE!\n\n"
        "یک گزینه رو انتخاب کن 👇",
        reply_markup=keyboard
    )

@bot.message_handler(func=lambda message: True)
def menu(message):
    text = message.text

    if text == "🛍 خرید Mew Points":
        bot.reply_to(
            message,
            "مقدار Mew Points موردنظرت رو برای ثبت سفارش بفرست."
        )
    elif text == "🎁 گیفت‌ها":
        bot.reply_to(message, "🎁 برای سفارش گیفت با پشتیبانی هماهنگ کن.")
    elif text == "💰 قیمت‌ها":
        bot.reply_to(
            message,
            "💎 هر ۱ میلیون Mew Points: ۴۸۰۰ تومان"
        )
    elif text == "📞 پشتیبانی":
        bot.reply_to(message, "برای ثبت سفارش، پیام پشتیبانی رو ارسال کن.")
    else:
        bot.reply_to(message, "لطفاً یکی از گزینه‌های منو رو انتخاب کن.")

bot.infinity_polling()
