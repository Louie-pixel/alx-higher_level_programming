#!/usr/bin/env python3

import sys
from collections import defaultdict

def print_stats(total_size, status_counts):
    """Prints accumulated metrics."""
    print("File size: {}".format(total_size))
    for code, count in sorted(status_counts.items()):
        print("{}: {}".format(code, count))

def main():
    total_size = 0
    status_counts = defaultdict(int)
    valid_status_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}
    line_count = 0

    try:
        for line in sys.stdin:
            try:
                parts = line.split()
                file_size = int(parts[-1])
                status_code = parts[-2]
                if status_code in valid_status_codes:
                    total_size += file_size
                    status_counts[status_code] += 1
                    line_count += 1
            except (IndexError, ValueError):
                pass

            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        print_stats(total_size, status_counts)

if __name__ == "__main__":
    main()
