"""
Safe sample threat-intelligence feed.

These indicators are synthetic examples intended for testing
and educational purposes only.
"""

SAMPLE_FEED = [
    {
        "value": "192.0.2.10",
        "type": "ip",
    },
    {
        "value": "198.51.100.25",
        "type": "ip",
    },
    {
        "value": "203.0.113.50",
        "type": "ip",
    },
    {
        "value": "example-threat.test",
        "type": "domain",
    },
    {
        "value": "malware-simulation.test",
        "type": "domain",
    },
    {
        "value": "https://example-threat.test/login",
        "type": "url",
    },
    {
        "value": "https://malware-simulation.test/payload",
        "type": "url",
    },
    {
        "value": "5d41402abc4b2a76b9719d911017c592",
        "type": "md5",
    },
    {
        "value": "a9993e364706816aba3e25717850c26c9cd0d89d",
        "type": "sha1",
    },
    {
        "value": (
            "9f86d081884c7d659a2feaa0c55ad015"
            "a3bf4f1b2b0b822cd15d6c15b0f00a08"
        ),
        "type": "sha256",
    },
]
