from django.db import models

PHONE_CHOICE = (
    (0, 'brak informacji'),
    (1, 'komórkowy'),
    (2, 'domowy'),
    (3, 'służbowy'),
    (4, 'inny')
)

EMAIL_CHOICE = (
    (0, 'brak informacji'),
    (1, 'prywatny'),
    (2, 'służbowy'),
    (3, 'inny')
)


class Person(models.Model):
    name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    description = models.CharField(max_length=128, null=True)
    #image = models.ImageField(upload_to="home/witek/Desktop/Warsztaty4/Warsztaty4/Warsztaty4/mail_box/Photos/", blank=True)
    adres = models.ForeignKey("Address", on_delete=models.PROTECT, null=True)


class Address(models.Model):
    city = models.CharField(max_length=64)
    street = models.CharField(max_length=64, null=True)
    house_no = models.CharField(max_length=64, null=True)
    flat_no = models.CharField(max_length=64, null=True)


class Phone(models.Model):
    ph_number = models.CharField(max_length=32)
    ph_type = models.IntegerField(choices=PHONE_CHOICE, default=0)
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)


class Email(models.Model):
    email_address = models.CharField(max_length=64)
    email_type = models.IntegerField(choices=EMAIL_CHOICE, default=0)
    e_owner = models.ForeignKey(Person, on_delete=models.CASCADE)


class Group(models.Model):
    name = models.CharField(max_length=64)
    persons = models.ManyToManyField(Person)