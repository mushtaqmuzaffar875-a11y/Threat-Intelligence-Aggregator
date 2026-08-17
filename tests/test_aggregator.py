import unittest

from core.aggregator import ThreatIntelligenceAggregator
from core.normalizer import detect_ioc_type, normalize_ioc
from core.validator import validate_ioc


class TestThreatIntelligenceAggregator(unittest.TestCase):

    def setUp(self):
        self.aggregator = ThreatIntelligenceAggregator()

    def test_ip_detection(self):
        self.assertEqual(
            detect_ioc_type("192.0.2.10"),
            "ip"
        )

    def test_domain_detection(self):
        self.assertEqual(
            detect_ioc_type("example-threat.test"),
            "domain"
        )

    def test_url_detection(self):
        self.assertEqual(
            detect_ioc_type("https://example-threat.test/login"),
            "url"
        )

    def test_hash_detection(self):
        self.assertEqual(
            detect_ioc_type(
                "5d41402abc4b2a76b9719d911017c592"
            ),
            "md5"
        )

    def test_valid_ip(self):
        self.assertTrue(
            validate_ioc("192.0.2.10", "ip")
        )

    def test_invalid_ip(self):
        self.assertFalse(
            validate_ioc("999.999.999.999", "ip")
        )

    def test_normalization(self):
        self.assertEqual(
            normalize_ioc("Example-Threat.TEST.", "domain"),
            "example-threat.test"
        )

    def test_add_indicator(self):
        result = self.aggregator.add_indicator(
            "192.0.2.10",
            source="Test Feed"
        )

        self.assertTrue(result)
        self.assertEqual(len(self.aggregator.get_indicators()), 1)

    def test_duplicate_detection(self):
        self.aggregator.add_indicator(
            "192.0.2.10",
            source="Test Feed"
        )

        self.aggregator.add_indicator(
            "192.0.2.10",
            source="Test Feed"
        )

        self.assertEqual(
            len(self.aggregator.get_indicators()),
            1
        )

    def test_statistics(self):
        self.aggregator.add_indicator(
            "192.0.2.10",
            source="Test Feed"
        )

        self.aggregator.add_indicator(
            "example-threat.test",
            source="Test Feed"
        )

        statistics = self.aggregator.get_statistics()

        self.assertEqual(statistics["ip"], 1)
        self.assertEqual(statistics["domain"], 1)


if __name__ == "__main__":
    unittest.main()
