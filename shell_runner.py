import subprocess
from utils.logger import get_logger

logger = get_logger("shell_runner")

def run_command(cmd):
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
        logger.info(output.decode().strip())
    except subprocess.CalledProcessError as e:
        logger.error(f"Command failed: {e.output.decode()}")

if __name__ == "__main__":
    run_command("kubectl get pods -A")
