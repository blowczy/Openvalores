from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
import time

# Configura o ChromeDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Execução em segundo plano, sem abrir janela do navegador
options.add_argument("--disable-dev-shm-usage")  # Evita problemas de uso de memória
options.add_argument("--no-sandbox")  # Execução em ambientes restritos
driver = webdriver.Chrome(options=options)

# Solicita o termo de pesquisa ao usuário
termo_pesquisa = input("Digite o termo de pesquisa: ")

# Realiza a pesquisa no Google e navega pelas páginas
for page_number in range(1, 11):  # Altere o valor máximo conforme necessário
    print(f"Acessando a página {page_number}...")

    # Constrói a URL da página
    google_url = f"https://www.google.com/search?q=Valores de '{termo_pesquisa}' em R$&start={((page_number - 1) * 10)}"
    driver.get(google_url)

    # Aguarda um pouco para carregar os resultados
    driver.implicitly_wait(10)

    # Encontra todos os resultados da pesquisa
    search_results = driver.find_elements("css selector", ".tF2Cxc")

    # Extrai e exibe os valores e nomes encontrados na página
    for result in search_results:
        nome = result.find_element("css selector", ".DKV0Md").text
        valores = re.findall(r'R\$\s?\d+(?:\.\d{3})*(?:,\d{2})?', result.text)

        # Encontra o link de referência
        link_element = result.find_element("css selector", "a")
        link = link_element.get_attribute("href")

        for valor in valores:
            print(f"Nome: {nome}\nValor: {valor}\nLink: {link}\n")

    # Avança para a próxima página (se houver)
    next_page_button = driver.find_elements("css selector", "a[aria-label='Próxima']")
    if next_page_button:
        next_page_button[0].click()
    else:
        print("Não há mais páginas de resultados.")
    print ("PRESSIONE PARA AVANÇAR PARA A PROXIMA PAGINA ")

    driver.implicitly_wait(10000)
    input("Pressione Enter para ir para a proxima pagina...") 





#DESENVOLVEDOR: BRUNO LOWCZY
#@1.0 VERSÃO 08 / 2023
