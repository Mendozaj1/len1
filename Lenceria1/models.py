from django.db import models

# Create your models here.

class Articulo(models.Model):
    Titulo = models.CharField(max_length=100)
    Numero = models.CharField(default = 'null', max_length=10)
    Contenido = models.TextField()
    Estado = models.BooleanField()
    imagen = models.ImageField(default = 'null', upload_to="Article")

    class Meta:
        verbose_name = "Categoria"
    
    
    def __str__(self):
        return f"{self.Titulo} ------------------------------ {self.Estado}"

class Jugetes(models.Model):
    Titulo = models.CharField(max_length=100)
    Numero = models.CharField(default = 'null', max_length=10)
    Contenido = models.TextField()
    Estado = models.BooleanField()
    imagen = models.ImageField(default = 'null', upload_to="Article")

    class Meta:
        verbose_name = "Jugete"
    
    
    def __str__(self):
        return f"{self.Titulo} ------------------------------ {self.Estado}"

class Lenceria_Mujeres(models.Model):
    Titulo = models.CharField(max_length=100)
    Numero = models.CharField(default = 'null', max_length=10)
    Contenido = models.TextField()
    Estado = models.BooleanField()
    imagen = models.ImageField(default = 'null', upload_to="Article")

    class Meta:
        verbose_name = "Lenceria_Mujere"
    
    
    def __str__(self):
        return f"{self.Titulo} ------------------------------ {self.Estado}"

class Lenceria_Hombres(models.Model):
    Titulo = models.CharField(max_length=100)
    Numero = models.CharField(default = 'null', max_length=10)
    Contenido = models.TextField()
    Estado = models.BooleanField()
    imagen = models.ImageField(default = 'null', upload_to="Article")

    class Meta:
        verbose_name = "Lenceria_Hombre"
    
    
    def __str__(self):
        return f"{self.Titulo} ------------------------------ {self.Estado}"

class Lubricante_cosmeticos(models.Model):
    Titulo = models.CharField(max_length=100)
    Numero = models.CharField(default = 'null', max_length=10)
    Contenido = models.TextField()
    Estado = models.BooleanField()
    imagen = models.ImageField(default = 'null', upload_to="Article")

    class Meta:
        verbose_name = "Lubricante_cosmetico"
    
    
    def __str__(self):
        return f"{self.Titulo} ------------------------------ {self.Estado}"

class Despedida_soltera(models.Model):
    Titulo = models.CharField(max_length=100)
    Numero = models.CharField(default = 'null', max_length=10)
    Contenido = models.TextField()
    Estado = models.BooleanField()
    imagen = models.ImageField(default = 'null', upload_to="Article")

    class Meta:
        verbose_name = "Despedida_soltera"
    
    
    def __str__(self):
        return f"{self.Titulo} ------------------------------ {self.Estado}"