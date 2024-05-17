from django.db import models
from .utils import get_reality_price

# Create your models here.

class Ceny(models.Model):
    name = models.CharField(max_length=220, blank=True)
    url = models.URLField(null=True, blank=True)
    now_price = models.IntegerField(blank=True)
    old_price = models.IntegerField(default=0)
    differ_price = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.name)
    
    class Meta:
        ordering = ('differ_price', '-created')
        
    def save(self, *args, **kwargs):
        name, price = get_reality_price(self.url)
        old_price = self.now_price
        if self.now_price:
            if price != old_price:
                diff = price - old_price
                self.differ_price = diff
                self.old_price = old_price
        else:
            self.old_price = 0
            self.differ_price = 0
            
        self.name = name
        self.now_price = price
                
        super().save(*args, **kwargs)
        
    
    
    