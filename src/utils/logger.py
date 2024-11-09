import logging

class Logger:
    def __init__(self, logger_name: str, log_level: int = logging.INFO):
        """Initializes a new Logger object which can be used for logging across the project."""
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(log_level)

        # Create a console handler to log to the console
        console_handler = logging.StreamHandler()
        console_handler.setLevel(log_level)

        # Define a formatter and set it for the console handler
        formatter = logging.Formatter('%(asctime)s %(levelname)s [%(name)s] - %(message)s')
        console_handler.setFormatter(formatter)

        # Add the console handler to the logger
        # Check if handler is already added to avoid duplicate logs
        if not self.logger.handlers:
            self.logger.addHandler(console_handler)

    def get_logger(self):
        return self.logger


# Usage example
if __name__ == '__main__':
    # Instantiate the logger
    project_logger = Logger("ProjectLogger").get_logger()

    # Log some messages
    project_logger.info("This is an info message.")
    project_logger.warning("This is a warning message.")
    project_logger.error("This is an error message.")