from unittest.mock import patch
from django.core.management import call_command
from django.test import SimpleTestCase
from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError


@patch(
    'core.management.commands.wait_for_db.Command.check_database_connection'
)
class WaitForDbCommandTest(SimpleTestCase):
    def test_wait_db(self, patched_check):
        # Mock the return value of the check_database_connection method
        patched_check.return_value = True
        # Call the wait_for_db management command
        call_command('wait_for_db')
        # Assert that the dbconnection was called with the expec argument
        patched_check.assert_called_once_with(database=['default'])

    @patch('time.sleep')
    def test_wait_for_db_delay(self, patched_sleep, patched_check):
        # Simulate database being unavailable initially
        patched_check.side_effect = (
            [Psycopg2Error] * 2 +
            [OperationalError] * 3 +
            [True]
        )

        # Call the wait_for_db management command
        call_command('wait_for_db')

        # Assert db conn was called the expected number of times
        self.assertEqual(patched_check.call_count, 6)

        # Assert the last call was with the expected argument
        patched_check.assert_called_with(database=['default'])
