#Logging implementation
# this is  the custom login

#installing operating system and logging
import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]" #initialize logging stream by saving ASCII timestamp and then save log level (info level log or bug log) then module , which module is running and then message we want to print

log_dir = "logs" # first a log directory is created
log_filepath = os.path.join(log_dir,"running_logs.log") # inside that running log directory is created
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath), # File handler will create teh log folder and save all the logging information
        logging.StreamHandler(sys.stdout) # Stream handler will print the log in the terminal
    ]
)

logger = logging.getLogger("mlProjectLogger") # finally initialize logger here
