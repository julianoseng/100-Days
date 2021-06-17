import requests
from datetime import datetime

pixela_my_site = "https://pixe.la/v1/users/julianohh/graphs/graph1"

USERNAME = "julianohh"
TOKEN = "qdgyuijjhgfbsqdq253jhghj433l234bjk921bdksa"
GRAPH_ID = "graph1"


pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixela_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_parameters = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "9.74",
}

# response = requests.post(url=pixela_creation_endpoint, json=pixel_parameters, headers=headers)
# print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20210616"

new_pixel_data = {
    "quantity": "4.5"
}

# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20210616"

response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)