"""User​ feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('features\user.feature', 'Succesful Login')
def test_succesful_login():
    """Succesful Login."""


@given('I am an authenticated user​')
def _():
    """I am an authenticated user​."""
    raise NotImplementedError


@when('I log in into the application​')
def _():
    """I log in into the application​."""
    raise NotImplementedError


@then('I should see all my products')
def _():
    """I should see all my products."""
    raise NotImplementedError
