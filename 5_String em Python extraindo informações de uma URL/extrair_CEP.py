endereco = input('Digite o endereço com CEP: ')

import re

padrao = re.compile('[0-9]{5}-?'
                    '[0-9]{3}')

busca = padrao.search(endereco)
if busca:
    cep = busca.group()
    print(f'O CEP é: {cep}')
else:
    print('Endereço digitado não contém CEP')

