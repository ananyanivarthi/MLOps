import logging
import os
from from_root import from_root
from datetime import datetime

# Generate log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the root path and log directory path
log_dir = os.path.join(os.getcwd(), 'logs')

# Debugging: Print the resolved log directory path
print(f"Log directory path: {log_dir}")

# Ensure the logs directory exists in the correct path
os.makedirs(log_dir, exist_ok=True)
print(f"Directory created (or already exists): {log_dir}")

# Full path for the log file
logs_path = os.path.join(log_dir, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=logs_path,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)

