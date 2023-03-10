import pytest

from kyu5.url_domain_extractor import domain_name


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
