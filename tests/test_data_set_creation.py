import pytest

from zyft_backend.data_set_creation import DataSetCreation


@pytest.fixture
def dsc():
    return DataSetCreation("zyft_backend/data/data_analysis_test_data (2).csv")


def test_get_upcs(dsc):
    dsc.get_upcs()
    assert len(dsc.upcs) == 240


def test_get_res(dsc):
    dsc.get_upcs()
    dsc.get_res()
    assert len(dsc.res) == 240


def test_count_diff_titles(dsc):
    dsc.get_upcs()
    dsc.get_res()
    res_gt_1 = [row for row in dsc.res if row["counter"] > 1]
    assert dsc.count_diff_titles(res_gt_1) == 80


def test_transform(dsc):
    dsc.transform()
    assert len(dsc.res) == 240


def test_write_csv(dsc):
    dsc.transform()
    dsc.write_csv(dsc.path.replace("data", "tmp").replace(".csv", "_transformed.csv"))
    assert True


if __name__ == "__main__":
    pytest.main()
