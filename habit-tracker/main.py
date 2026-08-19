import requests

USERNAME = "acloudnerd"
TOKEN = "dfahdgfdy7f6qi3vh3da"
pixela_endpoint = "https://pixe.la/v1/users"
GRAPH_ID = "graph1"

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
    "date": "20260819",
    "quantity": "3",
}

response = requests.post(url = pixela_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)


