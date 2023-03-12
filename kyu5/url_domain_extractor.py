"""kata id: https://www.codewars.com/kata/514a024011ea4fb54200004b"""

import re

import pytest


def domain_name(url: str) -> str:
    match_domain = re.search(r'(?!w)(?!\.)[-0-9a-zA-Z]*(?=\.)', url)
    return match_domain.group()
