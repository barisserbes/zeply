from django.db import models
from django.contrib.auth.models import User
from django_cryptography.fields import encrypt
from django.conf import settings


class BaseModel(models.Model):
    #I think it is better to keep user data in case some regulations might occur in the future by governments.
    id = models.AutoField(primary_key=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class PrivateKey(BaseModel):
    key = encrypt(models.CharField(max_length=64))


class BTCAddress(BaseModel):
    private_key = models.ForeignKey(PrivateKey, on_delete=models.DO_NOTHING)
    address = encrypt(models.CharField(max_length=64))


class ETHAddress(BaseModel):
    private_key = models.ForeignKey(PrivateKey, on_delete=models.DO_NOTHING)
    address = encrypt(models.CharField(max_length=64))