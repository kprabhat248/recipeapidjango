from unittest.mock import patch
from django.core.management import call_command
from django.test import SimpleTestCase

@patch('core.management.commands.wait_for_db.Command.check')
class WaitForDbCommandTest(SimpleTestCase):
    def test_wait_db(self, patched_check):
        # Mock the return value of the check method
        patched_check.return_value = True
        
        # Call the wait_for_db management command
        call_command('wait_for_db')
        
        # Assert that the check method was called with the expected arguments
        patched_check.assert_called_once_with(database=['default'])
