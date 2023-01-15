import requests
from datetime import datetime
USERNAME = "cem1707"
TOKEN =  "ASDASDQWEH55"
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor" : "yes"

}
"----- REQUEST POST-------"
#response = requests.post(url = pixela_endpoint, json = user_params)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id" : GRAPH_ID,
    "name" : "Cycling Graph",
    "unit" : "Km",
    "type" : "float",
    "color" : "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

#response = requests.post(url = graph_endpoint, json = graph_config,headers= headers)
#print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
todays_date = datetime.today().strftime("%Y%m%d")

pixel_data = {
    "date" : f"{todays_date}",
    "quantity" : "10.6",

}

#response = requests.post(url = pixel_creation_endpoint,json = pixel_data,headers= headers)
#print(response.text )

to_change_date = "20230115"
pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{to_change_date}"
change_data = {
    "quantity" : "20"
}

"--------REQUEST PUT---------"

#response = requests.put(url = pixel_update_endpoint,json = change_data, headers= headers)
#print(response.text)

"-------REQUEST DELETE-------"

pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{to_change_date}"
response = requests.delete(url = pixel_delete_endpoint, headers= headers)
print(response.text)

