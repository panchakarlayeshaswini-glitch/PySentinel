import asyncio
import httpx
from bs4 import BeautifulSoup
import yaml

from database import initialize_database, save_alert


# Load keywords from YAML
def load_keywords():

    with open("keywords.yaml", "r") as file:
        data = yaml.safe_load(file)

    return data["keywords"]


# Scrape webpage and search for keywords
async def scrape_page(url, keywords):

    async with httpx.AsyncClient(
        timeout=10,
        follow_redirects=True
    ) as client:

        response = await client.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # Remove unwanted elements
        for tag in soup(["script", "style"]):
            tag.decompose()

        # Extract webpage text
        text = soup.get_text(" ", strip=True).lower()

        # Find matching keywords
        matches = [
            keyword
            for keyword in keywords
            if keyword.lower() in text
        ]

        print("\n" + "=" * 60)
        print(f"URL: {url}")
        print(f"Status: {response.status_code}")
        print("=" * 60)

        if matches:

            print("Matched Keywords:")

            for keyword in matches:

                is_new = await save_alert(url, keyword)

                if is_new:
                    print("\n🚨 NEW KEYWORD ALERT!")
                    print(f"Keyword: {keyword}")
                    print(f"Website: {url}")
                else:
                    print(f"- {keyword} [ALREADY EXISTS]")

        else:
            print("No keywords found.")


# Main function
async def main():

    await initialize_database()

    keywords = load_keywords()

    url = "https://www.python.org"

    await scrape_page(url, keywords)


# Start program
if __name__ == "__main__":
    asyncio.run(main())