import time
import vlc
import os
import requests, json

os.add_dll_directory(r'C:\\Program Files\\VideoLAN\\VLC')
# api setup
def main():
    try:
        url = 'https://api.fpt.ai/hmi/tts/v5'
        payload = str(input("Please enter something: "))
        if len(payload) == 0:
            print("Enter something!!")
            return
        voice = str(input("voice: "))
        if len(voice) == 0:
            print("Choose voice please!!")
            return
        headers = {
            'api-key': 'YOUR API KEY',
            'speed': '',
            'voice': str(voice)
        }
        response = requests.request('POST', url, data=payload.encode('utf-8'), headers=headers)
        bike_dict = json.loads(response.text)
        p = vlc.MediaPlayer(bike_dict['async'])
        time.sleep(2)
        p.play()
        time.sleep(5)
        p.stop()
        return
    except Exception as err:
        print("error", err)