from core.normalizer import detect_ioc_type, normalize_ioc
from core.validator import validate_ioc


class ThreatIntelligenceAggregator:
    """Collect, normalize, validate, and deduplicate threat indicators."""

    def __init__(self):
        self.indicators = []

    def add_indicator(self, value: str, ioc_type: str = None, source: str = "unknown"):
        value = value.strip()

        if not value:
            return False

        if ioc_type is None:
            ioc_type = detect_ioc_type(value)

        normalized = normalize_ioc(value, ioc_type)

        if ioc_type in {"md5", "sha1", "sha256"}:
            valid = validate_ioc(normalized, ioc_type)
        else:
            valid = validate_ioc(normalized, ioc_type)

        if not valid:
            return False

        indicator = {
            "value": normalized,
            "type": ioc_type,
            "source": source,
        }

        if indicator not in self.indicators:
            self.indicators.append(indicator)

        return True

    def add_feed(self, feed: list, source: str = "unknown"):
        added = 0

        for item in feed:
            if isinstance(item, dict):
                value = item.get("value", "")
                ioc_type = item.get("type")
            else:
                value = str(item)
                ioc_type = None

            if self.add_indicator(value, ioc_type, source):
                added += 1

        return added

    def get_indicators(self):
        return list(self.indicators)

    def get_statistics(self):
        statistics = {}

        for indicator in self.indicators:
            ioc_type = indicator["type"]
            statistics[ioc_type] = statistics.get(ioc_type, 0) + 1

        return statistics
