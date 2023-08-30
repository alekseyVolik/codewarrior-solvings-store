import pytest

from kyu5 import (
    url_domain_extractor,
    max_subarray_sum
)


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
    assert url_domain_extractor.domain_name(url) == domain


@pytest.mark.parametrize(
    '_array, _sum',
    [
        ([], 0),
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([-2, -1, -3, -4, -1, -2, -1, -5, -4], 0),
        ([7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43], 155)
    ]
)
def test_max_sequence(_array, _sum):
    assert max_subarray_sum.max_sequence(_array) == _sum
