#!/usr/bin/env python3

from selene.support.shared import browser
from selene import be, have
from selene.core.condition import Condition
import pytest

selene_search_query = 'selene python'
invalid_search_query = 'gfdbvnthohg'
selene_search_result = 'User-oriented Web UI browser tests in Python'

@pytest.fixture
def open_browser():
    browser.open('https://google.com') #.maximize()

def test_search(text: str, condition: Condition):
    search_field = browser.element('[name="q"]')
    search_field.should(be.blank).type(text).press_enter()
    browser.element('#search').should(condition)

def test_able_to_find_selene_in_google(open_browser):
    test_search(selene_search_query, have.text(selene_search_result))

def test_unable_to_find_invalid_search_result_in_google(open_browser):
    test_search(invalid_search_query, have.no.texts())
