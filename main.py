from core.aggregator import ThreatIntelligenceAggregator
from reports.report_generator import generate_json_report
from sources.sample_feed import SAMPLE_FEED


def display_results(aggregator):
    print("\n" + "=" * 55)
    print("        THREAT INTELLIGENCE AGGREGATOR")
    print("        Developed by: MUZAFFAR MUSHTAQ")
    print("=" * 55)

    indicators = aggregator.get_indicators()
    statistics = aggregator.get_statistics()

    print(f"\nTotal Valid IOCs: {len(indicators)}")

    print("\nIOC Statistics:")
    for ioc_type, count in sorted(statistics.items()):
        print(f"  {ioc_type.upper():8} : {count}")

    print("\nCollected Indicators:")

    for number, indicator in enumerate(indicators, start=1):
        print(
            f"  {number:02d}. "
            f"[{indicator['type'].upper():6}] "
            f"{indicator['value']} "
            f"(Source: {indicator['source']})"
        )

    print("\n" + "=" * 55)


def main():
    aggregator = ThreatIntelligenceAggregator()

    added = aggregator.add_feed(
        SAMPLE_FEED,
        source="Safe Sample Feed",
    )

    print(f"Loaded {added} valid indicators.")

    display_results(aggregator)

    report_path = generate_json_report(
        aggregator.get_indicators(),
        aggregator.get_statistics(),
        "reports/threat_intelligence_report.json",
    )

    print(f"\nJSON report generated: {report_path}")


if __name__ == "__main__":
    main()
