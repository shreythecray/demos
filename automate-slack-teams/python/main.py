from trycourier import Courier
client = Courier(auth_token="<auth-token>")

resp = client.send_message(
  message={
    "to": {
      "slack": {
        "access_token": "access_token",
        "email": "example@gmail.com",
      },
      "ms_teams": {
          "conversation_id": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
          "tenant_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
          "service_url": "https://smba.trafficmanager.net/amer",
      },
      "email": "example@gmail.com",
      "phone_number": "123-456-7890"
    },
    # "template": "template_id",
    # note: routing object below is not needed if template is used instead of content object
      "content": {
        "title": "Important Survey Reminder",
        "body": "This is a reminder to fill out your survey by the end of this week.",
    },
    "routing": {
        # method: "single",
        "method": "all",
        "channels": ["direct_message", "email"]
      }
  }
)
print(resp['requestId'])
