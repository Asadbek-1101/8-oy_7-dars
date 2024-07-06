from django.db import models

class Header(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='images/')
    phrone_number = models.IntegerField()
    link = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class BigHeader(models.Model):
    image = models.ImageField(upload_to='images/', height_field="981x413")
    text = models.CharField(max_length=400)

    def __str__(self):
        return self.text

class Services(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Oportunities(models.Model):
    services = models.ForeignKey(Services, on_delete=models.CASCADE)
    aviakompaniya = models.CharField(max_length=200)
    date = models.IntegerField()
    viza = models.CharField(max_length=100)
    ambulation = models.IntegerField()
    occupation = models.CharField(max_length=200)
    whater = models.CharField(max_length=100)
    items = models.CharField(max_length=200)

    def __str__(self):
        return self.services


class About(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name


class SocialMedia(models.Model):
    name = models.CharField(max_length=50)
    text = models.TextField()
    link = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Comments(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=200)
    data = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    def __str__(self):
        return self.name















