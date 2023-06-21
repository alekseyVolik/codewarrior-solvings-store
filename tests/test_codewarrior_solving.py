import pytest

from kyu5.url_domain_extractor import domain_name
from kyu4.sum_of_intervals import sum_of_intervals


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


@pytest.mark.parametrize(
    'intervals, _sum',
    [
        ([(1, 5)], 4),
        ([1, 5], [10, 20], [1, 6], [16, 19], [5, 11], 19)
    ]
)
def test_sum_of_intervals(intervals, _sum):
    assert sum_of_intervals(intervals) == _sum
