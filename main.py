import requests
from decouple import config

TXT = "Hello there, this message is for you!"

def send_the_message(TXT, number):
    API_KEY = config('API_KEY')
    
    
    if not API_KEY:
        raise ValueError("API_KEY is not set. Please check your environment variables.")
    
    URL = f"https://api.kavenegar.com/v1/{API_KEY}/sms/send.json"
    data = {'receptor': number, 'message': TXT}
    
    try:
        r = requests.post(URL, data=data)
        r.raise_for_status()  
        return r.ok
    except requests.exceptions.RequestException as e:
        print(f"Error sending message: {e}")
        return False
