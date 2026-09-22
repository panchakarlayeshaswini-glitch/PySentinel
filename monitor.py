import asyncio
import time
import httpx
import yaml


# Read targets from YAML file
def load_targets():
    with open("config/targets.yaml", "r") as file:
        data = yaml.safe_load(file)

    return data["targets"]


# Check one website
async def check_target(client, target):
    name = target["name"]
    url = target["url"]

    start_time = time.perf_counter()

    try:
        response = await client.get(url)

        end_time = time.perf_counter()
        latency = (end_time - start_time) * 1000

        print(
            f"[UP]   {name:<10} "
            f"Status: {response.status_code}   "
            f"Response: {latency:.2f} ms"
        )

    except Exception as error:
        end_time = time.perf_counter()
        latency = (end_time - start_time) * 1000

        print(
            f"[DOWN] {name:<10} "
            f"Status: ERROR   "
            f"Response: {latency:.2f} ms"
        )

        print(f"       Reason: {error}")


# Check all websites
async def check_all_targets(targets):
    async with httpx.AsyncClient(timeout=10) as client:

        tasks = []

        for target in targets:
            tasks.append(check_target(client, target))

        await asyncio.gather(*tasks)


# Continuous monitoring daemon
async def main():

    targets = load_targets()

    print("=" * 60)
    print("        PySentinel - Service Health Monitor")
    print("=" * 60)

    print(f"Monitoring {len(targets)} services...")
    print("Check interval: 10 seconds")
    print("Press CTRL+C to stop.")
    print()

    while True:

        print("-" * 60)
        print(f"Health Check - {time.strftime('%Y-%m-%d %H:%M:%S')}")
        print("-" * 60)

        await check_all_targets(targets)

        print()
        print("Next health check in 10 seconds...")
        print()

        await asyncio.sleep(10)


# Start the program
if __name__ == "__main__":
    try:
        asyncio.run(main())

    except KeyboardInterrupt:
        print("\nPySentinel stopped.")