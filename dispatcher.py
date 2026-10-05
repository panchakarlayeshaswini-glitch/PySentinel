import asyncio
import time
import httpx
import yaml

from notifier import send_notification


def load_config():
    with open("config/notifications.yaml", "r") as file:
        return yaml.safe_load(file)


async def check_service(name, url):
    config = load_config()
    threshold = config["notifications"]["threshold_ms"]

    start_time = time.perf_counter()

    try:
        async with httpx.AsyncClient(timeout=10) as client:
            response = await client.get(url)

        end_time = time.perf_counter()
        latency = (end_time - start_time) * 1000

        print(f"\nService: {name}")
        print(f"Status Code: {response.status_code}")
        print(f"Response Time: {latency:.2f} ms")

        if latency > threshold:
            message = (
                f"⚠️ PySentinel Alert\n"
                f"Service: {name}\n"
                f"Response time: {latency:.2f} ms\n"
                f"Threshold: {threshold} ms"
            )

            await send_notification(message)

        elif response.status_code >= 400:
            message = (
                f"🚨 PySentinel Alert\n"
                f"Service: {name}\n"
                f"HTTP Status: {response.status_code}"
            )

            await send_notification(message)

        else:
            print("Service is healthy.")

    except Exception as error:
        print(f"\nService: {name}")
        print("Status: DOWN")
        print(f"Reason: {error}")

        message = (
            f"🚨 PySentinel Alert\n"
            f"Service: {name}\n"
            f"Status: DOWN\n"
            f"Reason: {error}"
        )

        await send_notification(message)


async def main():
    await check_service(
        "Python.org",
        "https://www.python.org"
    )


if __name__ == "__main__":
    asyncio.run(main())