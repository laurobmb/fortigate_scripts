import paramiko

class SSH:

    def __init__(self,IP,USER,PASSWORD):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(hostname=IP,username=USER,password=PASSWORD)

    def comando_ssh(self,cmd):
        stdin,stdout,stderr = self.ssh.exec_command(cmd)
        if stderr.channel.recv_exit_status() != 0:
            out = stderr.readlines()
        else:
            out = stdout.readlines()
        return out

def get_info(IP,USER,PASSWORD,COMANDO):
    conexao = SSH(IP,USER,PASSWORD)
    out = conexao.comando_ssh(COMANDO)
    out = list(map(lambda x:x.strip(),out)) #remove \n da lista
    return out

def get_firewall(IP,USER,PASSWORD,COMANDO):
    conexao = SSH(IP,USER,PASSWORD)
    out = conexao.comando_ssh(COMANDO)
    out = list(map(lambda x:x.strip(),out)) #remove \n da lista
    return out

def main():
    ip = '10.1.1.0'
    username = 'fortionly'
    password = 'senha'
    conexao = SSH(ip,username,password)
    
    out = get_info(ip,username,password,'get system status')
    cont=0
    while cont < 28:
        print(out[cont])
        cont=cont+1

    out = get_firewall(ip,username,password,'config vdom \n edit BGP-AS \n get system performance firewall statistics')
    cont=0
    while cont < 21:
        print(out[cont])
        cont=cont+1

if __name__ == '__main__':
    main()
