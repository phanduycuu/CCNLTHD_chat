import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chat.settings")
django.setup()  # Đảm bảo gọi setup() sau khi đặt biến môi trường

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from message.routing import websocket_urlpatterns

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter(websocket_urlpatterns),
})
