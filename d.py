# logger.py
from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def log(self, message):
        pass


# implementation of Logger using the 'logging' library
class LoggingLogger(Logger):
    def log(self, message):
        # Use the 'logging' library for logging
        print(f"Logging: {message}")


# implementation of Logger using the 'loguru' library
class LoguruLogger(Logger):
    def log(self, message):
        # Use the 'loguru' library for logging
        print(f"Loguru: {message}")


# application.py
class Application:
    def __init__(self, logger: Logger):
        self.logger = logger

    def do_something(self):
        # Application logic
        self.logger.log("Doing something in the application")


# d.py
if __name__ == "__main__":
    # Example usage
    logging_logger = LoggingLogger()
    application_with_logging = Application(logging_logger)
    application_with_logging.do_something()

    loguru_logger = LoguruLogger()
    application_with_loguru = Application(loguru_logger)
    application_with_loguru.do_something()
