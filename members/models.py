from django.db import models

# Create your models here.


class Member(models.Model):
    class Meta:
        verbose_name_plural = 'Members'
    full_name = models.CharField(max_length=254)
    email = models.CharField(max_length=254)
    created = models.DateTimeField()
    bio = models.CharField(max_length=254)
    admin_id = models.IntegerField()

    def __str__(self):
        return self.full_name


class Subs(models.Model):
    year = models.IntegerField(blank=False)
    member_id = models.IntegerField(blank=False)
    rate = models.DecimalField(max_digits=5, decimal_places=2)
    order_id = models.IntegerField()

    def __int__(self):
        return self.year, self.member_id
