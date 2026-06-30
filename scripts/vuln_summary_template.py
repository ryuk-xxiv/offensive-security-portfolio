"""
Sanitized vulnerability summary helper.

Purpose:
    Demonstrates safe reporting automation by summarizing vulnerability counts
    from a CSV export. Update field names as needed for your own sanitized data.
"""

import csv
from collections import Counter
from pathlib import Path


def summarize_vulnerabilities(csv_path: str, severity_field: str = "Severity") -> Counter:
    path = Path(csv_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {csv_path}")

    counts = Counter()
    with path.open(newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        if severity_field not in reader.fieldnames:
            raise ValueError(f"Missing expected field: {severity_field}")
        for row in reader:
            severity = row.get(severity_field, "Unknown").strip() or "Unknown"
            counts[severity] += 1
    return counts


if __name__ == "__main__":
    # Example usage with sanitized data only:
    # print(summarize_vulnerabilities("sample_findings.csv"))
    pass
