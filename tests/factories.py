import factory
from faker import Faker
from django.contrib.auth.models import User
from blog import models

fake = Faker('JA_jp')

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = fake.name()
    is_staff = 'True'


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Category

    name = fake.job()


class TagFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Tag

    name = fake.word()


class BlogFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Blog

    title = "test_blog_title"
    content = fake.text()
    category = factory.SubFactory(CategoryFactory)

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for tag in extracted:
                self.tags.add(tag)