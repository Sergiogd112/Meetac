from django.db import models
from django.contrib.auth.models import User

class MeetacUser(User):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tags=models.JSONField(blank=True)
    policy= models.BooleanField(default=False)
    birthday= models.DateField()
    description=models.TextField(max_length=256)
    profileimg= models.ImageField()

