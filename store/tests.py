from django.test import LiveServerTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium import webdriver
from django.core.management import call_command
import time, subprocess

driver = webdriver.Chrome()

class AtualizarPerfil(LiveServerTestCase):

    def setUp(self):
        subprocess.run(['python', 'manage.py', 'createproducts'], check=True)

    def tearDown(self):
        subprocess.run(['python', 'manage.py', 'deleteproducts'], check=True)
        subprocess.run(['python', 'manage.py', 'deletedoubles'], check=True)
        subprocess.run(['python', 'manage.py', 'deleteusers'], check=True)

    def test_cenario1(self):
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

    def test_cenario2(self):
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
        time.sleep(4)

class PesquisarProduto(LiveServerTestCase):

    def setUp(self):
        subprocess.run(['python', 'manage.py', 'createproducts'], check=True)

    def tearDown(self):
        subprocess.run(['python', 'manage.py', 'deleteproducts'], check=True)
        subprocess.run(['python', 'manage.py', 'deletedoubles'], check=True)

    def test_cenario3(self):
        driver.get("http://127.0.0.1:8000/search/")
        pesquisa = driver.find_element(by=By.NAME, value="searched")
        botao = driver.find_element(by=By.NAME, value="go")

        pesquisa.send_keys("iPhone")
        time.sleep(2)
        botao.send_keys(Keys.ENTER)
        self.assertEqual(driver.find_element(by=By.XPATH, value="/html/body/div/div/center/div/div[2]/div/div/div[1]/div/h5").text,"iPhone 13")
        time.sleep(2)

    def test_cenario4(self):

        driver.get("http://127.0.0.1:8000/search/")
        pesquisa = driver.find_element(by=By.NAME, value="searched")
        botao = driver.find_element(by=By.NAME, value="go")

        pesquisa.send_keys("8gb")
        time.sleep(2)
        botao.send_keys(Keys.ENTER)
        self.assertEqual(driver.find_element(by=By.XPATH, value="/html/body/div/div/center/div/div[2]/div[4]/div/div[1]/div/h5").text,"iPhone 13")
        time.sleep(2)

    def test_cenario5(self):
        driver.get("http://127.0.0.1:8000/search/")
        pesquisa = driver.find_element(by=By.NAME, value="searched")
        botao = driver.find_element(by=By.NAME, value="go")

        pesquisa.send_keys("Fechadura eletrônica")
        time.sleep(2)
        botao.send_keys(Keys.ENTER)
        self.assertEqual(driver.find_element(by=By.XPATH, value="/html/body/div[1]").text,"Não achamos nenhum produto, tente denovo")
        time.sleep(2)

class AdicionarNoCarrinho(LiveServerTestCase):

    def setUp(self):
        subprocess.run(['python', 'manage.py', 'createproducts'], check=True)

    def tearDown(self):
        subprocess.run(['python', 'manage.py', 'deleteproducts'], check=True)
        subprocess.run(['python', 'manage.py', 'deletedoubles'], check=True)
        subprocess.run(['python', 'manage.py', 'deleteusers'], check=True)

    def test_cenario6(self):
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
        time.sleep(2)

    def test_cenario7(self):
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
        time.sleep(1)

    def test_cenario8(self):
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
        time.sleep(3)


class GerenciarCarrinho(LiveServerTestCase):

    def test_cenario9(self):
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
        botao2 = driver.find_element(by=By.XPATH, value="/html/body/section/div/div/div[1]/div/div[2]/div/a")
        botao2.send_keys(Keys.ENTER)
        time.sleep(2)
        botaoadd = driver.find_element(by=By.ID, value="add-cart")
        botaoqty = driver.find_element(by=By.XPATH, value="/html/body/div/div/div/div[2]/div/center/div/div[2]/select")
        chooser = Select(botaoqty)
        chooser.select_by_value('3')
        time.sleep(2)
        botaoadd.send_keys(Keys.ENTER)
        time.sleep(2)
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
        driver.get("http://127.0.0.1:8000/")
        time.sleep(2)
        driver.get("http://127.0.0.1:8000/cart/")
        time.sleep(2)

        self.assertEqual(driver.find_element(by=By.ID, value="total").text,"Total: R$12500.00")
        driver.get("http://127.0.0.1:8000/logout/")
        time.sleep(3)

    def test_cenario92(self):
        driver.get("http://127.0.0.1:8000/login/")
        usuario = driver.find_element(by=By.NAME, value="username")
        senha = driver.find_element(by=By.NAME, value="password")
        botao = driver.find_element(by=By.NAME, value="login")

        usuario.send_keys("User_2")
        senha.send_keys("Senha1234")
        botao.send_keys(Keys.ENTER)
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
        botaodel = driver.find_element(by=By.ID, value="remova")
        botaodel.send_keys(Keys.ENTER)
        time.sleep(2)
        
        self.assertEqual(driver.find_element(by=By.ID, value="total").text,"Total: R$14000.00")
        driver.get("http://127.0.0.1:8000/logout/")
        time.sleep(3)

class ProcurarPorCategoria(LiveServerTestCase):

    def test_cenario11(self):
        driver.get("http://127.0.0.1:8000/")
        time.sleep(2)
        botao = driver.find_element(by=By.XPATH, value="/html/body/nav/div/div/ul/li[6]/a")
        botao.send_keys(Keys.ENTER)
        time.sleep(1)
        botao2 = driver.find_element(by=By.NAME, value="notebooks")
        botao2.send_keys(Keys.ENTER)
        self.assertEqual(driver.find_element(by=By.NAME, value="title").text,"Notebooks")
        time.sleep(2)
        botao = driver.find_element(by=By.XPATH, value="/html/body/nav/div/div/ul/li[6]/a")
        botao.send_keys(Keys.ENTER)
        time.sleep(1)
        botao3 = driver.find_element(by=By.NAME, value="celulares")
        botao3.send_keys(Keys.ENTER)
        self.assertEqual(driver.find_element(by=By.NAME, value="title").text,"Celulares")
        time.sleep(2)
        botao = driver.find_element(by=By.XPATH, value="/html/body/nav/div/div/ul/li[6]/a")
        botao.send_keys(Keys.ENTER)
        time.sleep(1)
        botao4 = driver.find_element(by=By.NAME, value="tablets")
        botao4.send_keys(Keys.ENTER)
        self.assertEqual(driver.find_element(by=By.NAME, value="title").text,"Tablets")
        time.sleep(2)
        botao = driver.find_element(by=By.XPATH, value="/html/body/nav/div/div/ul/li[6]/a")
        botao.send_keys(Keys.ENTER)
        time.sleep(1)
        botao5 = driver.find_element(by=By.NAME, value="smartwatchs")
        botao5.send_keys(Keys.ENTER)
        self.assertEqual(driver.find_element(by=By.NAME, value="title").text,"Smartwatchs")
        time.sleep(2)
        botao = driver.find_element(by=By.XPATH, value="/html/body/nav/div/div/ul/li[6]/a")
        botao.send_keys(Keys.ENTER)
        time.sleep(1)
        botao6 = driver.find_element(by=By.NAME, value="fones")
        botao6.send_keys(Keys.ENTER)
        self.assertEqual(driver.find_element(by=By.NAME, value="title").text,"Fones de ouvido")
        time.sleep(2)

    def testcenario16(self):
        driver.get("http://127.0.0.1:8000/")
        time.sleep(2)
        botao = driver.find_element(by=By.XPATH, value="/html/body/nav/div/div/ul/li[6]/a")
        botao.send_keys(Keys.ENTER)
        time.sleep(1)
        botao2 = driver.find_element(by=By.NAME, value="all")
        botao2.send_keys(Keys.ENTER)
        time.sleep(2)
        botao3 = driver.find_element(by=By.XPATH, value="/html/body/div/div/center/div/h3[1]/a")
        botao3.send_keys(Keys.ENTER)
        time.sleep(2)
        self.assertEqual(driver.find_element(by=By.NAME, value="title").text,"Notebooks")
        driver.get("http://127.0.0.1:8000/category_summary/")
        time.sleep(2)
        botao4 = driver.find_element(by=By.XPATH, value="/html/body/div/div/center/div/h3[2]/a")
        botao4.send_keys(Keys.ENTER)
        time.sleep(2)
        self.assertEqual(driver.find_element(by=By.NAME, value="title").text,"Celulares")
        driver.get("http://127.0.0.1:8000/category_summary/")
        time.sleep(2)
        botao5 = driver.find_element(by=By.XPATH, value="/html/body/div/div/center/div/h3[3]/a")
        botao5.send_keys(Keys.ENTER)
        time.sleep(2)
        self.assertEqual(driver.find_element(by=By.NAME, value="title").text,"Tablets")
        driver.get("http://127.0.0.1:8000/category_summary/")
        time.sleep(2)
        botao6 = driver.find_element(by=By.XPATH, value="/html/body/div/div/center/div/h3[4]/a")
        botao6.send_keys(Keys.ENTER)
        time.sleep(2)
        self.assertEqual(driver.find_element(by=By.NAME, value="title").text,"Smartwatchs")
        driver.get("http://127.0.0.1:8000/category_summary/")
        time.sleep(2)
        botao7 = driver.find_element(by=By.XPATH, value="/html/body/div/div/center/div/h3[5]/a")
        botao7.send_keys(Keys.ENTER)
        time.sleep(2)
        self.assertEqual(driver.find_element(by=By.NAME, value="title").text,"Fones de ouvido")
        time.sleep(3)


class Contato(LiveServerTestCase):

    def test_cenario12(self):
        driver.get("http://127.0.0.1:8000/")
        time.sleep(2)
        botao = driver.find_element(by=By.XPATH, value="/html/body/nav/div/div/ul/li[7]/a")
        botao.send_keys(Keys.ENTER)
        self.assertEqual(driver.find_element(by=By.NAME, value="logmsg").text,"Para enviar uma reclamação, você precisa estar logado/registrado.")
        time.sleep(2)

    def test_cenario13(self):
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
        time.sleep(2)
        enviar.send_keys(Keys.ENTER)
        time.sleep(2)

        driver.get("http://127.0.0.1:8000/contato/contato/")
        assunto = driver.find_element(by=By.NAME, value="assunto")
        enviar = driver.find_element(by=By.XPATH, value="/html/body/center/div/div/div/form/button")
        assunto.send_keys(f"Notebook Lenovo está muito caro!")
        time.sleep(2)
        enviar.send_keys(Keys.ENTER)
        time.sleep(2)

        self.assertEqual(driver.find_element(by=By.XPATH, value="/html/body/center/form/div[2]/div/div").text,"Notebook Lenovo está muito caro!")
        driver.get("http://127.0.0.1:8000/logout/")
        time.sleep(3)

    def test_cenario14(self):
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
        self.assertEqual(driver.find_element(by=By.XPATH, value="/html/body/center/form/div[2]/div/div").text,"Notebook Lenovo está muito caro!")
        driver.get("http://127.0.0.1:8000/logout/")
        time.sleep(3)

    def test_cenario15(self):
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
        time.sleep(2)
        enviar.send_keys(Keys.ENTER)
        time.sleep(2)

        self.assertEqual(driver.find_element(by=By.XPATH, value="/html/body/center/form/div[1]/div/div").text,"Poucos produtos! Quero mais!")
        driver.get("http://127.0.0.1:8000/logout/")
        time.sleep(3)

class AdicionarComentarios(LiveServerTestCase):
    def test_cenario17(self):

        driver.get("http://127.0.0.1:8000/register/")
        usuario = driver.find_element(by=By.NAME, value="username")
        nome = driver.find_element(by=By.NAME, value="first_name")
        sobrenome = driver.find_element(by=By.NAME, value="last_name")
        email = driver.find_element(by=By.NAME, value="email")
        senha = driver.find_element(by=By.NAME, value="password1")
        confirmar_senha = driver.find_element(by=By.NAME, value="password2")
        botao = driver.find_element(by=By.NAME, value="registro")
        time.sleep(2)

        usuario.send_keys(f"Caminha_21032006")
        nome.send_keys(f"Teteu")
        sobrenome.send_keys(f"Brazao")
        email.send_keys(f"gustavson@cesar.school")
        senha.send_keys("Suadao1234")
        confirmar_senha.send_keys("Suadao1234")
        botao.send_keys(Keys.ENTER)
        time.sleep(2)

        driver.get("http://127.0.0.1:8000/")
        botao2 = driver.find_element(by=By.XPATH, value="/html/body/section/div/div/div/div/div[2]/div/a")
        botao2.send_keys(Keys.ENTER)
        time.sleep(2)

        comentario = driver.find_element(by=By.NAME, value="texto")
        comentario.send_keys(f"Esse iphone é muito bonito, gostei!")
        time.sleep(2)
        enviarcomentario = driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/div/form/button")
        enviarcomentario.send_keys(Keys.ENTER)
        time.sleep(5)
        self.assertEqual(driver.find_element(by=By.XPATH, value="/html/body/div/div[3]/div/div[1]/div/p[1]").text,"Esse iphone é muito bonito, gostei!")
        driver.get("http://127.0.0.1:8000/logout/")
        time.sleep(3)

    def test_cenario18(self):
        driver.get("http://127.0.0.1:8000/register/")
        usuario = driver.find_element(by=By.NAME, value="username")
        nome = driver.find_element(by=By.NAME, value="first_name")
        sobrenome = driver.find_element(by=By.NAME, value="last_name")
        email = driver.find_element(by=By.NAME, value="email")
        senha = driver.find_element(by=By.NAME, value="password1")
        confirmar_senha = driver.find_element(by=By.NAME, value="password2")
        botao = driver.find_element(by=By.NAME, value="registro")
        time.sleep(2)

        usuario.send_keys(f"Jose_Braz1987")
        nome.send_keys(f"Felipe")
        sobrenome.send_keys(f"Caminha")
        email.send_keys(f"becker@cesar.school")
        senha.send_keys("Suadao1234")
        confirmar_senha.send_keys("Suadao1234")
        botao.send_keys(Keys.ENTER)
        time.sleep(2)

        driver.get("http://127.0.0.1:8000/")
        botao2 = driver.find_element(by=By.XPATH, value="/html/body/section/div/div/div/div/div[2]/div/a")
        botao2.send_keys(Keys.ENTER)
        time.sleep(2)

        comentario = driver.find_element(by=By.NAME, value="texto")
        comentario.send_keys(f"Esse iphone esta muito caro, Que assalto!")
        time.sleep(2)
        enviarcomentario = driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/div/form/button")
        enviarcomentario.send_keys(Keys.ENTER)
        time.sleep(5)
        self.assertEqual(driver.find_element(by=By.XPATH, value="/html/body/div/div[3]/div/div[2]/div/p[1]").text,"Esse iphone esta muito caro, Que assalto!")
        driver.get("http://127.0.0.1:8000/logout/")
        time.sleep(3)
    
    def test_cenario19(self):
        driver.get("http://127.0.0.1:8000/login/")
        usuario = driver.find_element(by=By.NAME, value="username")
        senha = driver.find_element(by=By.NAME, value="password")
        time.sleep(2)

        usuario.send_keys(f"Jose_Braz1987")
        senha.send_keys("Suadao1234")
        botao = driver.find_element(by=By.NAME, value="login")
        botao.send_keys(Keys.ENTER)
        time.sleep(1)

        driver.get("http://127.0.0.1:8000/")
        botao2 = driver.find_element(by=By.XPATH, value="/html/body/section/div/div/div[2]/div/div[2]/div/a")
        botao2.send_keys(Keys.ENTER)
        time.sleep(2)
        comentario = driver.find_element(by=By.NAME, value="texto")
        comentario.send_keys(f"Esse Lenovo esta muito caro, Que assalto!")
        time.sleep(2)
        enviarcomentario = driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/div/form/button")
        enviarcomentario.send_keys(Keys.ENTER)
        time.sleep(4)
        self.assertEqual(driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[3]/div/div/div/p[1]").text,"Esse Lenovo esta muito caro, Que assalto!")
        driver.get("http://127.0.0.1:8000/logout/")
        time.sleep(3)

    def test_cenario20(self):
        botao2 = driver.find_element(by=By.XPATH, value="/html/body/section/div/div/div[2]/div/div[2]/div/a")
        botao2.send_keys(Keys.ENTER)
        self.assertEqual(driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/div/p").text,"Para adicionar um comentário, você precisa estar logado/registrado.")
        time.sleep(4)

class AdicionarAosFavoritos(LiveServerTestCase):
    def test_cenario21(self):
        driver.get("http://127.0.0.1:8000/register/")
        usuario = driver.find_element(by=By.NAME, value="username")
        nome = driver.find_element(by=By.NAME, value="first_name")
        sobrenome = driver.find_element(by=By.NAME, value="last_name")
        email = driver.find_element(by=By.NAME, value="email")
        senha = driver.find_element(by=By.NAME, value="password1")
        confirmar_senha = driver.find_element(by=By.NAME, value="password2")
        botao = driver.find_element(by=By.NAME, value="registro")
        time.sleep(2)

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
        time.sleep(3)
        self.assertEqual(driver.find_element(by=By.XPATH, value="/html/body/div/div/div[1]/div/div/center[1]/h5").text,"iPhone 13")
        self.assertEqual(driver.find_element(by=By.XPATH, value="/html/body/div/div/div[2]/div/div/center[1]/h5").text,"Notebook Lenovo")
        driver.get("http://127.0.0.1:8000/logout/")
        time.sleep(3)

    def test_cenario22(self):
        driver.get("http://127.0.0.1:8000/")
        botao2 = driver.find_element(by=By.XPATH, value="/html/body/section/div/div/div[1]/div/div[2]/div/a")
        botao2.send_keys(Keys.ENTER)
        time.sleep(2)
        self.assertEqual(driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div/div[2]/div/center/h5[2]").text,"Para adicionar um produto ao carrinho ou aos favoritos, você precisa estar logado/registrado.")
        
class RemoverDosFavoritos(LiveServerTestCase):
    def test_cenario23(self):
        driver.get("http://127.0.0.1:8000/register/")
        usuario = driver.find_element(by=By.NAME, value="username")
        nome = driver.find_element(by=By.NAME, value="first_name")
        sobrenome = driver.find_element(by=By.NAME, value="last_name")
        email = driver.find_element(by=By.NAME, value="email")
        senha = driver.find_element(by=By.NAME, value="password1")
        confirmar_senha = driver.find_element(by=By.NAME, value="password2")
        botao = driver.find_element(by=By.NAME, value="registro")
        time.sleep(2)

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

        driver.get("http://127.0.0.1:8000/")
        botao3= driver.find_element(by=By.XPATH, value="/html/body/section/div/div/div[2]/div/div[2]/div/a")
        botao3.send_keys(Keys.ENTER)
        time.sleep(2)

        favoritos2 = driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div/div[2]/div/center/button[2]")
        favoritos2.send_keys(Keys.ENTER)
        time.sleep(2)
        driver.get("http://127.0.0.1:8000/favoritos")
        time.sleep(2)

        remover2 =driver.find_element(by=By.XPATH,value="/html/body/div/div/div[2]/div/div/center[3]/button")
        remover2.send_keys(Keys.ENTER)
        time.sleep(1)

        remover1 =driver.find_element(by=By.XPATH,value="/html/body/div/div/div[1]/div/div/center[3]/button")
        remover1.send_keys(Keys.ENTER)
        time.sleep(1)

        self.assertEqual(driver.find_element(by=By.XPATH, value="/html/body/div[2]/h5").text,"Não existem produtos nos seus favoritos.")
        driver.get("http://127.0.0.1:8000/logout/")
        time.sleep(2)

    def test_cenario24(self):
        driver.get("http://127.0.0.1:8000/favoritos")
        time.sleep(2)
        self.assertEqual(driver.find_element(by=By.XPATH, value="/html/body/div/div/h5").text,"Para gerenciar/ver seus produtos favoritos, você precisa estar logado/registrado.")


        












        