import json
from datetime import datetime
from pathlib import Path


def generate_json_report(indicators, statistics, output_file):
    """Generate a JSON threat-intelligence report."""

    report = {
        "report_title": "Threat Intelligence Aggregation Report",
        "generated_by": "MUZAFFAR MUSHTAQ",
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "total_indicators": len(indicators),
        "statistics": statistics,
        "indicators": indicators,
    }

    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8") as file:
        json.dump(report, file, indent=4)

    return output_path
