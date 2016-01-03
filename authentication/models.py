from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from django.contrib.auth.models import BaseUserManager


class AccountManager(BaseUserManager):
    def create_user(self, employeeid, email, firstname, lastname, password=None, **kwargs):
        if not employeeid:
            raise ValueError('Users must have a valid Employee ID.')

        if not kwargs.get('username'):
            raise ValueError('Users must have a valid Username')

        if not email:
            raise ValueError('Users must have a valid email address.')

        if not firstname:
            raise ValueError('First Name is required.')

        if not lastname:
            raise ValueError('Last Name is required.')

        account = self.model(
            email=self.normalize_email(email), 
            username=kwargs.get('username'),
            employeeid=employeeid,
            firstname=firstname,
            lastname=lastname
        )

        account.set_password(password)
        account.save()

        return account

    def create_superuser(self, employeeid, email, firstname, lastname, password, **kwargs):
        account = self.create_user(employeeid, email, firstname, lastname, password, **kwargs)

        account.is_admin = True
        account.save()

        return account

class Account(AbstractBaseUser):
    employeeid = models.CharField(unique=True,max_length=50)
    username = models.CharField(max_length=50, unique=True)

    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

    is_admin = models.BooleanField(default=False)

    datecreated = models.DateTimeField(auto_now_add=True)

    objects = AccountManager()

    USERNAME_FIELD = 'employeeid'
    REQUIRED_FIELDS = ['username','email','firstname','lastname']

    def __unicode__(self):
        return self.employeeid

    def get_full_name(self):
        return ' '.join([self.firstname, self.lastname])

    def get_short_name(self):
        return self.firstname