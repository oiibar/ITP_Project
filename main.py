import logging
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes, ConversationHandler

TOKEN = "7831039981:AAEXX1yyZb44ZYEquV6K3C-_sb3yAg2ooZk"
logging.basicConfig(level=logging.INFO)

REGMID, REGEND, FINAL = range(3)
ATTENDANCE = 4


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет АЙТУшник! Я ваш Aitu bot. Используйте /menu для списка команд.")

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    commands = "/start - Запустить бота\n/menu - Показать команды\n/stepa - считать стипендию\n/attendance - подсчитать посещаемость\n/syllabus - получить силлабус"
    await update.message.reply_text(f"Список команд:\n{commands}")


async def attendance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Введите число пропусков:")
    return ATTENDANCE


async def process_attendance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message.text.isdigit():
        await update.message.reply_text("❌ Пожалуйста, введите число!")
        return ATTENDANCE

    attendance = float(update.message.text)
    result = (1 - (attendance / 30)) * 100
    await update.message.reply_text(f"✅ Посещаемость до файнала: {result:.2f}%")
    return ConversationHandler.END


async def stepa(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Введите оценку за RegMid (в процентах):")
    return REGMID


async def process_regmid(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message.text.isdigit():
        await update.message.reply_text("❌ Введите только число!")
        return REGMID

    context.user_data["regmid"] = float(update.message.text)
    await update.message.reply_text("Введите оценку за RegEnd (в процентах):")
    return REGEND


async def process_regend(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message.text.isdigit():
        await update.message.reply_text("❌ Введите только число!")
        return REGEND

    context.user_data["regend"] = float(update.message.text)
    possible_score = 0.3 * context.user_data["regmid"] + 0.3 * context.user_data["regend"]
    required_final = (70 - possible_score) / 0.4

    keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("Ввести финальный балл", callback_data="enter_final")]])
    await update.message.reply_text(
        f"💡 Чтобы получить стипендию (≥70%), вам нужно набрать {required_final:.2f}% на финальном экзамене.",
        reply_markup=keyboard
    )
    return FINAL


async def process_final(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message.text.isdigit():
        await update.message.reply_text("❌ Введите только число!")
        return FINAL

    context.user_data["final"] = float(update.message.text)
    total_score = (0.3 * context.user_data["regmid"] + 0.3 * context.user_data["regend"] + 0.4 * context.user_data[
        "final"])

    if total_score >= 70:
        await update.message.reply_text(f"✅ Ваш общий балл: {total_score:.2f}%. Поздравляем! Вы на стипендии! 🎉")
    else:
        await update.message.reply_text(
            f"❌ Ваш общий балл: {total_score:.2f}%. К сожалению, этого недостаточно для стипендии.")
    return ConversationHandler.END


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "enter_final":
        await query.message.reply_text("Введите финальный балл:")
        return FINAL


async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Неизвестная команда. Используйте /menu для списка команд.")


async def calc(update, context):
    chat_id = update.message.chat_id
    document = open('syllabus/calc.pdf', 'rb')
    await context.bot.send_document(chat_id, document)

async def dm(update, context):
    chat_id = update.message.chat_id
    document = open('syllabus/dm.pdf', 'rb')
    await context.bot.send_document(chat_id, document)

async def itp(update, context):
    chat_id = update.message.chat_id
    document = open('syllabus/itp.pdf', 'rb')
    await context.bot.send_document(chat_id, document)

app = ApplicationBuilder().token(TOKEN).build()

conv_handler = ConversationHandler(
    entry_points=[CommandHandler("stepa", stepa)],
    states={
        REGMID: [MessageHandler(filters.TEXT & ~filters.COMMAND, process_regmid)],
        REGEND: [MessageHandler(filters.TEXT & ~filters.COMMAND, process_regend)],
        FINAL: [MessageHandler(filters.TEXT & ~filters.COMMAND, process_final)],
    },
    fallbacks=[]
)

attend_handler = ConversationHandler(
    entry_points=[CommandHandler("attendance", attendance)],
    states={ATTENDANCE: [MessageHandler(filters.TEXT & ~filters.COMMAND, process_attendance)]},
    fallbacks=[]
)

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("menu", menu))
app.add_handler(CommandHandler("calc_syllabus", calc))
app.add_handler(CommandHandler("dm_syllabus", dm))
app.add_handler(CommandHandler("itp_syllabus", itp))
app.add_handler(attend_handler)
app.add_handler(conv_handler)
app.add_handler(CallbackQueryHandler(button_handler))
app.add_handler(MessageHandler(filters.COMMAND, unknown))

if __name__ == "__main__":
    app.run_polling()
