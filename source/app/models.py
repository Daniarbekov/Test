from django.db import models
from django.urls import reverse


class MenuItems(models.Model):
    name = models.CharField(unique=True ,max_length=50)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True, unique=True)
    named_url = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_children(self):
        return self.menuitems_set.all()
    
    def get_url(self):
        if self.named_url:
            try:
                url = reverse(self.named_url)
            except:
                if self.url:
                    url = self.url
        return "/" + url
