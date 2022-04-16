import pytest

# from django.contrib.auth.models import User

# @pytest.fixture
# def user_1(db):
#     user = User.objects.create_user('test-user')
#     print('create-user')
#     return user

# @pytest.mark.django_db
# def test_set_check_password(user_1):
#     user_1.set_password('new-password')
#     assert user_1.check_password("new-password") is True

# @pytest.mark.django_db
# def test_set_check_password1(user_1):
#     assert user_1.username == 'test-user'


# def test_new_user(new_user2):
#     print(new_user2.is_staff)
#     assert new_user2.is_staff

# def test_new_user(user_factory):
#     print(user_factory.username)
#     assert True

# from django.contrib.auth.models import User

# @pytest.mark.django_db
# def test_new_useer(user_factory):
#     user = user_factory.create(username="test")
#     user2 = user_factory.create(username="test2")
#     print(user.username)
#     count = User.objects.all().count()
#     print(count)
#     assert True

def test_category(category_factory):
    category = category_factory.build()
    print(category)
    assert True

def test_tag(db, tag_factory):
    tag = tag_factory.build()
    print(tag)
    assert True

def test_blog(db, blog_factory, tag_factory):
    tag = tag_factory.create(name="sample1")
    tag2 = tag_factory.create(name="sample2")
    blog = blog_factory.create(tags=(tag, tag2))
    print(blog.title)
    print(blog.content)
    print(blog.category)
    print(blog.tags.all())
    assert True