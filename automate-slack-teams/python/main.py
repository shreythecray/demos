from trycourier import Courier
client = Courier(auth_token="<auth-token>")

resp = client.send_message(
  message={
    "to": {
      "slack": {
        "access_token": "xoxb-abcd",
        "email": "example@gmail.com",
      },
      "ms_teams": {
          "conversation_id": "85S5NWXJVQ4GN8J21JSKV3JVCSV2",
          "tenant_id": "aac0c564-6c5e-4b05-8dc3-408087f77f76",
          "service_url": "https://smba.trafficmanager.net/amer",
      },
      "email": "example@gmail.com",
      "phone_number": "123-456-7890"
    },
    "template": "Z5N9D2J8DSMBKEHWF27AEEF6J822"
  }
)
print(resp['requestId'])
