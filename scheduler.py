import logging
import asyncio

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from monitor import load_targets, check_all_targets
from scraper import load_keywords, scrape_page
from database import initialize_database


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


async def run_monitor():
    """Run a single round of service health checks."""
    logging.info("Starting scheduled health check...")

    targets = load_targets()
    await check_all_targets(targets)

    logging.info("Health check completed.")


async def run_scraper():
    """Run the keyword scraper on a schedule."""
    logging.info("Starting scheduled keyword scraping...")

    keywords = load_keywords()

    # The same URL used by the existing scraper.py
    await scrape_page("https://www.python.org", keywords)

    logging.info("Scheduled scraping completed.")


async def main():
    await initialize_database()

    scheduler = AsyncIOScheduler()

    # Check all configured services every 5 minutes
    scheduler.add_job(
        run_monitor,
        "interval",
        minutes=5,
        id="health_monitor",
        max_instances=1,
        coalesce=True
    )

    # Scrape the configured website every 10 minutes
    scheduler.add_job(
        run_scraper,
        "interval",
        minutes=10,
        id="keyword_scraper",
        max_instances=1,
        coalesce=True
    )

    scheduler.start()

    logging.info("PySentinel Scheduler started.")
    logging.info("Health monitoring: every 5 minutes.")
    logging.info("Keyword scraping: every 10 minutes.")
    logging.info("Press CTRL+C to stop.")

    # Run each task once immediately for testing
    await run_monitor()
    await run_scraper()

    try:
        while True:
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        scheduler.shutdown(wait=False)
        raise


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("PySentinel Scheduler stopped.")