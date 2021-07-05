'''

from paramiko import SSHClient, AutoAddPolicy
from rich import print, pretty, inspect
pretty.install()

client = SSHClient()
client.set_missing_host_key_policy(AutoAddPolicy())
client.load_system_host_keys()
client.connect('127.0.0.1', username = 'ydrea')
inspect(client, methods = True)
stdin, stdout, stderr = client.exec_command('ps aux')


def execute():
    try:
        client = SSHClient()
        client.set_missing_host_key_policy(AutoAddPolicy())
        client.load_system_host_keys()
        client.connect(hostname = '127.0.0.1:5000', username = 'ydrea', password = 'lorien')
        inspect(client, methods = True)
        stdin, stdout, stderr = client.exec_command('ps aux')
    except Exception as err:
        print(str(err))
'''