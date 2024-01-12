from django.db import models

class NavbarItem(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(blank=True)
    order = models.IntegerField()
    image = models.ImageField(upload_to='nav_images', blank=True)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']