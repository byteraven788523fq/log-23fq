"""Simple log parsing helper.
Parses lines like:
2023-10-09 12:34:56,789 INFO Message
"""

import sys
import re
import json
from typing import Iterable, Dict

LOG_RE = re.compile(
    r'(?P<ts>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}) '
    r'(?P<lvl>[A-Z]+) (?P<msg>.*)'
)

def parse_log(lines: Iterable[str]) -> Iterable[Dict]:
    """Yield parsed log entries."""
    for line in lines:
        m = LOG_RE.match(line.strip())
        if m:
            yield m.groupdict()

def main() -> None:
    for entry in parse_log(sys.stdin):
        print(json.dumps(entry))

if __name__ == "__main__":
    main()