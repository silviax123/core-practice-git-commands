import pytest


def always_returns_true():
    print("Hi friends!")
    return False


def test_always_returns_true():
    assert always_returns_true()
