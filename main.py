#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  : Matthew Davidson
# Created Date: 2023-01-23
# version ='1.0'
# ---------------------------------------------------------------------------
"""a_short_project_description"""
# ---------------------------------------------------------------------------

import threading
import time
import logging

from src.log_aggregator.log_client import create_log_handler
from src.log_aggregator.log_server import LogServer


# Function to run the server
def run_server():
    log_server = LogServer(host="127.0.0.1", port=9000, log_file="server_logs.txt")
    log_server.start()


def start_server_thread():
    # Start the server in a separate thread
    server_thread = threading.Thread(target=run_server)
    server_thread.daemon = (
        True  # Daemonize the server thread so it shuts down with the main program
    )
    server_thread.start()

    # Wait a bit to ensure the server has started
    time.sleep(2)


# Define the main function to create the server and client
def main():
    # Start the server
    start_server_thread()

    # Initialize the client
    remote_logging_handler = create_log_handler(
        server_host="127.0.0.1", server_port=9000
    )

    # Create a logger and add the handler
    logger = logging.getLogger("ApplicationLogger")
    logger.setLevel(logging.INFO)
    logger.addHandler(remote_logging_handler)

    # Log some messages using the logger
    for i in range(5):
        logger.info(f"Log message {i + 1} from application")
        time.sleep(1)


if __name__ == "__main__":
    main()
