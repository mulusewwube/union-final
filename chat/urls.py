from django.urls import path
from .views import load_previous_chats, check_unread_messages,send_message

app_name = 'chat'

urlpatterns = [
    # path('chat/',chat_view,name='chat' ),

# urls.py
    path('send-message/',send_message, name='send_message'),

    path('load-previous-chats/', load_previous_chats, name='load_previous_chats'),
    path('check-unread-messages/', check_unread_messages, name='check_unread_messages'),
    # other paths
]
