from sphinx_docs_test.list import sort, revsort


def test_sort():
    assert sort([3, 1, 5, 2, 4]) == [1, 2, 3, 4, 5]


def test_revsort():
    assert revsort([3, 1, 5, 2, 4]) == [5, 4, 3, 2, 1]
