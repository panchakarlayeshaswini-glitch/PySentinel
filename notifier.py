import httpx
import yaml


def load_notification_config():
    with open("config/notifications.yaml", "r") as file:
        return yaml.safe_load(file)


async def send_discord_notification(message):
    config = load_notification_config()
    discord = config["notifications"]["discord"]

    if not discord["enabled"] or not discord["webhook_url"]:
        return False

    payload = {
        "content": message
    }

    async with httpx.AsyncClient(timeout=10) as client:
        response = await client.post(
            discord["webhook_url"],
            json=payload
        )

        print(f"Discord notification status: {response.status_code}")
        return True


async def send_slack_notification(message):
    config = load_notification_config()
    slack = config["notifications"]["slack"]

    if not slack["enabled"] or not slack["webhook_url"]:
        return False

    payload = {
        "text": message
    }

    async with httpx.AsyncClient(timeout=10) as client:
        response = await client.post(
            slack["webhook_url"],
            json=payload
        )

        print(f"Slack notification status: {response.status_code}")
        return True


async def send_notification(message):
    config = load_notification_config()
    notifications = config["notifications"]

    print("\n🚨 ALERT TRIGGERED!")
    print(message)

    notification_sent = False

    if notifications["discord"]["enabled"]:
        result = await send_discord_notification(message)
        notification_sent = notification_sent or result

    if notifications["slack"]["enabled"]:
        result = await send_slack_notification(message)
        notification_sent = notification_sent or result

    if not notification_sent:
        print("Notification channels are disabled. Alert displayed locally.")