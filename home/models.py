# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Organizationtype(models.Model):

    #__Organizationtype_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)

    #__Organizationtype_FIELDS__END

    class Meta:
        verbose_name        = _("Organizationtype")
        verbose_name_plural = _("Organizationtype")


class Organization(models.Model):

    #__Organization_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    organization_type = models.ForeignKey(OrganizationType, on_delete=models.CASCADE)

    #__Organization_FIELDS__END

    class Meta:
        verbose_name        = _("Organization")
        verbose_name_plural = _("Organization")


class Autonomoussystem(models.Model):

    #__Autonomoussystem_FIELDS__
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    announced = models.BooleanField()

    #__Autonomoussystem_FIELDS__END

    class Meta:
        verbose_name        = _("Autonomoussystem")
        verbose_name_plural = _("Autonomoussystem")


class Prefix(models.Model):

    #__Prefix_FIELDS__
    prefix = models.CharField(max_length=255, null=True, blank=True)
    asn = models.ForeignKey(AutonomousSystem, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    announced = models.BooleanField()

    #__Prefix_FIELDS__END

    class Meta:
        verbose_name        = _("Prefix")
        verbose_name_plural = _("Prefix")



#__MODELS__END
