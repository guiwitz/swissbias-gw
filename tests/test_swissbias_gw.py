from swissbias_gw.algos import add_one


def test_add_one():
    out = add_one(1)
    assert out == 2, f"Expected 2, but got {out}"
