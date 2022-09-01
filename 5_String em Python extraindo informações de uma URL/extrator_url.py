"""Salva a url num atributo do objeto (self.url = url) e verifica se a url é válida"""


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


url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
extrator_url = ExtratorURL(url)
valor_quantidade = extrator_url.get_valor_parametro("quantidade")
print(valor_quantidade)
