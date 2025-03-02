import sys
from networksecurity.logging import logger

class NetworkSecurityException(Exception):
    def __init__(self, error_message: str, error_details: sys):
        super().__init__(error_message)
        self.error_message = error_message
        self.error_details = error_details

    def __str__(self):
        return f"Error occurred: {self.error_message}, Details: {self.error_details}"

