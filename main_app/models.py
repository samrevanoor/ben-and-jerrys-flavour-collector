from django.db import models
from django.urls import reverse

TOPPINGS = (
    ('N', 'None')
    ('CSp', 'coloured sprinkles'),
    ('ChSp', 'chocolate sprinkles'),
    ('Ch', 'cherries'),
    ('Nu', 'nuts'),
    ('Ca', 'caramel')
)

class Flavour(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    rating = models.IntegerField()

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
        # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.quantity} of {self.get_topping_display()}"