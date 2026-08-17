import re


def normalize_ioc(value: str, ioc_type: str) -> str:
    """
    Normalize an Indicator of Compromise (IOC).
    """

    value = value.strip()

    if ioc_type == "domain":
        return value.lower().rstrip(".")

    if ioc_type == "url":
        return value.strip().rstrip("/")

    if ioc_type == "ip":
        return value.strip()

    if ioc_type == "hash":
        return value.lower()

    return value


def detect_ioc_type(value: str) -> str:
    """
    Detect the likely IOC type.
    """

    value = value.strip()

    if re.fullmatch(
        r"(?:\d{1,3}\.){3}\d{1,3}",
        value
    ):
        return "ip"

    if re.match(r"^https?://", value, re.IGNORECASE):
        return "url"

    if re.fullmatch(r"[a-fA-F0-9]{32}", value):
        return "md5"

    if re.fullmatch(r"[a-fA-F0-9]{40}", value):
        return "sha1"

    if re.fullmatch(r"[a-fA-F0-9]{64}", value):
        return "sha256"

    if re.fullmatch(
        r"(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}",
        value
    ):
        return "domain"

    return "unknown"

