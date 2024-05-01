from django.test import LiveServerTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium import webdriver
import time

driver = webdriver.Chrome()

class AtualizarPerfil(LiveServerTestCase):

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

        self.assertEqual(driver.find_element(by=By.NAME, value="title").text,"iTech Store")
        driver.get("http://127.0.0.1:8000/logout/")
        time.sleep(5)

    def test_cenario2(self):
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
        numero.send_keys("8199999990")
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

        self.assertEqual(driver.find_element(by=By.NAME, value="title").text,"iTech Store")
        driver.get("http://127.0.0.1:8000/logout/")
        time.sleep(4)

class PesquisarProduto(LiveServerTestCase):

    def test_cenario3(self):
        driver.get("http://127.0.0.1:8000/search/")
        pesquisa = driver.find_element(by=By.NAME, value="searched")
        botao = driver.find_element(by=By.NAME, value="go")

        pesquisa.send_keys("iPhone")
        time.sleep(2)
        botao.send_keys(Keys.ENTER)
        self.assertEqual(driver.find_element(by=By.NAME, value="prodname").text,"iPhone 13")
        time.sleep(2)

    def test_cenario4(self):
        driver.get("http://127.0.0.1:8000/search/")
        pesquisa = driver.find_element(by=By.NAME, value="searched")
        botao = driver.find_element(by=By.NAME, value="go")

        pesquisa.send_keys("8gb")
        time.sleep(2)
        botao.send_keys(Keys.ENTER)
        self.assertEqual(driver.find_element(by=By.NAME, value="prodname").text,"iPhone 13")
        time.sleep(2)

    def test_cenario5(self):
        driver.get("http://127.0.0.1:8000/search/")
        pesquisa = driver.find_element(by=By.NAME, value="searched")
        botao = driver.find_element(by=By.NAME, value="go")

        pesquisa.send_keys("Fechadura eletrônica")
        time.sleep(2)
        botao.send_keys(Keys.ENTER)
        self.assertEqual(driver.find_element(by=By.NAME, value="title").text,"Procurar Produtos")
        time.sleep(2)

class AdicionarNoCarrinho(LiveServerTestCase):

    def test_cenario6(self):
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
        botao2 = driver.find_element(by=By.XPATH, value="/html/body/section/div/div/div[2]/div/div[2]/div/a")
        botao2.send_keys(Keys.ENTER)
        time.sleep(2)
        botaoadd = driver.find_element(by=By.ID, value="add-cart")
        botaoadd.send_keys(Keys.ENTER)
        time.sleep(2)
        botaocart = driver.find_element(by=By.NAME, value="carrinho")
        botaocart.send_keys(Keys.ENTER)
        time.sleep(2)

        self.assertEqual(driver.find_element(by=By.ID, value="total").text,"Total: R$2400.00")
        driver.get("http://127.0.0.1:8000/logout/")
        time.sleep(2)
        driver.get("http://127.0.0.1:8000/cart/")
        time.sleep(3)

    def test_cenario7(self):
        driver.get("http://127.0.0.1:8000/login/")
        usuario = driver.find_element(by=By.NAME, value="username")
        senha = driver.find_element(by=By.NAME, value="password")
        botao = driver.find_element(by=By.NAME, value="login")

        usuario.send_keys("User_3")
        senha.send_keys("Senha1234")
        botao.send_keys(Keys.ENTER)
        time.sleep(2)

        driver.get("http://127.0.0.1:8000/")
        botao2 = driver.find_element(by=By.XPATH, value="/html/body/section/div/div/div[1]/div/div[2]/div/a")
        botao2.send_keys(Keys.ENTER)
        time.sleep(2)
        botaoadd = driver.find_element(by=By.ID, value="add-cart")
        botaoadd.send_keys(Keys.ENTER)
        time.sleep(2)
        botaocart = driver.find_element(by=By.NAME, value="carrinho")
        botaocart.send_keys(Keys.ENTER)
        time.sleep(2)

        self.assertEqual(driver.find_element(by=By.ID, value="total").text,"Total: R$5600.00")
        driver.get("http://127.0.0.1:8000/logout/")
        time.sleep(3)

    def test_cenario8(self):
        driver.get("http://127.0.0.1:8000/")
        time.sleep(2)
        botao2 = driver.find_element(by=By.XPATH, value="/html/body/section/div/div/div[3]/div/div[2]/div/a")
        botao2.send_keys(Keys.ENTER)
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

        self.assertEqual(driver.find_element(by=By.ID, value="total").text,"Total: R$16000.00")
        driver.get("http://127.0.0.1:8000/logout/")
        time.sleep(3)

    def test_cenario10(self):
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
        
        self.assertEqual(driver.find_element(by=By.ID, value="total").text,"Total: R$12000.00")
        driver.get("http://127.0.0.1:8000/logout/")
        time.sleep(3)

class ProcurarPorCategoria(LiveServerTestCase):

    def test_cenario11(self):
        driver.get("http://127.0.0.1:8000/")
        time.sleep(2)
        botao = driver.find_element(by=By.XPATH, value="/html/body/nav/div/div/ul/li[6]/a")
        botao.send_keys(Keys.ENTER)
        time.sleep(2)
        botao2 = driver.find_element(by=By.NAME, value="notebooks")
        botao2.send_keys(Keys.ENTER)
        self.assertEqual(driver.find_element(by=By.NAME, value="title").text,"Notebooks")
        time.sleep(3)