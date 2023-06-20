import requests
import os
import sendmail

api_end_point = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ.get('Api_key')
# print(os.environ.get('Api_key'))

location = {'lat':16.518854,
            'lon':81.368480,
            'appid':api_key,
            'exclude':'current,minutely,daily'}
data = requests.get(url=api_end_point, params=location)
print(data.status_code)
hourly_weather_data = data.json()
will_it_rain = False
for i in range(0,12):
    condition_code = hourly_weather_data['hourly'][i]['weather'][0]['id']
    
    if 200 <= condition_code <700 or 801 <= condition_code <=804:
        will_it_rain = True

if will_it_rain:
    sendmail = sendmail.SendMail(message='chances of rain please carry umbrella')