import requests

BASE_URL = 'http://127.0.0.1:5000'
ENDPOINT = 'test'

def get_resource():
    # resp=requests.get(BASE_URL+ENDPOINT)  <<< Request url malformed
    resp = requests.get(BASE_URL+"/"+ENDPOINT)
    print(resp.status_code)
    print(resp.json())


get_resource()

# response = requests.put(BASE + '/cred')
# print(response.json())

# response = requests.get(BASE + '/alo')
# print(response.json())

# test localhost
# hostname = 'localhost'
# port = 22
# user = "ydrea"
# passw = "lorien"

# try:
# for server in servers:
# client = SSHClient()
#    client.load_host_keys()
#     client.set_missing_host_key_policy(AutoAddPolicy())
#     client.load_system_host_keys()
#     client.connect(hostname, username='ydrea', port=port, password=passw)
#     stdin, stdout, stderr = client.exec_command('ps aux')
#     print(stdout.read().decode())
# except Exception as err:
#     print(str(err))

# if stdout.channel.recv_exit_status() == 0:
#     print(f'STDOUT: {stdout.read().decode("utf8")}')
# else:
#     print(f'STDERR: {stderr.read().decode("utf8")}')

# stdin.close()
# stdout.close()
# stderr.close()
# client.close()
