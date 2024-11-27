# Openvalores

# Scraper de Preços Simples #RPA # BOT #PYTHON #WEBSCRAPPER

# Scraper de Preços Simples

Este projeto é um scraper de preços simples, usando Selenium e Python.  Ele extrai informações de preços de produtos de um site específico (Google).

**Recursos:**

* Extração de preços, nomes de produtos e links.
* Suporte a múltiplas páginas de resultados.
* Tratamento de erros robusto (com logs).
* Uso de `WebDriverWait` para espera eficiente.
* Uso de XPath para seletores mais robustos.


**Limitacões:**

* **Fragilidade:**  O código pode quebrar se o site alterar sua estrutura HTML.
* **Escopo limitado:**  Atualmente, só funciona para um site específico.


**Instruções de Uso:**

1. **Instale as dependências:** `pip install selenium`
2. **Baixe o ChromeDriver:**  Certifique-se que a versão do ChromeDriver seja compatível com a sua versão do Chrome.  Coloque o `chromedriver.exe` (ou `chromedriver`) na mesma pasta do script Python.
3. **Execute o script:** `python main.py`
4. **Insira o termo de pesquisa:** O programa solicitará o termo a ser pesquisado.

**Contribuições:**

Contribuições são bem-vindas!  Abra um Issue para relatar bugs ou sugerir novas funcionalidades.

**Licença:**

[MIT License](LICENSE)
