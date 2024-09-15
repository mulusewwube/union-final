from django.db import models

class Contact_us_page(models.Model):
    name = models.CharField(null=False,max_length=50)
    email = models.EmailField(null=False, blank=False)
    Subject = models.TextField(null=False, blank=False)
    message = models.TextField(null=False, blank=False)
    # date = models.DateTimeField(auto_created=True, blank=False)
    
    def __str__(self):
        return self.name
    
class Review(models.Model):
    RATINGS = [
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    rating = models.PositiveIntegerField(choices=RATINGS)
    comments = models.TextField()

    def __str__(self):
        return f'{self.name} - {self.rating} Stars'