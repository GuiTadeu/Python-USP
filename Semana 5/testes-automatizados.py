# Bugs: Sintaxe ou Lógica
# Bugs causam catastrofes
# Bugs causam desconforto

''' Como Testar?
Testes Manuais:
- Cansativo
- Testar apenas alguns casos
- Apenas algumas vezes

Testes automatizados:
- Bateria de testes que cobre o maximo possivel do seu código
- Executada rotineirameente várias vezes ao dia

PYTEST
ARCABOUÇOS DE TESTES AUTOMATIZADOS

Veja como instalar em docs.pytest.org

Considera que arquivos do tipo test_*.py e *_test.py são arquivos de teste
Executa funções e métodos do tipo test_*
Considera classes do tipo Test*

EM SUMA

Pense cuidadosamente nos casos em que seu programa ppode falhar
Pense nos diferentes tipos de entrada que exercitam caminhos diferentes no seu programa
Pense nos casos diferentes do seu código
Escreva testes automatizados para todos esses casos

'''

def fatorial(n):
    i = fat = 1
    while i <= n:
        fat = fat * i
        i = i + 1
    return fat

def test_fatorial0():
    assert fatorial(0) == 1

def test_fatorial5():
    assert fatorial(5) == 5