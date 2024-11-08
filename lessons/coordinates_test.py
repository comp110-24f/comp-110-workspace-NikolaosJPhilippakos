from CQs.cq04.coordinates import get_coords


def test_get_coords() -> None:
    assert get_coords("Hello", "World") is None
