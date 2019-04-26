import requests
from pydub import AudioSegment
from pydub.playback import play
from datetime import datetime
import time

rurl = 'https://api.coincap.io/v2/assets/bitcoin'
headers = {'content-type': 'application/json; charset=utf-8'}
payload = {}
AudioSegment.ffmpeg = '~/Documents/bitrate/death.mp3'
audio = AudioSegment.from_mp3('death.mp3')

key = 'changePercent24Hr'
score = 0.0
num = 00

def run():
    res = requests.request('GET', rurl, headers=headers, data=payload)
    j = res.json()
    data = j['data']
    btc = float(data[key])
    clock = datetime.now().strftime("%H:%M:%S")

    while True:
        global score
        global num
        if btc < score:
            diff = score - btc
            print('{} BTC {}\n  FALL: -{}'.format(clock, num, diff))
            play(audio)
        elif btc > score:
            diff = btc - score
            print('{} BTC {}\n  RISE: +{}'.format(clock, num, diff))
        else:
            print('{} BTC {}\n  SAFE: {}'.format(clock, num, btc))
        score = btc
        num += 1
        time.sleep(30)
        return run()
