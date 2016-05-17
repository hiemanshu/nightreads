from django.db import models
from django.contrib.auth.models import User

from nightreads.utils import TimeStampMixin
from nightreads.posts.models import Tag


class UserTag(TimeStampMixin):
    user = models.OneToOneField(User)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.user.username
