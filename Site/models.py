from django.db import models

# Create your models here.


class Class(models.Model):
    group = models.CharField(max_length=20, null=True, blank=True)
    day = models.CharField(max_length=25, null=True, blank=True)
    time = models.CharField(max_length=12, null=True, blank=True)
    def __str__(self):
        return(f"{self.group} {self.day} {self.time}")


class Artist(models.Model):
    firstname = models.CharField(max_length=20, null=True, blank=True)
    lastname = models.CharField(max_length=20, null=True, blank=True)
    phone = models.CharField(max_length=12, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    prefix = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return(f"{self.firstname} {self.lastname}")


class Teacher(models.Model):
    artist = models.ForeignKey(Artist, null=True, on_delete=models.CASCADE, related_name="teacher_artist")
    photo = models.CharField(max_length=200, null=True, blank=True)
    photo_size = models.CharField(max_length=100, null=True, blank=True)
    quote = models.TextField(null=True, blank=True)
    started = models.CharField(max_length=4, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    classes = models.ManyToManyField(Class, blank=True, related_name="teacher_class")

    def __str__(self):
        return(f"{self.artist}")
    
    def get_teacher_classes(self):
        return [tc for tc in self.classes.all()]


class Artwork(models.Model):
    artist = models.ForeignKey(Artist, null=True, on_delete=models.CASCADE, related_name="artwork_artist")
    image = models.CharField(max_length=200, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    medium = models.CharField(max_length=200, null=True, blank=True)
    size = models.CharField(max_length=30, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return(f"{self.artist} {self.image}")
    
    def serialize(self):
        return {
            'artist' : f'{self.artist.firstname} {self.artist.lastname}',
            'image' : self.image,
            'title' : self.title,
            'medium' : self.medium,
            'size' : self.size,
            'price' : self.price,
            'status' : self.status
        }




class MailList(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    events = models.BooleanField(null=True, blank=True)
    newsletter = models.BooleanField(null=True, blank=True)
