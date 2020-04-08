import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('10.1.1.0',username='admin',password='senha')
stdin, stdout, stderr = ssh.exec_command("get system status")
var = stdout.readlines()
var = list(map(lambda x:x.strip(),var)) #remove \n da lista 
cont=0
while cont < 28:
	print(var[cont])
	cont=cont+1
