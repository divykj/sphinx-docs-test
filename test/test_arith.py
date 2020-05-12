from sphinx_docs_test.arith import add, sub, mul, div


def test_add():
    assert add(100, 10) == 110


def test_sub():
    assert sub(100, 10) == 90


def test_mul():
    assert mul(100, 10) == 1000


def test_div():
    assert div(100, 10) == 10

