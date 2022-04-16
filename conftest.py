from pytest_factoryboy import register
from tests.factories import UserFactory, CategoryFactory, TagFactory, BlogFactory

register(UserFactory)
register(CategoryFactory)
register(TagFactory)
register(BlogFactory)