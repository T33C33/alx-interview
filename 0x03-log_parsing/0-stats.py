#!/usr/bin/python3
import sys

# Initialize variables
total_file_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_stats():
    """Prints the accumulated statistics."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

try:
    for line in sys.stdin:
        line_count += 1
        try:
            # Split and parse the log line
            parts = line.split()
            if len(parts) < 7:
                continue

            # Extract file size and status code
            file_size = int(parts[-1])
            status_code = int(parts[-2])

            # Update total file size
            total_file_size += file_size

            # Update the status code count if it's a valid code
            if status_code in status_codes:
                status_codes[status_code] += 1

        except (ValueError, IndexError):
            # Skip the line if it doesn't conform to the format
            continue

        # After every 10 lines, print the statistics
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # Handle the keyboard interruption (Ctrl + C)
    print_stats()
    raise

# Print final stats after exiting the loop
print_stats()
