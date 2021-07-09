
from paramiko import SSHClient, AutoAddPolicy

client = SSHClient()
client.set_missing_host_key_policy(AutoAddPolicy())
client.load_system_host_keys()
client.connect(hostname='127.0.0.1', username='xxxxxx', password='xxxxxx')
stdin, stdout, stderr = client.exec_command('ps -eo pid,pcpu,comm')
global psaux
psaux = f"{stdout.read().decode('utf8')}"
# print (psaux)
