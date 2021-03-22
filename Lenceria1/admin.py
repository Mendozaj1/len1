from django.contrib import admin
from .models import Articulo, Jugetes, Lenceria_Mujeres, Lenceria_Hombres, Lubricante_cosmeticos, Despedida_soltera

# Register your models here.

admin.site.register(Articulo)
admin.site.register(Jugetes)
admin.site.register(Lenceria_Mujeres)
admin.site.register(Lenceria_Hombres)
admin.site.register(Lubricante_cosmeticos)
admin.site.register(Despedida_soltera)