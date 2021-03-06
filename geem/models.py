from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField

# Create your models here.
class Package(models.Model):
    owner = models.ForeignKey(
        User,
        related_name='packages',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    contents = JSONField()

    def __str__(self):
        owner = self.owner
        if (owner):
            return "id:" + str(self.id) + " owner:" + self.owner.username + " created:" + str(self.created)
        else:
            return "id:" + str(self.id) + " owner:" + "public" + " created:" + str(self.created)
    
