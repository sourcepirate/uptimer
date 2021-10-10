"""Main module."""

import logging
from datetime import datetime
from urllib.parse import urlparse
from typing import Any, Dict, List

import requests


def check_domain(domain_url: str) -> Dict[str, Any]:

    try:
        current_time = datetime.now()
        session = requests.Session()
        response = session.get(domain_url)
        return {
            "healthy": response.ok,
            "latency": response.elapsed.microseconds // 1000,
            "content_type": response.headers.get("Content-Type"),
            "current_time": int(current_time.timestamp()),
            "domain_url": domain_url,
            "domain": urlparse(domain_url).hostname,
        }
    except Exception:
        return {
            "healthy": False,
            "latency": 0,
            "current_time": int(current_time.timestamp()),
            "domain_url": domain_url,
            "domain": urlparse(domain_url).hostname,
        }


def access_domains(domains: List[str]) -> Dict[str, Any]:
    responses = []
    for domain_url in domains:
        try:
            responses.append(check_domain(domain_url))
        except Exception:
            pass
    return responses
