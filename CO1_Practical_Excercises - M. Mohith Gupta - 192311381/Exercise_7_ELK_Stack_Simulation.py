"""Exercise 7: Simulate Logstash parsing, Elasticsearch indexing, and Kibana aggregation."""
import re
from collections import Counter

LOG_PATTERN = re.compile(
    r'(?P<ip>\\S+) - - \\[(?P<timestamp>[^\\]]+)\\] '
    r'"(?P<method>\\S+) (?P<path>\\S+) (?P<protocol>[^"]+)" '
    r'(?P<status>\\d{3}) (?P<size>\\d+|-)'
)

def parse_log(line):
    match = LOG_PATTERN.match(line)
    if not match:
        return None
    event = match.groupdict()
    event["status"] = int(event["status"])
    event["size"] = int(event["size"]) if event["size"] != "-" else 0
    return event

if __name__ == "__main__":
    raw_logs = [
        '192.168.1.10 - - [16/Oct/2026:09:00:00 +0000] "GET /home HTTP/1.1" 200 1200',
        '192.168.1.11 - - [16/Oct/2026:09:01:00 +0000] "POST /login HTTP/1.1" 401 240',
        '192.168.1.10 - - [16/Oct/2026:09:02:00 +0000] "GET /admin HTTP/1.1" 403 180',
        '192.168.1.12 - - [16/Oct/2026:09:03:00 +0000] "GET /home HTTP/1.1" 200 1200',
    ]

    # Logstash-style: parse raw lines into structured events.
    events = [event for line in raw_logs if (event := parse_log(line)) is not None]
    print("Parsed structured events:")
    for event in events:
        print(event)

    # Elasticsearch-style: in-memory index keyed by event number.
    index = {f"event-{i+1}": event for i, event in enumerate(events)}
    print(f"\\nIndexed {len(index)} events (in-memory demonstration).")

    # Kibana-style: aggregate status codes and requested paths.
    status_counts = Counter(event["status"] for event in index.values())
    path_counts = Counter(event["path"] for event in index.values())
    print("\\nStatus-code aggregation:")
    for status, count in sorted(status_counts.items()):
        print(f"{status}: {count}")
    print("\\nRequest-path aggregation:")
    for path, count in sorted(path_counts.items()):
        print(f"{path}: {count}")
