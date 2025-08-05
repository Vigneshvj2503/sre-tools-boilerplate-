from prometheus_client import start_http_server, Counter
import time

API_FAILURES = Counter('api_failures_total', 'Total API failures')

def simulate_check():
    while True:
        API_FAILURES.inc()  # Simulate failure metric
        time.sleep(5)

if __name__ == "__main__":
    start_http_server(8000)
    simulate_check()
