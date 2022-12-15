import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

from .models import UserMessage, ChatRoomsList
from django.contrib.auth.models import User



class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]# room_name coming from router.py
        self.room_group_name = "chat_%s" % self.room_name
        #adding group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type':"test_message",
                'tester': "Hello hello" #this is the information
            }
        )
        
    async def test_message(self, event): #shoudl be as same as the top type
         tester = event['tester']

         await self.send(text_data=json.dumps({'tester':tester}))
    
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = text_data_json['username']
        print(message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type':"user_message",
                'message': message  #this is the information
            }
        )
        await self.save_to_the_db(username,self.room_name,message)

        #collect the above information and send it to webpage/websocket
    async def user_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({'user_message':message}))

    @sync_to_async
    def save_to_the_db(self,user,room,message):
        user = User.objects.get(username=user)
        room = ChatRoomsList.objects.get(slug=room)
        UserMessage.objects.create(user=user, room=room, message=message) 
