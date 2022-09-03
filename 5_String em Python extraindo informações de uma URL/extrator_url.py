"""Salva a url num atributo do objeto (self.url = url) e verifica se a url é válida"""
import re


class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    # """Retorna a url removendo espaços em branco."""
    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    # """Valida se a url está vazia"""
    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia")

        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(url)
        if not match:
            raise ValueError('A URL não é válida')

    # """Retorna a base da url."""
    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    # """Retorna os parâmetros da url."""
    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    # """Retorna o valor do parametro `parametro_busca`."""
    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url + '\n' + "Parâmetros: " + self.get_url_parametros() + '\n' + "URL Base: " + self.get_url_base()

    def __eq__(self, other):
        return self.url == other.url


url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
extrator_url = ExtratorURL(url)
extrator_url_2 = ExtratorURL(url)
print("O tamanho da URL é: ", len(extrator_url))
print("URL completa: ", extrator_url)
print("extrator_url == extrator_url_2? ", extrator_url == extrator_url_2)
valor_quantidade = extrator_url.get_valor_parametro("quantidade")
print("Valor do parâmetro 'quantidade': ", valor_quantidade)


