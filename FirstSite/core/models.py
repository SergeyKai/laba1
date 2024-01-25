from django.db import models


class Actor(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    age = models.IntegerField()

    def __str__(self):
        return f'{self.first_name} {self.last_name} id: {self.pk}'


class Film(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    img = models.ImageField(upload_to='film_img')

    actors = models.ManyToManyField(Actor)

    def __str__(self):
        return f'{self.title} id: {self.pk}'


class FilmImages(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='film_img')

    def __str__(self):
        return f'IMG {self.film.title} id: {self.pk}'
