#  pip install DingtalkChatbot

from django.conf import settings
from dingtalkchatbot.chatbot import DingtalkChatbot

# at_mobiles -> @ corresponding user
def send(message, at_mobiles=[]):
    webhook = settings.DINGTALK_WEB_HOOK

    # initialize the chat bot
    chatBot = DingtalkChatbot(webhook)

    # @ all
    chatBot.send_text(msg=('Interview Notification: %s' % message), at_mobiles = at_mobiles)