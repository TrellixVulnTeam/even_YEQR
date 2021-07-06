
'''

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///baza.db'
# db = SQLAlchemy(app)

# class PsAuxModel(db.Model):
#     id = db.Column(db.Integer, primary_key=True)    
#     ip = db.Column(db.Integer, nullable=False)    
#     uname = db.Column(db.String(120), nullable=False)    
#     pwd = db.Column(db.String(120), nullable=False)    
#     pid = db.Column(db.Integer, nullable=False)    
#     command = db.Column(db.String(120), nullable=False)    
#     cpu = db.Column(db.Integer, nullable=False) 
    
#     def __repr__(self):
#         return f"Baza(ipA={ip}, unameA={uname}, pwd={pwd}, pidA={pid}, commandA={commmand}, cpuA={cpu} )"

# db.create_all()

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