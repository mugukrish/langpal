import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter, get_default_application
from django.core.asgi import get_asgi_application


from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/<str:room_name>/', consumers.ChatConsumer.as_asgi()),
]


if not os.environ.get("LOCAL_DEV"):
    application = ProtocolTypeRouter(
        {
            "websocket":AuthMiddlewareStack(
                URLRouter(
                    websocket_urlpatterns
                )
            )
            # Just HTTP for now. (We can add other protocols later.)
        }
    )

