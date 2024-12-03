import requests

url = "https://meowfacts.herokuapp.com/"

res=requests.get(url=url)
print(res.json())
