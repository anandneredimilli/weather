import requests

url = "https://weatherapi-com.p.rapidapi.com/current.json"

parameters = {"q":"16.518854,81.368480"} #latitude and longitude

key = {
	"X-RapidAPI-Key": "8c5205b29emshd4249e142e5330dp1fe9e0jsn4becbc3de772",
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

response = requests.get(url, headers=key, params=parameters)

print(response.json())