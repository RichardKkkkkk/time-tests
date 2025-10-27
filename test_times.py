import pytest
from times import compute_overlap_time, time_range

def test_generic_case():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    expected = [("2010-01-12 10:30:00","2010-01-12 10:37:00"), ("2010-01-12 10:38:00", "2010-01-12 10:45:00")]
    assert compute_overlap_time(large, short) == expected

def test_range_dont_overlap():
    first = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    second = time_range("2010-01-12 12:30:00", "2010-01-12 12:45:00", 2, 60)
    expected = []
    assert compute_overlap_time(first, second) == expected

def test_both_have_intervals():
    first = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", 4, 60)
    second = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    expected = [("2010-01-12 10:30:15", "2010-01-12 10:37:00"), ("2010-01-12 10:38:00", "2010-01-12 10:45:00")]
    assert compute_overlap_time(first, second) == expected

def test_sameEnd_otherStart():
    first = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    second = time_range("2010-01-12 12:00:00", "2010-01-12 13:00:00", 2, 60)
    expected = []
    assert compute_overlap_time(first, second) == expected

def test_time_range_backwards_error():
    with pytest.raises(ValueError, match="end_time must be after start_time"):
        time_range("2010-01-12 12:00:00", "2010-01-12 10:00:00")


    