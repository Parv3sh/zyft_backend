import pytest

from zyft_backend.tag_model_number import Feature


@pytest.fixture
def feature():
    return Feature(
        (
            "HUB6630B",
            "CA416",
            "HU6630B",
            "MDC9082-1",
            "CA960",
            "ACL104RA2-10",
            "DBA2182S",
            "278062",
            "ACL104RA2-3",
            "IEBC001",
            "XYZ",
        )
    )


def test_tag_html(feature):
    assert feature.tag_html("<html> <body> ABC HU6630B XYZ HU6630B </body><html>") == [
        ["HU6630B", {"start_index": 18, "end_index": 24}],
        ["XYZ", {"start_index": 26, "end_index": 28}],
        ["HU6630B", {"start_index": 30, "end_index": 36}],
    ]
