# import telegram
# from django.template.loader import render_to_string
# from annport2023.settings.base import BASE_DIR, get_secret
# import json
#
# with open(BASE_DIR / "secret.json") as f:
#     secrets = json.loads(f.read())
#
# api_key = get_secret("TELEGRAM_BOT_API_KEY")
# chat_id = get_secret("TELEGRAM_CHAT_ID")
#
#
# # @spool
# def post_event_on_telegram(of):
#     message_html = render_to_string('academy/onlineform_inbox.html', {
#         'of': of
#     })
#     bot = telegram.Bot(token=api_key)
#     send_message = bot.sendMessage(chat_id, text=message_html, parse_mode=telegram.ParseMode.HTML)
#     bot.sendContact(chat_id, phone_number=of.phoneNumber, first_name=of.name, reply_to_message_id=send_message['message_id'])