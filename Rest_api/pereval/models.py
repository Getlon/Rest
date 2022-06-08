from django.db import models


class User(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    fam = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    otc = models.CharField(max_length=100)


class PerevalAdded(models.Model):
    date_added = models.DateTimeField(blank=False, null=False)
    beauty_title = models.TextField()
    title = models.TextField()
    other_titles = models.TextField()
    connect = models.CharField(max_length=1, blank=True)
    add_time = models.DateTimeField(auto_now_add=True)
    coord = models.ForeignKey('Coords', on_delete=models.CASCADE)
    level_winter = models.TextField(max_length=3, blank=True)
    level_summer = models.TextField(max_length=3, blank=True)
    level_autumn = models.TextField(max_length=3, blank=True)
    level_spring = models.TextField(max_length=3, blank=True)


class PerevalAreas(models.Model):
    parent = models.OneToOneField(PerevalAdded, on_delete=models.CASCADE, primary_key=True)
    title = models.TextField()
    STATUS_TYPES = {
        ('new', 'new'),
        ('pending', 'pending'),
        ('accepted', 'accepted'),
        ('rejected', 'rejected'),
    }
    status = models.TextField(default='new', choices=STATUS_TYPES)


class PerevalImages(models.Model):
    data = models.BinaryField(null=False)
    title_img = models.TextField()


class SprActivitiesTypes(models.Model):
    title = models.TextField()


class Coords(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.IntegerField()


class PerevalAddedPerevalImages(models.Model):
    pereval_added = models.ForeignKey(PerevalAdded, on_delete=models.CASCADE)
    pereval_images = models.ForeignKey(PerevalImages, on_delete=models.CASCADE)


class SubmitData(models.Model):
    beauty_title = models.TextField()
    title = models.TextField()
    other_titles = models.TextField()
    connect = models.CharField(max_length=1, blank=True)
    add_time = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    fam = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    otc = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.IntegerField()
    level_winter = models.TextField(max_length=3, blank=True)
    level_summer = models.TextField(max_length=3, blank=True)
    level_autumn = models.TextField(max_length=3, blank=True)
    level_spring = models.TextField(max_length=3, blank=True)
    data = models.BinaryField(null=False)
    title_img = models.TextField()

    def __str__(self):
        return self.title
