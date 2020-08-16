from pypresence import Presence
import requests
from datetime import datetime
import time
import json

client_id = '1234567890'  # Fake ID, put your real one here
RPC = Presence(client_id)  # Initialize the client class
RPC.connect() # Start the handshake loop

print(RPC.update(state="The music RPC", details="No music currently playing"))  # Set the presence

current_time = round((datetime.utcnow() - datetime(1970, 1, 1)).total_seconds())

while True: # The presence will stay on as long as the program is running
    try:
        r = requests.get('http://127.0.0.1:5175/playing_state')
        data =  r.json()
        desc = data['artist']
        if data['album'] != "": # If there's album data
            desc = desc + ' - ' + data['album']
        print(RPC.update(state=data['title'], details=desc))
    except:
        print(RPC.update(state="The music RPC", details="No music currently playing"))
    time.sleep(15) # Can only update rich presence every 15 seconds
