from django.test import LiveServerTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium import webdriver
from django.core.management import call_command
import time, subprocess

class AtualizarPerfil(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-browser-side-navigation")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1440,1080")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-extensions")
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def setUp(self):
        subprocess.run(['python', 'manage.py', 'createproducts'], check=True)

    def tearDown(self):
        subprocess.run(['python', 'manage.py', 'deleteproducts'], check=True)
        subprocess.run(['python', 'manage.py', 'deletedoubles'], check=True)
        subprocess.run(['python', 'manage.py', 'deleteusers'], check=True)

    def test_cenario1(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/register/")
        usuario = driver.find_element(by=By.NAME, value="username")
        nome = driver.find_element(by=By.NAME, value="first_name")
        sobrenome = driver.find_element(by=By.NAME, value="last_name")
        email = driver.find_element(by=By.NAME, value="email")
        senha = driver.find_element(by=By.NAME, value="password1")
        confirmar_senha = driver.find_element(by=By.NAME, value="password2")
        botao = driver.find_element(by=By.NAME, value="registro")

        usuario.send_keys(f"User_1")
        nome.send_keys(f"José")
        sobrenome.send_keys(f"Braz")
        email.send_keys(f"jbon@cesar.school")
        senha.send_keys("Senha1234")
        confirmar_senha.send_keys("Senha1234")
        botao.send_keys(Keys.ENTER)
        time.sleep(2)

        driver.get("http://127.0.0.1:8000/update_info/")
        numero = driver.find_element(by=By.NAME, value="Numero")
        endereco1 = driver.find_element(by=By.NAME, value="Endereço1")
        endereco2 = driver.find_element(by=By.NAME, value="Endereço2")
        cidade = driver.find_element(by=By.NAME, value="Cidade")
        estado = driver.find_element(by=By.NAME, value="Estado")
        cep = driver.find_element(by=By.NAME, value="CEP")
        pais = driver.find_element(by=By.NAME, value="País")
        botao2 = driver.find_element(by=By.NAME, value="atualizar")

        numero.send_keys("8199999999")
        endereco1.send_keys(f"Rua Le Parc, 100")
        endereco2.send_keys(f"Rua Cais do Apolo, 77")
        cidade.send_keys(f"Recife")
        estado.send_keys(f"Pernambuco")
        cep.send_keys("123456789")
        pais.send_keys(f"Brasil")
        botao2.send_keys(Keys.ENTER)
        time.sleep(2)

        driver.get("http://127.0.0.1:8000/update_info/")
        numero = driver.find_element(by=By.NAME, value="Numero")
        value_numero = numero.get_attribute("value")
        self.assertEqual(value_numero, "8199999999")
        driver.get("http://127.0.0.1:8000/logout/")

    def test_cenario2(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/register/")
        usuario = driver.find_element(by=By.NAME, value="username")
        nome = driver.find_element(by=By.NAME, value="first_name")
        sobrenome = driver.find_element(by=By.NAME, value="last_name")
        email = driver.find_element(by=By.NAME, value="email")
        senha = driver.find_element(by=By.NAME, value="password1")
        confirmar_senha = driver.find_element(by=By.NAME, value="password2")
        botao = driver.find_element(by=By.NAME, value="registro")

        usuario.send_keys(f"User_1")
        nome.send_keys(f"José")
        sobrenome.send_keys(f"Braz")
        email.send_keys(f"jbon@cesar.school")
        senha.send_keys("Senha1234")
        confirmar_senha.send_keys("Senha1234")
        botao.send_keys(Keys.ENTER)
        time.sleep(2)

        driver.get("http://127.0.0.1:8000/update_info/")
        numero = driver.find_element(by=By.NAME, value="Numero")
        endereco1 = driver.find_element(by=By.NAME, value="Endereço1")
        endereco2 = driver.find_element(by=By.NAME, value="Endereço2")
        cidade = driver.find_element(by=By.NAME, value="Cidade")
        estado = driver.find_element(by=By.NAME, value="Estado")
        cep = driver.find_element(by=By.NAME, value="CEP")
        pais = driver.find_element(by=By.NAME, value="País")
        botao2 = driver.find_element(by=By.NAME, value="atualizar")

        numero.send_keys("8199999999")
        endereco1.send_keys(f"Rua Le Parc, 100")
        endereco2.send_keys(f"Rua Cais do Apolo, 77")
        cidade.send_keys(f"Recife")
        estado.send_keys(f"Pernambuco")
        cep.send_keys("123456789")
        pais.send_keys(f"Brasil")
        botao2.send_keys(Keys.ENTER)
        time.sleep(2)

        driver.get("http://127.0.0.1:8000/update_info/")
        numero = driver.find_element(by=By.NAME, value="Numero")
        value_numero = numero.get_attribute("value")
        self.assertEqual(value_numero, "8199999999")
        driver.get("http://127.0.0.1:8000/logout/")
        time.sleep(2)

        driver.get("http://127.0.0.1:8000/login/")
        usuario = driver.find_element(by=By.NAME, value="username")
        senha = driver.find_element(by=By.NAME, value="password")
        botao = driver.find_element(by=By.NAME, value="login")

        usuario.send_keys("User_1")
        senha.send_keys("Senha1234")
        botao.send_keys(Keys.ENTER)
        time.sleep(2)

        driver.get("http://127.0.0.1:8000/update_info/")
        numero = driver.find_element(by=By.NAME, value="Numero")
        endereco1 = driver.find_element(by=By.NAME, value="Endereço1")
        endereco2 = driver.find_element(by=By.NAME, value="Endereço2")
        cep = driver.find_element(by=By.NAME, value="CEP")
        botao2 = driver.find_element(by=By.NAME, value="atualizar")

        for i in range(10):
            numero.send_keys(Keys.BACK_SPACE)
        numero.send_keys("8199099190")
        for j in range(17):
            endereco1.send_keys(Keys.BACKSPACE)
        endereco1.send_keys(f"Rua Cais do Apolo, 77")
        for k in range(21):
            endereco2.send_keys(Keys.BACKSPACE)
        endereco2.send_keys(f"Rua Le Parc, 100")
        for l in range(9):
            cep.send_keys(Keys.BACKSPACE)
        cep.send_keys("987654321")
        time.sleep(1)
        botao2.send_keys(Keys.ENTER)
        time.sleep(2)

        driver.get("http://127.0.0.1:8000/update_info/")
        numero = driver.find_element(by=By.NAME, value="Numero")
        value_numero = numero.get_attribute("value")
        self.assertEqual(value_numero, "8199099190")
        driver.get("http://127.0.0.1:8000/logout/")

class PesquisarProduto(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-browser-side-navigation")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1440,1080")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-extensions")
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def setUp(self):
        subprocess.run(['python', 'manage.py', 'createproducts'], check=True)

    def tearDown(self):
        subprocess.run(['python', 'manage.py', 'deleteproducts'], check=True)
        subprocess.run(['python', 'manage.py', 'deletedoubles'], check=True)

    def test_cenario1(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/search/")
        pesquisa = driver.find_element(by=By.NAME, value="searched")
        botao = driver.find_element(by=By.NAME, value="go")

        pesquisa.send_keys("iPhone")
        time.sleep(2)
        botao.send_keys(Keys.ENTER)
        self.assertEqual(driver.find_element(by=By.XPATH, value="/html/body/div/div/center/div/div[2]/div/div/div[1]/div/h5").text,"iPhone 13")

    def test_cenario2(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/search/")
        pesquisa = driver.find_element(by=By.NAME, value="searched")
        botao = driver.find_element(by=By.NAME, value="go")

        pesquisa.send_keys("8gb")
        time.sleep(2)
        botao.send_keys(Keys.ENTER)
        self.assertEqual(driver.find_element(by=By.XPATH, value="/html/body/div/div/center/div/div[2]/div[4]/div/div[1]/div/h5").text,"iPhone 13")

    def test_cenario3(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/search/")
        pesquisa = driver.find_element(by=By.NAME, value="searched")
        botao = driver.find_element(by=By.NAME, value="go")

        pesquisa.send_keys("Fechadura eletrônica")
        time.sleep(2)
        botao.send_keys(Keys.ENTER)
        self.assertEqual(driver.find_element(by=By.XPATH, value="/html/body/div[1]").text,"Não achamos nenhum produto, tente denovo")

class AdicionarNoCarrinho(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-browser-side-navigation")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1440,1080")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-extensions")
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def setUp(self):
        subprocess.run(['python', 'manage.py', 'createproducts'], check=True)

    def tearDown(self):
        subprocess.run(['python', 'manage.py', 'deleteproducts'], check=True)
        subprocess.run(['python', 'manage.py', 'deletedoubles'], check=True)
        subprocess.run(['python', 'manage.py', 'deleteusers'], check=True)

    def test_cenario1_and_2(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        time.sleep(2)
        botao = driver.find_element(by=By.XPATH, value="/html/body/section/div/div/div[3]/div/div[2]/div/a")
        botao.send_keys(Keys.ENTER)
        time.sleep(3)
        botao2 = driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div/div[2]/div/center/a[2]")
        botao2.send_keys(Keys.ENTER)
        
        usuario = driver.find_element(by=By.NAME, value="username")
        nome = driver.find_element(by=By.NAME, value="first_name")
        sobrenome = driver.find_element(by=By.NAME, value="last_name")
        email = driver.find_element(by=By.NAME, value="email")
        senha = driver.find_element(by=By.NAME, value="password1")
        confirmar_senha = driver.find_element(by=By.NAME, value="password2")
        botao = driver.find_element(by=By.NAME, value="registro")

        usuario.send_keys(f"User_3")
        nome.send_keys(f"Rodrigo")
        sobrenome.send_keys(f"Torre")
        email.send_keys(f"rtmr@cesar.school")
        senha.send_keys("Senha1234")
        confirmar_senha.send_keys("Senha1234")
        botao.send_keys(Keys.ENTER)
        time.sleep(2)

        driver.get("http://127.0.0.1:8000/")
        botao2 = driver.find_element(by=By.XPATH, value="/html/body/section/div/div/div[5]/div/div[2]/div/a")
        botao2.send_keys(Keys.ENTER)
        time.sleep(2)
        botaoadd = driver.find_element(by=By.ID, value="add-cart")
        botaoadd.send_keys(Keys.ENTER)
        time.sleep(2)
        botaocart = driver.find_element(by=By.NAME, value="carrinho")
        botaocart.send_keys(Keys.ENTER)
        time.sleep(2)

        self.assertEqual(driver.find_element(by=By.XPATH, value="/html/body/div/div/div/div[2]/div/center/h5").text,"Tablet Samsung")
        driver.get("http://127.0.0.1:8000/logout/")

    def test_cenario3(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/register/")
        usuario = driver.find_element(by=By.NAME, value="username")
        nome = driver.find_element(by=By.NAME, value="first_name")
        sobrenome = driver.find_element(by=By.NAME, value="last_name")
        email = driver.find_element(by=By.NAME, value="email")
        senha = driver.find_element(by=By.NAME, value="password1")
        confirmar_senha = driver.find_element(by=By.NAME, value="password2")
        botao = driver.find_element(by=By.NAME, value="registro")
        usuario.send_keys(f"User_3")
        nome.send_keys(f"Rodrigo")
        sobrenome.send_keys(f"Torre")
        email.send_keys(f"rtmr@cesar.school")
        senha.send_keys("Senha1234")
        confirmar_senha.send_keys("Senha1234")
        botao.send_keys(Keys.ENTER)
        time.sleep(2)

        driver.get("http://127.0.0.1:8000/")
        botao2 = driver.find_element(by=By.XPATH, value="/html/body/section/div/div/div[7]/div/div[2]/div/a")
        botao2.send_keys(Keys.ENTER)
        time.sleep(2)
        botaoadd = driver.find_element(by=By.ID, value="add-cart")
        botaoadd.send_keys(Keys.ENTER)
        time.sleep(2)
        botaocart = driver.find_element(by=By.NAME, value="carrinho")
        botaocart.send_keys(Keys.ENTER)
        time.sleep(2)
        
        self.assertEqual(driver.find_element(by=By.XPATH, value="/html/body/div/div/div/div[2]/div/center/h5").text,"Smartwatch")
        driver.get("http://127.0.0.1:8000/logout/")
        time.sleep(2)

        driver.get("http://127.0.0.1:8000/login/")
        usuario = driver.find_element(by=By.NAME, value="username")
        senha = driver.find_element(by=By.NAME, value="password")
        botao = driver.find_element(by=By.NAME, value="login")
        usuario.send_keys("User_3")
        senha.send_keys("Senha1234")
        botao.send_keys(Keys.ENTER)
        time.sleep(2)

        driver.get("http://127.0.0.1:8000/")
        botao2 = driver.find_element(by=By.XPATH, value="/html/body/section/div/div/div[15]/div/div[2]/div/a")
        botao2.send_keys(Keys.ENTER)
        time.sleep(2)
        botaoadd = driver.find_element(by=By.ID, value="add-cart")
        botaoadd.send_keys(Keys.ENTER)
        time.sleep(2)
        botaocart = driver.find_element(by=By.NAME, value="carrinho")
        botaocart.send_keys(Keys.ENTER)
        time.sleep(2)

        self.assertEqual(driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div/div[2]/div/center/h5").text,"Smartwatch")
        self.assertEqual(driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/div/div[2]/div/center/h5").text,"Samsung Buds")
        driver.get("http://127.0.0.1:8000/logout/")

    def test_cenario4(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/register/")
        usuario = driver.find_element(by=By.NAME, value="username")
        nome = driver.find_element(by=By.NAME, value="first_name")
        sobrenome = driver.find_element(by=By.NAME, value="last_name")
        email = driver.find_element(by=By.NAME, value="email")
        senha = driver.find_element(by=By.NAME, value="password1")
        confirmar_senha = driver.find_element(by=By.NAME, value="password2")
        botao = driver.find_element(by=By.NAME, value="registro")
        usuario.send_keys(f"User_3")
        nome.send_keys(f"Rodrigo")
        sobrenome.send_keys(f"Torre")
        email.send_keys(f"rtmr@cesar.school")
        senha.send_keys("Senha1234")
        confirmar_senha.send_keys("Senha1234")
        botao.send_keys(Keys.ENTER)
        time.sleep(2)

        driver.get("http://127.0.0.1:8000/")
        botao2 = driver.find_element(by=By.XPATH, value="/html/body/section/div/div/div[3]/div/div[2]/div/a")
        botao2.send_keys(Keys.ENTER)
        time.sleep(2)
        botaoqty = driver.find_element(by=By.XPATH, value="/html/body/div/div/div/div[2]/div/center/div/div[2]/select")
        chooser = Select(botaoqty)
        chooser.select_by_value('2')
        time.sleep(2)
        botaoadd = driver.find_element(by=By.ID, value="add-cart")
        botaoadd.send_keys(Keys.ENTER)
        time.sleep(2)
        botaocart = driver.find_element(by=By.NAME, value="carrinho")
        botaocart.send_keys(Keys.ENTER)
        time.sleep(6)
        
        self.assertEqual(driver.find_element(by=By.XPATH, value="/html/body/div/div/div/div[2]/div/center/h5").text,"Samsung Galaxy S23")
        self.assertEqual(driver.find_element(by=By.ID, value="total").text,"Total: R$6800,00")
        driver.get("http://127.0.0.1:8000/logout/")

class GerenciarCarrinho(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-browser-side-navigation")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1440,1080")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-extensions")
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def setUp(self):
        subprocess.run(['python', 'manage.py', 'createproducts'], check=True)

    def tearDown(self):
        subprocess.run(['python', 'manage.py', 'deleteproducts'], check=True)
        subprocess.run(['python', 'manage.py', 'deletedoubles'], check=True)
        subprocess.run(['python', 'manage.py', 'deleteusers'], check=True)

    def test_cenario1(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/register/")
        usuario = driver.find_element(by=By.NAME, value="username")
        nome = driver.find_element(by=By.NAME, value="first_name")
        sobrenome = driver.find_element(by=By.NAME, value="last_name")
        email = driver.find_element(by=By.NAME, value="email")
        senha = driver.find_element(by=By.NAME, value="password1")
        confirmar_senha = driver.find_element(by=By.NAME, value="password2")
        botao = driver.find_element(by=By.NAME, value="registro")

        usuario.send_keys(f"User_2")
        nome.send_keys(f"Felipe")
        sobrenome.send_keys(f"Camisa")
        email.send_keys(f"fcc3@cesar.school")
        senha.send_keys("Senha1234")
        confirmar_senha.send_keys("Senha1234")
        botao.send_keys(Keys.ENTER)
        time.sleep(2)

        driver.get("http://127.0.0.1:8000/")
        botao2 = driver.find_element(by=By.XPATH, value="/html/body/section/div/div/div[4]/div/div[2]/div/a")
        botao2.send_keys(Keys.ENTER)
        time.sleep(1)
        botaoadd = driver.find_element(by=By.ID, value="add-cart")
        botaoqty = driver.find_element(by=By.XPATH, value="/html/body/div/div/div/div[2]/div/center/div/div[2]/select")
        chooser = Select(botaoqty)
        chooser.select_by_value('3')
        time.sleep(2)
        botaoadd.send_keys(Keys.ENTER)
        time.sleep(1)
        botaocart = driver.find_element(by=By.NAME, value="carrinho")
        botaocart.send_keys(Keys.ENTER)
        time.sleep(2)

        botaoqty2 = driver.find_element(by=By.XPATH, value="/html/body/div/div/div/div[2]/div/center/div/div[2]/select")
        chooser2 = Select(botaoqty2)
        chooser2.select_by_value('5')
        time.sleep(2)
        botaoupdate = driver.find_element(by=By.ID, value="atualizar")
        botaoupdate.send_keys(Keys.ENTER)
        time.sleep(2)
        driver.refresh() #Verificando se a quantidade ainda será 5 depois de recarregar a página
        time.sleep(2)

        self.assertEqual(driver.find_element(by=By.XPATH, value="/html/body/div/div/div/div[2]/div/center/h5").text,"iPhone 13")
        self.assertEqual(driver.find_element(by=By.ID, value="total").text,"Total: R$16000,00")
        driver.get("http://127.0.0.1:8000/logout/")

    def test_cenario2(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/register/")
        usuario = driver.find_element(by=By.NAME, value="username")
        nome = driver.find_element(by=By.NAME, value="first_name")
        sobrenome = driver.find_element(by=By.NAME, value="last_name")
        email = driver.find_element(by=By.NAME, value="email")
        senha = driver.find_element(by=By.NAME, value="password1")
        confirmar_senha = driver.find_element(by=By.NAME, value="password2")
        botao = driver.find_element(by=By.NAME, value="registro")

        usuario.send_keys(f"User_2")
        nome.send_keys(f"Felipe")
        sobrenome.send_keys(f"Camisa")
        email.send_keys(f"fcc3@cesar.school")
        senha.send_keys("Senha1234")
        confirmar_senha.send_keys("Senha1234")
        botao.send_keys(Keys.ENTER)
        time.sleep(2)

        driver.get("http://127.0.0.1:8000/")
        botao2 = driver.find_element(by=By.XPATH, value="/html/body/section/div/div/div[4]/div/div[2]/div/a")
        botao2.send_keys(Keys.ENTER)
        time.sleep(1)
        botaoadd = driver.find_element(by=By.ID, value="add-cart")
        botaoqty = driver.find_element(by=By.XPATH, value="/html/body/div/div/div/div[2]/div/center/div/div[2]/select")
        chooser = Select(botaoqty)
        chooser.select_by_value('5')
        time.sleep(2)
        botaoadd.send_keys(Keys.ENTER)
        time.sleep(1)
        botaocart = driver.find_element(by=By.NAME, value="carrinho")
        botaocart.send_keys(Keys.ENTER)
        time.sleep(2)

        driver.get("http://127.0.0.1:8000/")
        botao2 = driver.find_element(by=By.XPATH, value="/html/body/section/div/div/div[2]/div/div[2]/div/a")
        botao2.send_keys(Keys.ENTER)
        time.sleep(2)
        botaoadd = driver.find_element(by=By.ID, value="add-cart")
        botaoqty = driver.find_element(by=By.XPATH, value="/html/body/div/div/div/div[2]/div/center/div/div[2]/select")
        chooser = Select(botaoqty)
        chooser.select_by_value('5')
        time.sleep(2)
        botaoadd.send_keys(Keys.ENTER)
        time.sleep(2)
        botaocart = driver.find_element(by=By.NAME, value="carrinho")
        botaocart.send_keys(Keys.ENTER)
        time.sleep(2)

        self.assertEqual(driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div/div[2]/div/center/h5").text,"Macbook")
        self.assertEqual(driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/div/div[2]/div/center/h5").text,"iPhone 13")
        self.assertEqual(driver.find_element(by=By.ID, value="total").text,"Total: R$30000,00")
        botaodel = driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/div/div[2]/div/center/button[2]")
        botaodel.send_keys(Keys.ENTER)
        time.sleep(2)
        
        self.assertEqual(driver.find_element(by=By.ID, value="total").text,"Total: R$14000,00")
        driver.get("http://127.0.0.1:8000/logout/")

class ProcurarPorCategoria(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-browser-side-navigation")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1440,1080")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-extensions")
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def setUp(self):
        subprocess.run(['python', 'manage.py', 'createproducts'], check=True)

    def tearDown(self):
        subprocess.run(['python', 'manage.py', 'deleteproducts'], check=True)
        subprocess.run(['python', 'manage.py', 'deletedoubles'], check=True)

    def test_cenario1(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        time.sleep(2)
        botao = driver.find_element(by=By.XPATH, value="/html/body/nav/div/div/ul[1]/li[4]/a")
        botao.send_keys(Keys.ENTER)
        time.sleep(1)
        botao2 = driver.find_element(by=By.NAME, value="notebooks")
        botao2.send_keys(Keys.ENTER)
        self.assertEqual(driver.find_element(by=By.NAME, value="title").text,"Notebooks")
        time.sleep(2)
        botao = driver.find_element(by=By.XPATH, value="/html/body/nav/div/div/ul[1]/li[4]/a")
        botao.send_keys(Keys.ENTER)
        time.sleep(1)
        botao3 = driver.find_element(by=By.NAME, value="celulares")
        botao3.send_keys(Keys.ENTER)
        self.assertEqual(driver.find_element(by=By.NAME, value="title").text,"Celulares")
        time.sleep(2)
        botao = driver.find_element(by=By.XPATH, value="/html/body/nav/div/div/ul[1]/li[4]/a")
        botao.send_keys(Keys.ENTER)
        time.sleep(1)
        botao4 = driver.find_element(by=By.NAME, value="tablets")
        botao4.send_keys(Keys.ENTER)
        self.assertEqual(driver.find_element(by=By.NAME, value="title").text,"Tablets")
        time.sleep(2)
        botao = driver.find_element(by=By.XPATH, value="/html/body/nav/div/div/ul[1]/li[4]/a")
        botao.send_keys(Keys.ENTER)
        time.sleep(1)
        botao5 = driver.find_element(by=By.NAME, value="smartwatchs")
        botao5.send_keys(Keys.ENTER)
        self.assertEqual(driver.find_element(by=By.NAME, value="title").text,"Smartwatchs")
        time.sleep(2)
        botao = driver.find_element(by=By.XPATH, value="/html/body/nav/div/div/ul[1]/li[4]/a")
        botao.send_keys(Keys.ENTER)
        time.sleep(1)
        botao6 = driver.find_element(by=By.NAME, value="fones")
        botao6.send_keys(Keys.ENTER)
        self.assertEqual(driver.find_element(by=By.NAME, value="title").text,"Fones de ouvido")

    def test_cenario2(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        time.sleep(2)
        botao = driver.find_element(by=By.XPATH, value="/html/body/nav/div/div/ul[1]/li[4]/a")
        botao.send_keys(Keys.ENTER)
        time.sleep(1)
        botao2 = driver.find_element(by=By.NAME, value="all")
        botao2.send_keys(Keys.ENTER)
        time.sleep(2)
        botao3 = driver.find_element(by=By.XPATH, value="/html/body/div/div/div/div/a[1]")
        botao3.send_keys(Keys.ENTER)
        time.sleep(2)
        self.assertEqual(driver.find_element(by=By.NAME, value="title").text,"Notebooks")
        driver.get("http://127.0.0.1:8000/category_summary/")
        time.sleep(2)
        botao4 = driver.find_element(by=By.XPATH, value="/html/body/div/div/div/div/a[2]")
        botao4.send_keys(Keys.ENTER)
        time.sleep(2)
        self.assertEqual(driver.find_element(by=By.NAME, value="title").text,"Celulares")
        driver.get("http://127.0.0.1:8000/category_summary/")
        time.sleep(2)
        botao5 = driver.find_element(by=By.XPATH, value="/html/body/div/div/div/div/a[3]")
        botao5.send_keys(Keys.ENTER)
        time.sleep(2)
        self.assertEqual(driver.find_element(by=By.NAME, value="title").text,"Tablets")
        driver.get("http://127.0.0.1:8000/category_summary/")
        time.sleep(2)
        botao6 = driver.find_element(by=By.XPATH, value="/html/body/div/div/div/div/a[4]")
        botao6.send_keys(Keys.ENTER)
        time.sleep(2)
        self.assertEqual(driver.find_element(by=By.NAME, value="title").text,"Smartwatchs")
        driver.get("http://127.0.0.1:8000/category_summary/")
        time.sleep(2)
        botao7 = driver.find_element(by=By.XPATH, value="/html/body/div/div/div/div/a[5]")
        botao7.send_keys(Keys.ENTER)
        time.sleep(2)
        self.assertEqual(driver.find_element(by=By.NAME, value="title").text,"Fones de ouvido")

class Contato(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-browser-side-navigation")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1440,1080")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-extensions")
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def setUp(self):
        subprocess.run(['python', 'manage.py', 'createproducts'], check=True)

    def tearDown(self):
        subprocess.run(['python', 'manage.py', 'deleteproducts'], check=True)
        subprocess.run(['python', 'manage.py', 'deletedoubles'], check=True)
        subprocess.run(['python', 'manage.py', 'deleteusers'], check=True)

    def test_cenario1_and_2(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        botao = driver.find_element(by=By.XPATH, value="/html/body/nav/div/div/ul[1]/li[5]/a")
        botao.send_keys(Keys.ENTER)
        time.sleep(1)
        self.assertEqual(driver.find_element(by=By.NAME, value="logmsg").text,"Para enviar uma reclamação, você precisa estar logado/registrado.")
        botao2 = driver.find_element(by=By.XPATH, value="/html/body/center/a[2]")
        botao2.send_keys(Keys.ENTER)
        time.sleep(1)

        usuario = driver.find_element(by=By.NAME, value="username")
        nome = driver.find_element(by=By.NAME, value="first_name")
        sobrenome = driver.find_element(by=By.NAME, value="last_name")
        email = driver.find_element(by=By.NAME, value="email")
        senha = driver.find_element(by=By.NAME, value="password1")
        confirmar_senha = driver.find_element(by=By.NAME, value="password2")
        botao = driver.find_element(by=By.NAME, value="registro")

        usuario.send_keys(f"User_4")
        nome.send_keys(f"Miguel")
        sobrenome.send_keys(f"Becker")
        email.send_keys(f"mcb4@cesar.school")
        senha.send_keys("Senha1234")
        confirmar_senha.send_keys("Senha1234")
        botao.send_keys(Keys.ENTER)
        time.sleep(2)

        driver.get("http://127.0.0.1:8000/contato/contato/")
        assunto = driver.find_element(by=By.NAME, value="assunto")
        enviar = driver.find_element(by=By.XPATH, value="/html/body/center/div/div/div/form/button")
        assunto.send_keys(f"iPhone 13 está muito caro!")
        time.sleep(1)
        enviar.send_keys(Keys.ENTER)
        self.assertEqual(driver.find_element(by=By.XPATH, value="/html/body/center/form/div/div/div").text,"iPhone 13 está muito caro!")
        time.sleep(2)

        driver.get("http://127.0.0.1:8000/contato/contato/")
        assunto = driver.find_element(by=By.NAME, value="assunto")
        enviar = driver.find_element(by=By.XPATH, value="/html/body/center/div/div/div/form/button")
        assunto.send_keys(f"Notebook Lenovo está muito caro!")
        time.sleep(1)
        enviar.send_keys(Keys.ENTER)
        time.sleep(2)

        self.assertEqual(driver.find_element(by=By.XPATH, value="/html/body/center/form/div[2]/div/div").text,"Notebook Lenovo está muito caro!")
        driver.get("http://127.0.0.1:8000/logout/")

    def test_cenario3(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/register/")
        usuario = driver.find_element(by=By.NAME, value="username")
        nome = driver.find_element(by=By.NAME, value="first_name")
        sobrenome = driver.find_element(by=By.NAME, value="last_name")
        email = driver.find_element(by=By.NAME, value="email")
        senha = driver.find_element(by=By.NAME, value="password1")
        confirmar_senha = driver.find_element(by=By.NAME, value="password2")
        botao = driver.find_element(by=By.NAME, value="registro")

        usuario.send_keys(f"User_4")
        nome.send_keys(f"Miguel")
        sobrenome.send_keys(f"Becker")
        email.send_keys(f"mcb4@cesar.school")
        senha.send_keys("Senha1234")
        confirmar_senha.send_keys("Senha1234")
        botao.send_keys(Keys.ENTER)
        time.sleep(2)

        driver.get("http://127.0.0.1:8000/contato/contato/")
        assunto = driver.find_element(by=By.NAME, value="assunto")
        enviar = driver.find_element(by=By.XPATH, value="/html/body/center/div/div/div/form/button")
        assunto.send_keys(f"iPhone 13 está muito caro!")
        time.sleep(1)
        enviar.send_keys(Keys.ENTER)
        driver.get("http://127.0.0.1:8000/contato/contato/")
        assunto = driver.find_element(by=By.NAME, value="assunto")
        enviar = driver.find_element(by=By.XPATH, value="/html/body/center/div/div/div/form/button")
        assunto.send_keys(f"Notebook Lenovo está muito caro!")
        time.sleep(2)
        enviar.send_keys(Keys.ENTER)
        self.assertEqual(driver.find_element(by=By.XPATH, value="/html/body/center/form/div[1]/div/div").text,"iPhone 13 está muito caro!")
        self.assertEqual(driver.find_element(by=By.XPATH, value="/html/body/center/form/div[2]/div/div").text,"Notebook Lenovo está muito caro!")
        time.sleep(1)
        driver.get("http://127.0.0.1:8000/logout/")
        time.sleep(2)

        driver.get("http://127.0.0.1:8000/login/")
        usuario = driver.find_element(by=By.NAME, value="username")
        senha = driver.find_element(by=By.NAME, value="password")
        botao = driver.find_element(by=By.NAME, value="login")
        usuario.send_keys("User_4")
        senha.send_keys("Senha1234")
        botao.send_keys(Keys.ENTER)
        time.sleep(2)

        driver.get("http://127.0.0.1:8000/contato/complaints/")
        time.sleep(2)
        self.assertEqual(driver.find_element(by=By.XPATH, value="/html/body/center/form/div[1]/div/div").text,"iPhone 13 está muito caro!")
        self.assertEqual(driver.find_element(by=By.XPATH, value="/html/body/center/form/div[2]/div/div").text,"Notebook Lenovo está muito caro!")
        driver.get("http://127.0.0.1:8000/logout/")

    def test_cenario4(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/register/")
        usuario = driver.find_element(by=By.NAME, value="username")
        nome = driver.find_element(by=By.NAME, value="first_name")
        sobrenome = driver.find_element(by=By.NAME, value="last_name")
        email = driver.find_element(by=By.NAME, value="email")
        senha = driver.find_element(by=By.NAME, value="password1")
        confirmar_senha = driver.find_element(by=By.NAME, value="password2")
        botao = driver.find_element(by=By.NAME, value="registro")

        usuario.send_keys(f"User_5")
        nome.send_keys(f"Bernardo")
        sobrenome.send_keys(f"Hauer")
        email.send_keys(f"bch@cesar.school")
        senha.send_keys("Senha1234")
        confirmar_senha.send_keys("Senha1234")
        botao.send_keys(Keys.ENTER)
        time.sleep(2)

        driver.get("http://127.0.0.1:8000/contato/contato/")
        assunto = driver.find_element(by=By.NAME, value="assunto")
        enviar = driver.find_element(by=By.XPATH, value="/html/body/center/div/div/div/form/button")
        assunto.send_keys(f"Poucos produtos! Quero mais!")
        time.sleep(1)
        enviar.send_keys(Keys.ENTER)
        time.sleep(2)

        self.assertEqual(driver.find_element(by=By.XPATH, value="/html/body/center/form/div/div/div").text,"Poucos produtos! Quero mais!")
        driver.get("http://127.0.0.1:8000/logout/")

class AdicionarComentarios(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-browser-side-navigation")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1440,1080")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-extensions")
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def setUp(self):
        subprocess.run(['python', 'manage.py', 'createproducts'], check=True)

    def tearDown(self):
        subprocess.run(['python', 'manage.py', 'deleteproducts'], check=True)
        subprocess.run(['python', 'manage.py', 'deletedoubles'], check=True)
        subprocess.run(['python', 'manage.py', 'deleteusers'], check=True)

    def test_cenario1_and_2(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        botao = driver.find_element(by=By.XPATH, value="/html/body/section/div/div/div[4]/div/div[2]/div/a")
        botao.send_keys(Keys.ENTER)
        time.sleep(2)
        self.assertEqual(driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/div/p").text,"Para adicionar um comentário, você precisa estar logado/registrado.")
        botao2 = driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/div/a[2]")
        botao2.send_keys(Keys.ENTER)
        time.sleep(1)
        
        usuario = driver.find_element(by=By.NAME, value="username")
        nome = driver.find_element(by=By.NAME, value="first_name")
        sobrenome = driver.find_element(by=By.NAME, value="last_name")
        email = driver.find_element(by=By.NAME, value="email")
        senha = driver.find_element(by=By.NAME, value="password1")
        confirmar_senha = driver.find_element(by=By.NAME, value="password2")
        botao = driver.find_element(by=By.NAME, value="registro")

        usuario.send_keys(f"Caminha_21032006")
        nome.send_keys(f"Teteu")
        sobrenome.send_keys(f"Brazao")
        email.send_keys(f"gustavson@cesar.school")
        senha.send_keys("Suadao1234")
        confirmar_senha.send_keys("Suadao1234")
        botao.send_keys(Keys.ENTER)
        time.sleep(2)

        driver.get("http://127.0.0.1:8000/")
        botao2 = driver.find_element(by=By.XPATH, value="/html/body/section/div/div/div[4]/div/div[2]/div/a")
        botao2.send_keys(Keys.ENTER)
        time.sleep(1)

        comentario = driver.find_element(by=By.NAME, value="texto")
        comentario.send_keys(f"Esse iphone é muito bonito, gostei!")
        time.sleep(1)
        enviarcomentario = driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/div/form/button")
        enviarcomentario.send_keys(Keys.ENTER)
        time.sleep(2)
        self.assertEqual(driver.find_element(by=By.XPATH, value="/html/body/div/div[3]/div/div[1]/div/p[1]").text,"Esse iphone é muito bonito, gostei!")
        driver.get("http://127.0.0.1:8000/logout/")

    def test_cenario3(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/register/")
        usuario = driver.find_element(by=By.NAME, value="username")
        nome = driver.find_element(by=By.NAME, value="first_name")
        sobrenome = driver.find_element(by=By.NAME, value="last_name")
        email = driver.find_element(by=By.NAME, value="email")
        senha = driver.find_element(by=By.NAME, value="password1")
        confirmar_senha = driver.find_element(by=By.NAME, value="password2")
        botao = driver.find_element(by=By.NAME, value="registro")

        usuario.send_keys(f"Caminha_21032006")
        nome.send_keys(f"Teteu")
        sobrenome.send_keys(f"Brazao")
        email.send_keys(f"gustavson@cesar.school")
        senha.send_keys("Suadao1234")
        confirmar_senha.send_keys("Suadao1234")
        botao.send_keys(Keys.ENTER)
        time.sleep(2)

        driver.get("http://127.0.0.1:8000/")
        botao2 = driver.find_element(by=By.XPATH, value="/html/body/section/div/div/div[4]/div/div[2]/div/a")
        botao2.send_keys(Keys.ENTER)
        time.sleep(1)

        comentario = driver.find_element(by=By.NAME, value="texto")
        comentario.send_keys(f"Esse iphone é muito bonito, gostei!")
        time.sleep(1)
        enviarcomentario = driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/div/form/button")
        enviarcomentario.send_keys(Keys.ENTER)
        time.sleep(2)
        self.assertEqual(driver.find_element(by=By.XPATH, value="/html/body/div/div[3]/div/div[1]/div/p[1]").text,"Esse iphone é muito bonito, gostei!")
        driver.get("http://127.0.0.1:8000/logout/")

        driver.get("http://127.0.0.1:8000/register/")
        usuario = driver.find_element(by=By.NAME, value="username")
        nome = driver.find_element(by=By.NAME, value="first_name")
        sobrenome = driver.find_element(by=By.NAME, value="last_name")
        email = driver.find_element(by=By.NAME, value="email")
        senha = driver.find_element(by=By.NAME, value="password1")
        confirmar_senha = driver.find_element(by=By.NAME, value="password2")
        botao = driver.find_element(by=By.NAME, value="registro")

        usuario.send_keys(f"Suwado_d3m41s")
        nome.send_keys(f"Beckinho")
        sobrenome.send_keys(f"do Joguinho")
        email.send_keys(f"kuffour@cesar.school")
        senha.send_keys("Suadao1234")
        confirmar_senha.send_keys("Suadao1234")
        botao.send_keys(Keys.ENTER)
        time.sleep(2)

        driver.get("http://127.0.0.1:8000/")
        botao2 = driver.find_element(by=By.XPATH, value="/html/body/section/div/div/div[4]/div/div[2]/div/a")
        botao2.send_keys(Keys.ENTER)
        time.sleep(2)

        comentario = driver.find_element(by=By.NAME, value="texto")
        comentario.send_keys(f"Esse iphone esta muito caro, Que assalto!")
        time.sleep(1)
        enviarcomentario = driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/div/form/button")
        enviarcomentario.send_keys(Keys.ENTER)
        time.sleep(2)
        self.assertEqual(driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[3]/div/div[1]/div/p[1]").text,"Esse iphone é muito bonito, gostei!")
        self.assertEqual(driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[3]/div/div[2]/div/p[1]").text,"Esse iphone esta muito caro, Que assalto!")
        driver.get("http://127.0.0.1:8000/logout/")
    
    def test_cenario4(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/register/")
        usuario = driver.find_element(by=By.NAME, value="username")
        nome = driver.find_element(by=By.NAME, value="first_name")
        sobrenome = driver.find_element(by=By.NAME, value="last_name")
        email = driver.find_element(by=By.NAME, value="email")
        senha = driver.find_element(by=By.NAME, value="password1")
        confirmar_senha = driver.find_element(by=By.NAME, value="password2")
        botao = driver.find_element(by=By.NAME, value="registro")

        usuario.send_keys(f"Suwado_d3m41s")
        nome.send_keys(f"Beckinho")
        sobrenome.send_keys(f"do Joguinho")
        email.send_keys(f"kuffour@cesar.school")
        senha.send_keys("Suadao1234")
        confirmar_senha.send_keys("Suadao1234")
        botao.send_keys(Keys.ENTER)
        time.sleep(2)

        driver.get("http://127.0.0.1:8000/")
        botao2 = driver.find_element(by=By.XPATH, value="/html/body/section/div/div/div[1]/div/div[2]/div/a")
        botao2.send_keys(Keys.ENTER)
        time.sleep(2)
        comentario = driver.find_element(by=By.NAME, value="texto")
        comentario.send_keys(f"Esse Lenovo esta muito caro, Que assalto!")
        time.sleep(1)
        enviarcomentario = driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/div/form/button")
        enviarcomentario.send_keys(Keys.ENTER)
        time.sleep(2)
        self.assertEqual(driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[3]/div/div/div/p[1]").text,"Esse Lenovo esta muito caro, Que assalto!")
        driver.get("http://127.0.0.1:8000/logout/")

class AdicionarAosFavoritos(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-browser-side-navigation")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1440,1080")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-extensions")
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def setUp(self):
        subprocess.run(['python', 'manage.py', 'createproducts'], check=True)

    def tearDown(self):
        subprocess.run(['python', 'manage.py', 'deleteproducts'], check=True)
        subprocess.run(['python', 'manage.py', 'deletedoubles'], check=True)
        subprocess.run(['python', 'manage.py', 'deleteusers'], check=True)

    def test_cenario1(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        botao2 = driver.find_element(by=By.XPATH, value="/html/body/section/div/div/div[1]/div/div[2]/div/a")
        botao2.send_keys(Keys.ENTER)
        time.sleep(2)
        self.assertEqual(driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div/div[2]/div/center/h5[2]").text,"Para adicionar um produto ao carrinho ou aos favoritos, você precisa estar logado/registrado.")
        time.sleep(1)

        driver.get("http://127.0.0.1:8000/register/")
        usuario = driver.find_element(by=By.NAME, value="username")
        nome = driver.find_element(by=By.NAME, value="first_name")
        sobrenome = driver.find_element(by=By.NAME, value="last_name")
        email = driver.find_element(by=By.NAME, value="email")
        senha = driver.find_element(by=By.NAME, value="password1")
        confirmar_senha = driver.find_element(by=By.NAME, value="password2")
        botao = driver.find_element(by=By.NAME, value="registro")

        usuario.send_keys(f"Rodrigo_Torres1988")
        nome.send_keys(f"Rodrigo")
        sobrenome.send_keys(f"Torres")
        email.send_keys(f"Torres@cesar.school")
        senha.send_keys("Suadao1234")
        confirmar_senha.send_keys("Suadao1234")
        botao.send_keys(Keys.ENTER)
        time.sleep(2)

        driver.get("http://127.0.0.1:8000/")
        botao2 = driver.find_element(by=By.XPATH, value="/html/body/section/div/div/div[1]/div/div[2]/div/a")
        botao2.send_keys(Keys.ENTER)
        time.sleep(2)

        favoritos = driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div/div[2]/div/center/button[2]")
        favoritos.send_keys(Keys.ENTER)
        time.sleep(2)

        driver.get("http://127.0.0.1:8000/")
        botao3= driver.find_element(by=By.XPATH, value="/html/body/section/div/div/div[2]/div/div[2]/div/a")
        botao3.send_keys(Keys.ENTER)
        time.sleep(2)

        favoritos2 = driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div/div[2]/div/center/button[2]")
        favoritos2.send_keys(Keys.ENTER)
        time.sleep(2)
        driver.get("http://127.0.0.1:8000/favoritos")
        time.sleep(2)
        self.assertEqual(driver.find_element(by=By.XPATH, value="/html/body/div/div/div[1]/div/div/center[1]/h5").text,"Notebook Lenovo")
        self.assertEqual(driver.find_element(by=By.XPATH, value="/html/body/div/div/div[2]/div/div/center[1]/h5").text,"Macbook")
        driver.get("http://127.0.0.1:8000/logout/")

    def test_cenario2(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/register/")
        usuario = driver.find_element(by=By.NAME, value="username")
        nome = driver.find_element(by=By.NAME, value="first_name")
        sobrenome = driver.find_element(by=By.NAME, value="last_name")
        email = driver.find_element(by=By.NAME, value="email")
        senha = driver.find_element(by=By.NAME, value="password1")
        confirmar_senha = driver.find_element(by=By.NAME, value="password2")
        botao = driver.find_element(by=By.NAME, value="registro")

        usuario.send_keys(f"Braz_J0se")
        nome.send_keys(f"Neto")
        sobrenome.send_keys(f"Oliveira")
        email.send_keys(f"seilamano@cesar.school")
        senha.send_keys("Suadao1234")
        confirmar_senha.send_keys("Suadao1234")
        botao.send_keys(Keys.ENTER)
        time.sleep(2)
        
        driver.get("http://127.0.0.1:8000/")
        botao2 = driver.find_element(by=By.XPATH, value="/html/body/section/div/div/div[4]/div/div[2]/div/a")
        botao2.send_keys(Keys.ENTER)
        time.sleep(2)

        favoritos = driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div/div[2]/div/center/button[2]")
        favoritos.send_keys(Keys.ENTER)
        time.sleep(2)
        driver.get("http://127.0.0.1:8000/logout/")
        time.sleep(1)

        driver.get("http://127.0.0.1:8000/register/")
        usuario = driver.find_element(by=By.NAME, value="username")
        nome = driver.find_element(by=By.NAME, value="first_name")
        sobrenome = driver.find_element(by=By.NAME, value="last_name")
        email = driver.find_element(by=By.NAME, value="email")
        senha = driver.find_element(by=By.NAME, value="password1")
        confirmar_senha = driver.find_element(by=By.NAME, value="password2")
        botao = driver.find_element(by=By.NAME, value="registro")

        usuario.send_keys(f"Rodrigo_Torres1988")
        nome.send_keys(f"Rodrigo")
        sobrenome.send_keys(f"Torres")
        email.send_keys(f"Torres@cesar.school")
        senha.send_keys("Suadao1234")
        confirmar_senha.send_keys("Suadao1234")
        botao.send_keys(Keys.ENTER)
        time.sleep(2)

        driver.get("http://127.0.0.1:8000/favoritos")
        time.sleep(2)
        self.assertEqual(driver.find_element(by=By.XPATH, value="/html/body/div/center/h5").text,"Não existem produtos nos seus favoritos.")
        driver.get("http://127.0.0.1:8000/logout/")

class RemoverDosFavoritos(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-browser-side-navigation")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1440,1080")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-extensions")
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def setUp(self):
        subprocess.run(['python', 'manage.py', 'createproducts'], check=True)

    def tearDown(self):
        subprocess.run(['python', 'manage.py', 'deleteproducts'], check=True)
        subprocess.run(['python', 'manage.py', 'deletedoubles'], check=True)
        subprocess.run(['python', 'manage.py', 'deleteusers'], check=True)

    def test_cenario1(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/favoritos/")
        self.assertEqual(driver.find_element(by=By.XPATH, value="/html/body/div/center/div/h5").text,"Para gerenciar/ver seus produtos favoritos, você precisa estar logado/registrado.")
        time.sleep(2)

    def test_cenario2(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/register/")
        usuario = driver.find_element(by=By.NAME, value="username")
        nome = driver.find_element(by=By.NAME, value="first_name")
        sobrenome = driver.find_element(by=By.NAME, value="last_name")
        email = driver.find_element(by=By.NAME, value="email")
        senha = driver.find_element(by=By.NAME, value="password1")
        confirmar_senha = driver.find_element(by=By.NAME, value="password2")
        botao = driver.find_element(by=By.NAME, value="registro")

        usuario.send_keys(f"João_Claudio1988")
        nome.send_keys(f"Jocla")
        sobrenome.send_keys(f"Torres")
        email.send_keys(f"Joclinha@cesar.school")
        senha.send_keys("Suadao1234")
        confirmar_senha.send_keys("Suadao1234")
        botao.send_keys(Keys.ENTER)
        time.sleep(2)

        driver.get("http://127.0.0.1:8000/")
        botao2 = driver.find_element(by=By.XPATH, value="/html/body/section/div/div/div[1]/div/div[2]/div/a")
        botao2.send_keys(Keys.ENTER)
        time.sleep(2)
        favoritos = driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div/div[2]/div/center/button[2]")
        favoritos.send_keys(Keys.ENTER)
        time.sleep(2)

        driver.get("http://127.0.0.1:8000/favoritos")
        time.sleep(1)
        remover = driver.find_element(by=By.XPATH,value="/html/body/div/div/div/div/div/center[3]/button")
        remover.send_keys(Keys.ENTER)
        time.sleep(2)
        self.assertEqual(driver.find_element(by=By.XPATH, value="/html/body/div[2]/center/h5").text,"Não existem produtos nos seus favoritos.")
        driver.get("http://127.0.0.1:8000/logout/")
