import tftpy

def tftp_run():
	server = tftpy.TftpServer('tftp')
	server.listen('192.168.122.1', 69)

