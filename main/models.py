from django.db import models

# Create your models here.
class Loggin(models.Model):
    username = models.CharField(max_lenght = 255)
    body = models.CharField(max_lenght = 255)
    email = models.EmailField()
    phone = models.CharField(max_lenght = 14)
    password = models.CharField(max_lenght = 50)
    name = models.CharField(max_lenght = 255)
    surname = models.CharField(max_lenght = 255)

class Body(models.Model):
    title = models.CharField(max_lenght = 255)
    body = models.TextField()
    icon = models.ImageField()

class Education(models.Model):
    name = models.CharField(max_lenght = 255)
    body = models.TextField()
    title = models.CharField()
    icon = models.ImageField()


class Addres(models.Model):
    addres = models.CharField(max_lenght = 255)
    title = models.CharField(max_lenght = 255)
    icon = models.ImageField()


class Choose1(models.Model):
    title = models.CharField(max_lenght = 255)
    body = models.TextField()
    icon = models.ImageField()


class Servise(models.Model):
    title = models.CharField(max_lenght = 255)
    body = models.TextField()
    icon = models.ImageField()


class Choose2(models.Model):
    title = models.CharField(max_lenght = 255)
    body = models.TextField()
    icon = models.ImageField()

class Form(models.Model):
    name = models.CharField(max_lenght = 255)
    email = models.EmailField()
    phone = models.CharField(max_lenght = 14)
    body = models.TextField()

    def __str__(self):
        return f"Murojat {self.name}dan"
    

    class Meta:
        verbose_name = "Murojatlar ro`yxati"
        verbose_name_plural = ""
        ordering = ("")
