from django.db import models
from django.contrib.auth.models import User
from PIL import Image

ROLE = (
    (False, "Mentee"),
    (True, "Mentor"),
)

BATCH = (
    ("2011", "2011"),
    ("2012", "2012"),
    ("2013", "2013"),
    ("2014", "2014"),
    ("2015", "2015"),
    ("2016", "2016"),
    ("2017", "2017"),
    ("2018", "2018"),
    ("2019", "2019"),
    ("2020", "2020"),
    ("2021", "2021")
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    role = models.CharField(max_length=10, choices=ROLE, default=False)
    batch = models.CharField(max_length=10, choices=BATCH, default="2019")
    name = models.CharField(max_length=100, default=None, blank=True, null=True)
    points = models.PositiveIntegerField(default=0)
    phone = models.PositiveBigIntegerField(default=None, blank=True, null=True)
    college = models.CharField(max_length=300, default=None, blank=True, null=True)
    profession = models.CharField(max_length=100, default=None, blank=True, null=True)
    address = models.TextField(default=None, blank=True, null=True)
    guidance = models.TextField(default=None, blank=True, null=True)
    linkedin = models.URLField(default=None, blank=True, null=True)
    instagram = models.URLField(default=None, blank=True, null=True)
    twitter = models.URLField(default=None, blank=True, null=True)
    github = models.URLField(default=None, blank=True, null=True)
    okr = models.URLField(default=None, blank=True, null=True)
    facebook = models.URLField(default=None, blank=True, null=True)

    def __str__(self):
        return f'{self.user} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
