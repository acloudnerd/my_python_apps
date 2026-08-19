import requests
from datetime import datetime

USERNAME = "acloudnerd"
TOKEN = "dfahdgfdy7f6qi3vh3da"
pixela_endpoint = "https://pixe.la/v1/users"
GRAPH_ID = "graph1"
TODAY = datetime.today().strftime("%Y%m%d")

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "Hour",
    "type": "int",
    "color": "kuro",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixela_creation_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
pixel_data = {
    "date": TODAY,
    "quantity": "5",
}

# response = requests.post(url=pixela_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20260819"

new_pixel_data = {
    "quantity": "8",
}

# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20260819"

response = requests.delete(url=delete_endpoint, headers=headers, json=new_pixel_data)
print(response.text)
