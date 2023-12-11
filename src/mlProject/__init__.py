# another constructor file, this time for logging
# this can be reused with only minor tweaks for other projects

import logging
import os
import sys

logging_str = (
    "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"  # another standard?
)

log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),  # saves log in a file
        logging.StreamHandler(sys.stdout),  # shows log in terminal
    ],
)

logger = logging.getLogger("mlProjectLogger")  # initialising the logger
