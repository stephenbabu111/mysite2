from django.db import models

class fb_table(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.username

class gmail_table(models.Model):
    email=models.CharField(max_length=100)
    gpassword=models.CharField(max_length=100)

    def __str__(self):
        return self.email
