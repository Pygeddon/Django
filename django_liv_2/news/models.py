from django.db import models
from django.urls import reverse

# Create your models here.


#modello per classe giornalista

class Giornalista(models.Model):
    nome = models.CharField(max_length = 20)
    cognome = models.CharField(max_length = 20)

    def __str__(self):
        return self.nome + " " + self.cognome


#modello generico di articolo news
class Articolo(models.Model):
    titolo = models.CharField(max_length=100)
    contenuto = models.TextField()
    giornalista = models.ForeignKey(Giornalista, on_delete=models.CASCADE, related_name="articoli")

    def __str__(self):
        return self.titolo

    def get_absolute_url(self):
        return reverse("articolo_detail", kwargs={"pk": self.pk})
