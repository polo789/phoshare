from django.db import models
from django.utils import timezone
class Category(models.Model):
    name=models.CharField(max_length=30)
    class Meta:
        verbose_name_plural='categories'
    def __str__(self):
        return self.name

class Location(models.Model):
    name=models.CharField(max_length=30)
    def __str__(self):
        return  self.name
    
    @classmethod
    def get_locations(cls):
        locations=Location.objects.all()
        return locations
    @classmethod
    def update_location(cls, id, value):
        cls.objects.filter(id=id).update(image=value)

class Image(models.Model):
    image=models.ImageField(upload_to='images/')
    location=models.ForeignKey(Location, on_delete=models.CASCADE)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    description=models.TextField()
    date=models.DateTimeField()
    author=models.CharField(max_length=20, default='admin')

    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if self.date is None:
            self.date=timezone.now()
        return super(Image, self).save(*args, **kwargs)
    class Meta:
        ordering=['date']
    @classmethod
    def get_image_by_id(cls, id):
        image=cls.objects.filter(id=id).all()
        return image
    @classmethod
    def update_image(cls, id, value):
        cls.objects.filter(id=id).update(image=value)
    @classmethod
    def search_by_category(cls, category):
        images=cls.objects.filter(category__name__icontains=category)
        return images
    @classmethod
    def filter_by_location(cls, location):
        image_location=Image.objects.filter(location__name=location).all()
        return image_location
    


