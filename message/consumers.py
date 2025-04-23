import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth import get_user_model
from asgiref.sync import sync_to_async
from .models import Message, ChatRoom

User = get_user_model()

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        # Tạo phòng chat nếu chưa tồn tại
        await self.get_or_create_room(self.room_name)

        # Thêm user vào nhóm chat
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # Xóa user khỏi nhóm chat
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data["message"]
        sender_username = data["sender"]

        # Lưu tin nhắn vào database
        await self.save_message(self.room_name, sender_username, message)

        # Gửi tin nhắn tới tất cả user trong phòng
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message,
                "sender": sender_username,
            },
        )

    async def chat_message(self, event):
        message = event["message"]
        sender = event["sender"]

        # Gửi tin nhắn tới client
        await self.send(text_data=json.dumps({"message": message, "sender": sender}))

    @sync_to_async
    def get_or_create_room(self, room_name):
        """Tạo phòng chat nếu chưa tồn tại"""
        ChatRoom.objects.get_or_create(name=room_name)

    @sync_to_async
    def save_message(self, room_name, sender_username, message):
        """Lưu tin nhắn vào database"""
        room = ChatRoom.objects.get(name=room_name)
        sender, _ = User.objects.get_or_create(username=sender_username)
        Message.objects.create(room=room, sender=sender, content=message)
