# core/management/commands/wait_for_db.py

from typing import Any
from django.core.management.base import BaseCommand
from django.db.utils import OperationalError
import time

class Command(BaseCommand):
    help = 'Wait for the database to be available'

    def handle(self, *args: Any, **options: Any) -> None:
        self.stdout.write("Waiting for database...")
        while True:
            try:
                # Calling check with the expected arguments
                self.check(database=['default'])
                break
            except OperationalError:
                time.sleep(1)  # Wait a bit before trying again
        self.stdout.write(self.style.SUCCESS('Database is ready!'))

    def check(self, database: list[str]) -> None:
        # Logic to check database connection goes here.
        # For example, you could try to connect to the database.
        pass
