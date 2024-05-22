from django.core.management.base import BaseCommand, CommandError
from store.models import Product, Category

class Command(BaseCommand):
    help = 'Apaga todos os produtos e categorias'

    def handle(self, *args, **kwargs):
        # Apagar todos os produtos
        Product.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Todos os produtos foram apagados com sucesso.'))

        # Apagar todas as categorias
        Category.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Todas as categorias foram apagadas com sucesso.'))