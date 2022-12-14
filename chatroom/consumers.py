import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync


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
        print(message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type':"user_message",
                'message': message  #this is the information
            }
        )
        #collect the above information and send it to webpage/websocket
    
    async def user_message(self, event):
        message = event['message']

        await self.send(text_data=json.dumps({'user_message':message}))

        

'''
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name

        await self.channel_layer.group_add(
            self.room_name,
            self.channel_name
        )

        await self.accept()
        

    async def disconnect(self):
        await self.channel_layer.group_discard(
            self.room_name,
            self.channel_name
        )
    


    
'''
