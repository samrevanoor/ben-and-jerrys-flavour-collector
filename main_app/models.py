from django.db import models
from django.urls import reverse

TOPPINGS = (
    ('N', 'no toppings!'),
    ('CSp', 'coloured sprinkles'),
    ('ChSp', 'chocolate sprinkles'),
    ('Ch', 'cherries'),
    ('Nu', 'nuts'),
    ('Ca', 'caramel')
)

class Vendor(models.Model):
  name = models.CharField(max_length=100)
  address = models.CharField(max_length=100)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('vendors_detail', kwargs={'pk': self.id})

class Flavour(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    rating = models.IntegerField()
    vendors = models.ManyToManyField(Vendor)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'flavour_id': self.id})

class RecommendedTopping(models.Model):
    topping = models.CharField(
        max_length=4,
        choices=TOPPINGS,
        default=TOPPINGS[0][0]
    )
    quantity = models.CharField('Recommended quantity', max_length=30)
    flavour = models.ForeignKey(Flavour, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_topping_display()}: {self.quantity}"
    
    class Meta:
        ordering = ['-id']