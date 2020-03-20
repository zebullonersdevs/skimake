# users/models.py
from django.contrib.auth.models import AbstractUser, User
from django.db import models

class CustomUser(AbstractUser):
    email                  = models.EmailField(max_length=254, unique=True)

    def __str__(self):
        return self.username

class CustomUserProfile(models.Model):
    '''
    an extension of the CustomUser model
    '''
    user                    = models.OneToOneField(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    about                   = models.TextField(blank=True, null=True)
    phone_number            = models.CharField( max_length=50, blank=False, null=True, unique=True)
    ref_phone_number        = models.CharField( max_length=50, blank=True, null=False, default='123456')
    date_of_birth           = models.DateField(auto_now=False, auto_now_add=False)
    nationality             = models.CharField( max_length=50, null=True, blank=True)
    profile_pic             = models.ImageField(upload_to="profile_pic", null=True, blank=True)
    b_name                  = models.CharField( max_length=100, null=True, blank=True)
    b_address               = models.CharField( max_length=200, null=True, blank=True)
    b_branch_address        = models.CharField( max_length=200, null=True, blank=True)
    b_employe_number        = models.IntegerField( null=True, blank=True )
    b_contact_person        = models.CharField( max_length=200, null=True, blank=True)
    b_phone_number          = models.IntegerField( null=True, blank=True )
    b_email                 = models.EmailField(max_length=254, blank=True, null=True)
    b_website               = models.CharField( max_length=200, null=True, blank=True)
    b_twitter_profile       = models.CharField( max_length=200, null=True, blank=True)
    b_facebook_profile      = models.CharField( max_length=200, null=True, blank=True)
    b_annual_print_budget   = models.IntegerField()
    b_logo                  = models.ImageField(upload_to="b_logo", null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'


class CustomUserWallet(models.Model):
    '''
    model representing custom user's wallet
    '''
    user                    = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    balance                 = models.IntegerField(default=2000)

    def __str__(self):
        return f"{self.user.username}'s balance: {self.balance}"


