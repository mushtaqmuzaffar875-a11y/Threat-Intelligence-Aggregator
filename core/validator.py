import ipaddress
import re


def is_valid_ip(value: str) -> bool:
    try:
        ipaddress.ip_address(value)
        return True
    except ValueError:
        return False


def is_valid_domain(value: str) -> bool:
    pattern = r"^(?=.{1,253}$)(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$"
    return bool(re.fullmatch(pattern, value))


def is_valid_url(value: str) -> bool:
    pattern = r"^https?://[^\s]+$"
    return bool(re.fullmatch(pattern, value, re.IGNORECASE))


def is_valid_hash(value: str) -> bool:
    return bool(
        re.fullmatch(
            r"(?:[a-fA-F0-9]{32}|[a-fA-F0-9]{40}|[a-fA-F0-9]{64})",
            value,
        )
    )


def validate_ioc(value: str, ioc_type: str) -> bool:
    if not value or not ioc_type:
        return False

    if ioc_type == "ip":
        return is_valid_ip(value)

    if ioc_type == "domain":
        return is_valid_domain(value)

    if ioc_type == "url":
        return is_valid_url(value)

    if ioc_type in {"md5", "sha1", "sha256", "hash"}:
        return is_valid_hash(value)

    return False

