import logging
from sqlalchemy import text, inspect

logger = logging.getLogger(__name__)

MIGRATIONS = [
    ("members", "password_hash", "VARCHAR(200)"),
    ("members", "telegram_chat_id", "VARCHAR(100)"),
    ("members", "notification_pref", "VARCHAR(20) DEFAULT 'email'"),
]


def run_migrations(engine):
    with engine.connect() as conn:
        inspector = inspect(engine)
        for table, column, col_type in MIGRATIONS:
            existing = [c["name"] for c in inspector.get_columns(table)]
            if column not in existing:
                conn.execute(text(f"ALTER TABLE {table} ADD COLUMN {column} {col_type}"))
                logger.info(f"Migration: added {table}.{column}")
        conn.commit()
