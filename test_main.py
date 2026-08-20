"""
Tests for the polling place lookup logic in main.py.
Run with: pytest
"""
import pytest
from main import get_polling_place


def test_known_voter_alice_johnson():
    result = get_polling_place("60601", 567)
    assert result is not None
    assert result[0] == "Central Community Center"
    assert result[1] == "100 Main St"


def test_known_voter_jack_taylor():
    result = get_polling_place("60085", 630)
    assert result is not None
    assert result[0] == "Lakeside Recreation Center"
    assert result[1] == "600 Lake Dr"


def test_known_voter_david_garcia():
    result = get_polling_place("60540", 229)
    assert result is not None
    assert result[0] == "Westside School Gym"
    assert result[1] == "300 West St"


def test_no_match_returns_none():
    result = get_polling_place("99999", 1)
    assert result is None


def test_correct_zip_wrong_precinct_returns_none():
    result = get_polling_place("60601", 999)
    assert result is None