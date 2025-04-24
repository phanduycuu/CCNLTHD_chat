from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import ChatRoom, Message
from rest_framework.decorators import api_view

@api_view(["GET"])
def get_chat_history(request, room_name):
    room = get_object_or_404(ChatRoom, name=room_name)
    messages = Message.objects.filter(room=room).order_by("timestamp")
    return JsonResponse(
        [{"sender": msg.sender.username, "chat": msg.content, "timestamp": msg.timestamp,"file": {
                "name": msg.file.name,
                "url": msg.file.link.url
            } if msg.file else None } for msg in messages],
        safe=False,
    )
