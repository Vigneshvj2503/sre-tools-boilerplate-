import requests
import time
from collections import Counter
from utils.logger import get_logger

logger = get_logger("api_checker")

def check_api(url, count=10, timeout=5):
    status_codes = []
    start_time = time.time()

    for i in range(count):
        try:
            response = requests.get(url, timeout=timeout)
            status_codes.append(response.status_code)
        except requests.exceptions.RequestException as e:
            logger.warning(f"Request failed: {e}")
            status_codes.append("Failed")

    total_time = time.time() - start_time
    logger.info(f"Total time: {total_time:.2f}s")
    logger.info(f"Status Summary: {Counter(status_codes)}")

if __name__ == "__main__":
    check_api("https://api.github.com", count=100)
