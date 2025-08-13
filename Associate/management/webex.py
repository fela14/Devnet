import requests
import json

url = "https://api.ciscospark.com/v1/teams"

token = "NmUxNzcyMDctMDI2ZS00MWY2LWE2ODktZWQwZmU4NzA0OTcxNDFjN2E5NTgtY2Ri_P0A1_b92032b1-66be-414c-8c0b-507765e6ad61"

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

body = {
    "name": "My Second Team"
}

# Create A Team

# post_response = requests.post(url, headers=headers,
#                               data=json.dumps(body))
# result = post_response.json()
# print(result)

get_response = requests.get(url, headers=headers)
result = get_response.json()
print(result)

teams = result["items"]
for team in teams:
    if team['name'] == "My Second Team":
        teamId = team["id"]

# Create A Room

room_url = "https://api.ciscospark.com/v1/rooms"

room_body = {
    "title": "second room",
    "teamId": teamId
}

room_post = requests.post(room_url, headers=headers,
                               data=json.dumps(room_body)).json()

get_rooms = requests.get(room_url, headers=headers)
result = get_rooms.json()
print("*"*25)
print(result)

rooms = result["items"]
for room in rooms:
    if room['title'] == "second room":
        roomId = room["id"]
print("*"*25)
print(roomId)

# Post a message to the room

msg_url = "https://api.ciscospark.com/v1/messages"

msg_body = {
    "text": "ALERT: Interface on device XYZ is down",
    "roomId": roomId
}

meg_post = requests.post(room_url, headers=headers,
                               data=json.dumps(msg_body)).json()

get_msg = requests.get(msg_url, headers=headers)
result = get_msg.json()
print("#"*25)
print(result)

# rooms = result["items"]
# for room in rooms:
#     if room['title'] == "second room":
#         roomId = room["id"]
# print("*"*25)
# print(roomId)