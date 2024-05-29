import os
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Apaga arquivos de mídia duplicados durante os testes'

    def handle(self, *args, **kwargs):
        media_path = 'media/uploads/product'
        allowed_images = {'Lenovo.jpg', 'macbook.png', 'Samsung_s23.jpg', 'Iphone.jpg', 'Tablet.jpg', 'Ipad.png', 'Smartwatch.jpg', 'Blackshark.jpg', 'notebook_positivo.jpg', 'notebook_gamer_acer.jpg', 's21_fe.jpg', 'ipad_air_5.jpg', 'airpods.jpg', 'apple_watch.jpg', 'samsung_pods.jpg'}

        if not os.path.exists(media_path):
            self.stdout.write(self.style.ERROR(f'Diretório {media_path} não existe'))
            return

        for filename in os.listdir(media_path):
            filepath = os.path.join(media_path, filename)
            if os.path.isfile(filepath) and filename not in allowed_images:
                os.remove(filepath)
                self.stdout.write(self.style.SUCCESS(f'Removendo imagem: {filepath}'))

        self.stdout.write(self.style.SUCCESS('Imagens removidas com sucesso.'))