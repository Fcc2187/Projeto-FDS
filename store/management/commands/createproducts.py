import os
from django.core.management.base import BaseCommand, CommandError
from store.models import Product, Category
from django.core.files import File

class Command(BaseCommand):
    help = 'Adiciona produtos padrão ao modelo Product'

    def handle(self, *args, **kwargs):
        # Detalhes dos produtos padrão
        products = [
            {
                'name': 'Notebook Lenovo',
                'price': 2500.00,
                'category_name': 'Notebooks',
                'description': 'Notebook Lenovo IdeaPad 1i Intel Core i5 - 8GB RAM SSD 512GB Windows 11 15,6” 15IAU7',
                'image_path': "media/uploads/product/Lenovo.jpg",
                'is_sale': False,
                'sale_price': 0.0
            },
            {
                'name': 'Macbook',
                'price': 2800.00,
                'category_name': 'Notebooks',
                'description': 'Apple Macbook Air (13 Polegadas, 2020, Chip M1, 256 Gb De Ssd, 8Gb De Ram) - Cinza-espacial',
                'image_path': "media/uploads/product/macbook.png",
                'is_sale': False,
                'sale_price': 0.0
            },
            {
                'name': 'Samsung Galaxy S23',
                'price': 3400.00,
                'category_name': 'Celulares',
                'description': 'Smartphone Samsung Galaxy S23 256GB Preto 5G 8GB RAM 6,1” Câm Tripla + Selfie 12MP',
                'image_path': "media/uploads/product/Samsung_s23.jpg",
                'is_sale': False,
                'sale_price': 0.0
            },
            {
                'name': 'iPhone 13',
                'price': 3200.00,
                'category_name': 'Celulares',
                'description': 'Apple iPhone 13 128GB Meia-Noite 5G Tela 6,1" Câm. Traseira 12+12MP Frontal 12MP',
                'image_path': "media/uploads/product/Iphone.jpg",
                'is_sale': False,
                'sale_price': 0.0
            },
            {
                'name': 'Tablet Samsung',
                'price': 2600.00,
                'category_name': 'Tablets',
                'description': 'Tablet Samsung Galaxy Tab S6 Lite com Caneta 10,4" 64GB 4GB RAM Android 14 Exynos 1280 Octa-Core Wi-Fi 4G',
                'image_path': "C:/Users/brazg/Downloads/fotos projeto/Tablet.jpg",
                'is_sale': False,
                'sale_price': 0.0
            },
            {
                'name': 'iPad',
                'price': 2900.00,
                'category_name': 'Tablets',
                'description': 'Tablet Apple iPad 10ª Geração 64GB Wi-Fi 10,9" iPadOS 12MP Silver (Prateado)',
                'image_path': "C:/Users/brazg/Downloads/fotos projeto/Ipad.png",
                'is_sale': False,
                'sale_price': 0.0
            },
            {
                'name': 'Smartwatch',
                'price': 250.00,
                'category_name': 'Smartwatchs',
                'description': 'Xiaomi-Redmi Watch 3 Active display LCD, frequência cardíaca, sangue, oxigênio, freqüência cardíaca, Bluetooth, chamada de voz, mais de 100 modos esportivos, 1,83 polegadas',
                'image_path': "C:/Users/brazg/Downloads/fotos projeto/Smartwatch.jpg",
                'is_sale': False,
                'sale_price': 0.0
            },
            {
                'name': 'Headset Gamer',
                'price': 360.00,
                'category_name': 'Fones de ouvido',
                'description': 'Fone De Ouvido Headset Gamer Razer Blackshark V2 X7.1 Pc Ps4 Cor Branco',
                'image_path': "C:/Users/brazg/Downloads/fotos projeto/Blackshark.jpg",
                'is_sale': False,
                'sale_price': 0.0
            },
            {
                'name': 'Notebook Positivo',
                'price': 1600.00,
                'category_name': 'Notebooks',
                'description': 'Notebook Positivo Motion C4128g-14 Intel® Celeron® Dual-Core™ 128GB 4GB Windows 11 Home 14" - Cinza',
                'image_path': "C:/Users/brazg/Downloads/fotos projeto/notebook positivo.jpg",
                'is_sale': False,
                'sale_price': 0.0
            },
            {
                'name': 'Notebook Gamer',
                'price': 4800.00,
                'category_name': 'Notebooks',
                'description': 'Notebook Acer Nitro 5 AN515-58-54UH Ci5 12ª Gen Windows 11 Home 8GB 512GB RTX 3050 15.6” Full HD',
                'image_path': "C:/Users/brazg/Downloads/fotos projeto/notebook gamer acer.jpg",
                'is_sale': False,
                'sale_price': 0.0
            },
            {
                'name': 'Samsung Galaxy S21 FE',
                'price': 2500.00,
                'category_name': 'Celulares',
                'description': 'Smartphone Samsung Galaxy S21 FE 5G Verde 256GB, 8GB RAM, Tela Infinita de 6.4”, Câmera Traseira Tripla, Android 11 e Processador Octa-Core',
                'image_path': "C:/Users/brazg/Downloads/fotos projeto/s21 fe.jpg",
                'is_sale': False,
                'sale_price': 0.0
            },
            {
                'name': 'iPad Air 5',
                'price': 6000.00,
                'category_name': 'Tablets',
                'description': 'iPad Air da Apple (5a geração): Com chip M1, tela Liquid Retina de 10,9 polegadas, 64 GB Wi-Fi 6, câmera frontal de 12 MP, câmera traseira de 12 MP, Touch ID, Azul',
                'image_path': "C:/Users/brazg/Downloads/fotos projeto/ipad air 5.jpg",
                'is_sale': False,
                'sale_price': 0.0
            },
            {
                'name': 'Air Pods',
                'price': 1200.00,
                'category_name': 'Fones de ouvido',
                'description': 'Apple AirPods (3ª geração) com estojo de recarga Lightning',
                'image_path': "C:/Users/brazg/Downloads/fotos projeto/airpods.jpg",
                'is_sale': False,
                'sale_price': 0.0
            },
            {
                'name': 'Apple Watch',
                'price': 1500.00,
                'category_name': 'Smartwatchs',
                'description': 'Apple Watch Se 2 Geração 40mm Preto',
                'image_path': "C:/Users/brazg/Downloads/fotos projeto/apple watch.jpg",
                'is_sale': False,
                'sale_price': 0.0
            },
            {
                'name': 'Samsung Buds',
                'price': 800.00,
                'category_name': 'Fones de ouvido',
                'description': 'Samsung Galaxy Buds vivo, Wireless Earbuds w / ativo de cancelamento de ruído (Mística Black)',
                'image_path': "C:/Users/brazg/Downloads/fotos projeto/samsung pods.jpg",
                'is_sale': False,
                'sale_price': 0.0
            },
        ]

        for product_data in products:
            name = product_data['name']
            price = product_data['price']
            category_name = product_data['category_name']
            description = product_data['description']
            image_path = product_data['image_path']
            is_sale = product_data['is_sale']
            sale_price = product_data['sale_price']

            # Verificar se o caminho da imagem existe
            if not os.path.exists(image_path):
                self.stdout.write(self.style.ERROR(f'Imagem não encontrada no caminho: {image_path}'))
                continue

            # Criar ou obter a categoria
            category, created = Category.objects.get_or_create(name=category_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Categoria "{category_name}" criada.'))

            # Abrir a imagem e criar o produto
            with open(image_path, 'rb') as image_file:
                product = Product(
                    name=name,
                    price=price,
                    category=category,
                    description=description,
                    is_sale=is_sale,
                    sale_price=sale_price
                )
                product.image.save(os.path.basename(image_path), File(image_file), save=True)

            self.stdout.write(self.style.SUCCESS(f'Produto "{name}" criado com sucesso.'))