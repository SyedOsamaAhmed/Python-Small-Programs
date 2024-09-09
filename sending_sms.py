import requests
import schedule
import time


def sendMessage():
    resp = requests.post('https://textbelt.com/text', {
        'phone': '03345122864',
        'message': 'Hi,good morning',
        'key': 'textbelt',
    })
    print(resp)


schedule.every(10).seconds.do(sendMessage)
while True:
    schedule.run_pending()
    time.sleep(1)
