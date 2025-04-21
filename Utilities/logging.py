import logging

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename="Logs/automation.log",  # Path to the log file
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p',
                            level=logging.INFO)
        logger = logging.getLogger()
        return logger
