from django.db import models


class Musician(models.Model):
    INSTRUMENT_TYPE = (
        ("harmonium", "Harmonium"),
        ("guitar", "Guitar"),
        ("drams", "Drams"),
        ("keyboard", "Keyboard"),
    )
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    instrument_type = models.CharField(choices=INSTRUMENT_TYPE, max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
