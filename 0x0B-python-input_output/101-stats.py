#!/usr/bin/python3

"""
A script that reads stdin line by line and computes metrics
"""

import sys
import signal
from collections import defaultdict

# Constants for status codes
STATUS_CODES = [200, 301, 400, 401, 403, 404, 405, 500]

# Variables to track statistics
total_file_size = 0
status_code_counts = defaultdict(int)
line_count = 0

def print_statistics():
    """
    Print the computed statistics.

    Args:
        None

    Returns:
        None

    Raises:
        None
    """
    print(f"Total file size: {total_file_size}")
    for status_code in sorted(status_code_counts.keys()):
        count = status_code_counts[status_code]
        print(f"{status_code}: {count}")

def signal_handler(sig, frame):
    """
    Signal handler for keyboard interruption (CTRL + C).

    Args:
        sig (int): Signal number
        frame (frame): Current stack frame

    Returns:
        None

    Raises:
        None
    """
    print_statistics()
    sys.exit(0)

# Set the signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line = line.strip()

        # Parse the line and extract the file size and status code
        _, _, _, _, file_size = line.rsplit(' ', 4)
        file_size = int(file_size)
        status_code = int(line.split()[8])

        # Update the total file size
        total_file_size += file_size

        # Update the status code count
        status_code_counts[status_code] += 1

        # Increment the line count
        line_count += 1

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print_statistics()

except KeyboardInterrupt:
    # Handle keyboard interruption (CTRL + C)
    print_statistics()
    sys.exit(0)
