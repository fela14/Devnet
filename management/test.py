from webexteamssdk import WebexTeamsAPI

api = WebexTeamsAPI(
    access_token="NmUxNzcyMDctMDI2ZS00MWY2LWE2ODktZWQwZmU4NzA0OTcxNDFjN2E5NTgtY2Ri_P0A1_b92032b1-66be-414c-8c0b-507765e6ad61"
)

# Find or create team
teamId = None
for team in api.teams.list():
    print(team.name)
    if team.name == "Second Team":
        teamId = team.id

if not teamId:
    create_team = api.teams.create("Second Team")
    teamId = create_team.id

# Find or create room
roomId = None
for room in api.rooms.list():
    if room.title == "Second Room":
        roomId = room.id

if not roomId:
    create_room = api.rooms.create("Second Room", teamId=teamId)
    roomId = create_room.id

# Post a message
api.messages.create(roomId, text="Posted from the SDK")

# Show your own profile
print(api.people.me())















from webexteamssdk import WebexTeamsAPI

api = WebexTeamsAPI(
    access_token="NmUxNzcyMDctMDI2ZS00MWY2LWE2ODktZWQwZmU4NzA0OTcxNDFjN2E5NTgtY2Ri_P0A1_b92032b1-66be-414c-8c0b-507765e6ad61"
)

teamId = None

for team in api.teams.list():
    print(team.name)
    if team.id == "SDK Team":
        teamId = team.id

if not team.id == "SDK Team":
    create_team = api.teams.create(name="SDK Team")
    teamId = create_team.id

roomId = None

for room in api.rooms.list():
    if room.id == "SDK room":
        roomId = room.id

if not room.id == "SDK room":
    create_room = api.rooms.create(name="SDK room", teamId=teamId)
    roomId = room.id

api.message.create(roomId, "ALERT: Created by webexsdk!")












