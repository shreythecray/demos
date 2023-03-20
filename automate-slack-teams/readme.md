# Node.js

```javascript
const { CourierClient } = require("@trycourier/courier");

const courier = CourierClient({ authorizationToken: "auth_token" });

async function send_message() {
  const { requestId } = await courier.send({
    message: {
      to: {
        slack: {
          access_token: "access_token",
          email: "example@email.com"
        },
        ms_teams: {
          conversation_id: "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
          tenant_id: "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
          service_url: "https://smba.trafficmanager.net/amer"
        },
        email: "example@email.com",
        phone_number: "123-456-7890"
      },
      // template: "template_id",
      content: {
        title: "Important Survey Reminder",
        body: "This is a reminder to fill out your survey by the end of this week.",
      },
      routing: {
        //method: "single",
        method: "all",
        channels: ["direct_message", "email", "sms"]
      }
    },
  });
  console.log(requestId)
}

send_message()
```

# Python

```python
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
      "content": {
        "title": "Important Survey Reminder",
        "body": "This is a reminder to fill out your survey by the end of this week.",
    },
    "routing": {
        # method: "single",
        "method": "all",
        "channels": ["direct_message", "email", "sms"]
      }
  }
)
print(resp['requestId'])
```

# Customization

## Routing

**Method: Single vs All**

- Single: send to only one of the specified channels. Courier will send in the order listed within the routing.channels property. If first channel fails, Courier will send to next channels, and so on until the message is delivered successfully.
- All: send to all channels listed.

## Templates

The routing object below is only needed for when you define the message within the API call (i.e. in the content object). If you decide to build your message as a notification template within https://app.courier.com/designer/, you can you remove both the content and routing objects, and just add the template object.
