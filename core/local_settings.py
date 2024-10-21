# type: ignore
# flake8: noqa

# Comando:
# python -c "import string as s;from secrets import SystemRandom as SR;print(''.join(SR().choices(s.ascii_letters + s.digits + s.punctuation, k=64)));"
SECRET_KEY = '1z2jrMODK#2UL}x7|_JNJdrDs`N[PD}(OWxbb1/I<H>(ai#!]Gimwyg(3YM6]CG'

# DEBUG DEVE SER False em produção
DEBUG = False

# Seu domínio ou IP devem vir aqui
ALLOWED_HOSTS = ['34.45.100.29', 'mappacfopm.com.br', 'www.mappacfopm.com.br', '127.0.0.1', 'localhost']

# Config para postgresql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'anotacao_cfo',
        'USER': 'usuario_mappa',
        'PASSWORD': 'senha_database',
        'HOST': '127.0.0.1',
        'PORT': '5433',
    }
}
