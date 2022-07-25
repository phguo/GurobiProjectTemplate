import logging
import logging.handlers

logger = logging.getLogger("log")
stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler(filename="log.log")
logger.setLevel(logging.DEBUG)
stream_handler.setLevel(logging.INFO)
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s | %(message)s")
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
logger.addHandler(file_handler)
