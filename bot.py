from telegram import Update
from telegram.ext import Application, ContextTypes
from datetime import time
import random
import pytz

# User list
users = [
    {"name": "Xolbek", "username": "@xolbekx"},
    {"name": "Ahmed", "username": "@William_zeegot"},
    {"name": "Nodirbek", "username": "@nod1rbek2812"},
    {"name": "Odilbek", "username": "@odilbekmatchonov"},
    {"name": "Zafarbek", "username": "@zafarbekshomurodov1"},
    {"name": "Jushkin", "username": "@jushkin"},
    {"name": "Otamurod", "username": "@Top_Dev_G"},
    {"name": "Ulugbek", "username": "@Ulugbek1_1"}
]

# Store the last message ID for validation
last_message_id = None
user_index = 0  # Start with the first user

# Daily duty announcement
async def daily_task(context: ContextTypes.DEFAULT_TYPE):
    global last_message_id, user_index

    # Get the current user in sequence
    selected_user = users[user_index]

    message = (
        f"‼️‼️‼️‼️\n\n"
        f"Bugun <b>{selected_user['name']}</b> {selected_user['username']} <b>POSUDANI yuvishi garak!</b>\n\n"
        "<b>GAY</b> BO'SANG YUVMASANGAM BO'LADI, SONGA RUXSAT BO\n\n"
        "Tozalab bo'lib bir rasm tasha"
    )

    try:
        # Send the message with HTML formatting
        sent_message = await context.bot.send_message(
            chat_id="-4224307845",
            text=message,
            parse_mode="HTML"
        )

        # Store message_id for future validation
        last_message_id = sent_message.message_id

        # Pin the message
        # await context.bot.pin_message(
        #     chat_id="-4224307845",
        #     message_id=sent_message.message_id
        # )

        # Update the user index for the next day
        user_index = (user_index + 1) % len(users)

    except Exception as e:
        print(f"Error: {e}")
        # Send a fallback message in case of an error
        await context.bot.send_message(
            chat_id="-4224307845",
            text="Oops! I couldn't pin the message due to insufficient permissions."
        )

# Start the bot
def main():
    TOKEN = "7778914325:AAHD7GtsZmItJZNgGEYyohh2r9CZUHWoyXY"
    app = Application.builder().token(TOKEN).build()

    # Define Uzbekistan timezone
    uzbekistan_tz = pytz.timezone('Asia/Tashkent')

    # Schedule daily message
    app.job_queue.run_daily(
        daily_task, time(hour=19, minute=37, tzinfo=uzbekistan_tz), chat_id="-4224307845"
    )
    # app.job_queue.run_once(daily_task, 2)  # Trigger the task after 10 seconds

    # Run the bot
    app.run_polling()

if __name__ == "__main__":
    main()
