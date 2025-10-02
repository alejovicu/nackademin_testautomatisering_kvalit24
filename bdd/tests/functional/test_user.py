"""User feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('features\user.feature', 'Publishing the article')
def test_publishing_the_article():
    """Publishing the article."""


@given('I am a new potential customer​')
def _():
    """I am a new potential customer​."""
    raise NotImplementedError


@when('I signup in the app​')
def _():
    """I signup in the app​."""
    raise NotImplementedError


@then('I should be able to log in with my new user')
def _():
    """I should be able to log in with my new user."""
    raise NotImplementedError

