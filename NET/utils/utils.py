import pexpect
import getpass
import sys

class BU():
    
        
    def copy():
        ssh.expect('Password:')
        ssh.sendline(PASSWORD)
        
        
        ssh.expect('[#>]')
        ssh.sendline('enable')
        ssh.expect('Password:')
        ssh.sendline(EN_PASS)
        ssh.expect('#')
        ssh.sendline('copy running-config tftp:')
        ssh.expect('Address or name of remote host \[]\?')
        ssh.sendline(SERVER_IP)
        ssh.expect('Destination filename [pr1-confg]?')
        ssh.sendline('{}'.format(IP))
        ssh.expect('#')
        ssh.sendline('copy start run')
        print(ssh.before.decode('utf-8'))

    def restore_config(CONNECTION_TYPE, USER, PASSWORD, SERVER_IP, DEVICES_IP):
            
        USER = 'usman'
        PASSWORD = 'cisco'
        SERVER_IP= '192.168.216.1'
        DEVICES_IP = [('192.168.206.1','cisco')]
        for IP,EN_PASS in DEVICES_IP:
            #print('Connection to device {}'.format(IP))
            with pexpect.spawn('ssh {}@{}'.format(USER, IP)) as ssh:
                copy()    
                