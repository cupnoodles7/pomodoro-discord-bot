

import os
import time
from discord_webhook import DiscordWebhook

# Get webhook URL from environment variable
webhook_url = os.getenv("SLIMEY_HOOK")

# Check if the webhook URL is available
if not webhook_url:
    raise ValueError("Error: SLIMEY_HOOK environment variable is not set!")

# Send a test message to Discord
while True:
    DiscordWebhook(url=webhook_url, content="Lock in, kid").execute()
    time.sleep(60*1)# Send message every 25 minutes
    DiscordWebhook(url=webhook_url, content="Lock out, kid").execute()
    time.sleep(60*0.1) #break for 5 minutes
