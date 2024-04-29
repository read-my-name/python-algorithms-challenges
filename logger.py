import logging
from datetime import datetime
import threading

class CustomLogger:
    def __init__(self):
        self.log_file   = None
        self.logger     = None
        self.lock       = threading.Lock()  # Initialize a lock
        self.line       = 50

    def setup_logger(self, line_limit: int = 50):
        self.line = line_limit
        # Check if the current log file has exceeded the line limit or if it exists
        current_datetime = datetime.now().strftime('%Y%m%d_%H%M%S_%f')[:-3]
        log_file = f"logfile_{current_datetime}.txt"
        self.log_file = log_file

        # Create a logger
        self.logger = logging.getLogger('my_logger')
        self.logger.setLevel(logging.DEBUG)

        # Create a file handler and set the level to DEBUG
        file_handler = logging.FileHandler(self.log_file)
        file_handler.setLevel(logging.DEBUG)

        # Create a formatter and set the format for the logs
        formatter = logging.Formatter('%(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        # Add the file handler to the logger
        self.logger.addHandler(file_handler)

    def count_lines(self):
        with self.lock:  # Acquire the lock before counting lines
            try:
                with open(self.log_file, 'r') as file:
                    lines = file.readlines()
                    count = len(lines)
                    print("Filename and line limit:", self.log_file, count)
                    return count
            except FileNotFoundError:
                print("File not found:", self.log_file)
                return 0

    def set_lines(self, line_limit: int):  # Set the line limit
        self.line = line_limit

    def __call__(self, log_level, message):
        # Set up logger if not already set up
        if not self.logger or self.count_lines() >= self.line:
            # print("Logger not set up or log file has exceeded the line limit.")
            self.setup_logger()

        with self.lock:  # Acquire the lock before logging
            # Log the message with the specified level
            if log_level == logging.DEBUG:
                self.logger.debug(message)
            elif log_level == logging.INFO:
                self.logger.info(message)
            elif log_level == logging.WARNING:
                self.logger.warning(message)
            elif log_level == logging.ERROR:
                self.logger.error(message)
            elif log_level == logging.CRITICAL:
                self.logger.critical(message)



# # Create an instance of CustomLogger
# LOGGER = CustomLogger()

# for i in range(60):
#     # Now you can use LOGGER to log messages
#     LOGGER(logging.DEBUG, 'This is a debug message')
#     # LOGGER(logging.INFO, 'This is a release message')
#     # LOGGER(logging.WARNING, 'This is a warning message')
#     # LOGGER(logging.ERROR, 'This is an error message')
#     # LOGGER(logging.CRITICAL, 'This is a critical message')