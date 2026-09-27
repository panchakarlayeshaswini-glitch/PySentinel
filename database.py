import aiosqlite


DATABASE_NAME = "pysentinel.db"


async def initialize_database():

    async with aiosqlite.connect(DATABASE_NAME) as db:

        await db.execute("""
            CREATE TABLE IF NOT EXISTS alerts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                url TEXT NOT NULL,
                keyword TEXT NOT NULL,
                UNIQUE(url, keyword)
            )
        """)

        await db.commit()


async def save_alert(url, keyword):

    async with aiosqlite.connect(DATABASE_NAME) as db:

        cursor = await db.execute(
            """
            INSERT OR IGNORE INTO alerts (url, keyword)
            VALUES (?, ?)
            """,
            (url, keyword)
        )

        await db.commit()

        return cursor.rowcount > 0