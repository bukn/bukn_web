from django.db import models
from django.contrib.auth.models import User

from get_ndays import get_ndays

class UserProfile(models.Model):
    user = models.ForeignKey(User)
    birthday = models.DateTimeField('birthday')

    def __unicode__(self):
        return self.birthday.ctime()
    def ndays(self):
        return get_ndays(self.birthday)
