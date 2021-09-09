import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from faker import Faker
from validate_docbr import CPF
import random
from clientes.models import Cliente

def criando_pessoas(quantidade_de_pessoas):
    try:
        fake = Faker('pt_BR')
        Faker.seed(10)
        for _ in range(quantidade_de_pessoas):
            cpf = CPF()
            nome = fake.name()
            email = '{}@{}'.format(nome.lower(),fake.free_email_domain())
            email = email.replace(' ', '')
            cpf = cpf.generate()
            rg = "{}{}{}{}".format(random.randrange(10, 99),random.randrange(100, 999),random.randrange(100, 999),random.randrange(0, 9) ) 
            celular = "{} 9{}-{}".format(random.randrange(10, 21), random.randrange(4000, 9999), random.randrange(4000, 9999))
            ativo = random.choice([True, False])
            p = Cliente(nome=nome, email=email, cpf=cpf, rg=rg, celular=celular, ativo=ativo)
            p.save()
            print("\x1b[6;30;42m############################# Dados ###########################\x1b[0m\n")
            print(f'\033[32m Nome: {nome} Email: {email} CPF: {cpf} RG: {rg} Celular: {celular} Status: {ativo} \033[0m')
    except Exception as e:
        print(e)

criando_pessoas(3020000000)