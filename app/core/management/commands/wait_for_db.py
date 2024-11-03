from typing import Any
from django.core.management.base import BaseCommand
from django.db.utils import OperationalError
import time
from psycopg2 import OperationalError as Psycopg2Error


class Command(BaseCommand):
    help = 'Wait for the database to be available'

    def handle(self, *args: Any, **options: Any) -> None:
        self.stdout.write("Waiting for database...")
        while True:
            try:
                self.check_database_connection(database=['default'])
                break
            except (Psycopg2Error, OperationalError):
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database is ready!'))

    def check_database_connection(self, database: list[str]) -> None:
        # Logic to check database connection
        pass
