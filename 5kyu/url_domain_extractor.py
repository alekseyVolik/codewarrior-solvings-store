"""kata id: https://www.codewars.com/kata/514a024011ea4fb54200004b"""

import re

import pytest


def domain_name(url: str) -> str:
    match_domain = re.search(r'(?!w)(?!\.)[-0-9a-zA-Z]*(?=\.)', url)
    return match_domain.group()


@pytest.mark.parametrize(
    'url, domain',
    [
        ("http://www.codewars.com/kata/", "codewars"),
        ("https://hyphen-site.org", "hyphen-site"),
        ("csxhfoctygtk.tv", "csxhfoctygtk"),
        ("http://google.com", "google"),
        ("http://google.co.jp", "google"),
        ("www.xakep.ru", "xakep"),
        ("https://youtube.com", "youtube")
    ]
)
def test_domain_test(url, domain):
    assert domain_name(url) == domain

