import pytest
from bs4 import BeautifulSoup
from zyft_backend.html_to_xpath import HtmlToXpath


@pytest.fixture
def html():
    return """
    <ul id='favouriteThings' class='myList' zyft_node_id='123456'> <li id='item1'> Thing 1</li>
    <li id='item2'> Thing 2</li>
    <li id='item3'> Thing 3</li>
    </ul>
    """


@pytest.fixture
def html_to_xpath(html):
    return HtmlToXpath(html)


def test_get_all_xpath_queries(html_to_xpath):
    assert html_to_xpath.get_all_xpath_queries() == [
        "//ul[1]",
    ]


def test_get_xpath_query(html_to_xpath):
    assert (
        html_to_xpath.get_xpath_query(
            BeautifulSoup(html_to_xpath.html, "html.parser").find(
                attrs={"zyft_node_id": "123456"}
            )
        )
        == "//ul[1]"
    )
