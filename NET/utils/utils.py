import pexpect
import getpass
import sys



class BU():
    
        
    def copy(self):
        
        
        
        con_type.expect('[#>]')
        con_type.sendline('enable')
        con_type.expect('Password:')
        con_type.sendline(EN_PASS)
        con_type.expect('#')
        con_type.sendline('copy running-config tftp:')
        con_type.expect('Address or name of remote host \[]\?')
        con_type.sendline(SERVER_IP)
        con_type.expect('Destination filename [pr1-confg]?')
        con_type.sendline('{}'.format(IP))
        con_type.expect('#')
        con_type.sendline('copy start run')
        print(con_type.before.decode('utf-8'))





    def restore_config(self,CONNECTION_TYPE, USER, PASSWORD, SERVER_IP, DEVICES_IP):
            
        USER = 'usman'
        PASSWORD = 'cisco'
        SERVER_IP= '192.168.216.1'
        DEVICES_IP = [('192.168.206.1','cisco')]
        for IP,EN_PASS in DEVICES_IP:
            #print('Connection to device {}'.format(IP))
            if CONNECTION_TYPE == 'ssh':
                with pexpect.spawn('ssh {}@{}'.format(USER, IP)) as con_type:
                    con_type.expect('Password:')
                    con_type.sendline(PASSWORD)
                    self.copy(con_type) 
            if CONNECTION_TYPE == 'telnet':
                with pexpect.spawn('telnet {}'.format(IP)) as con_type:
                    self.copy(con_type)

                
class SnmpSet():
    

    def setting_snmp(self, con_type):

        con_type.expect('[#>]')
        con_type.sendline('enable')
        con_type.expect('Password:')
        con_type.sendline(EN_PASS)
        con_type.expect('#')
        con_type.sendline('snmp-server community public RO')
        con_type.sendline('snmp-server host')
    


    def set_trap(self,CONNECTION_TYPE, USER, PASSWORD, DEVICES_IP):
        DEVICES_IP = [('192.168.206.1','cisco')]
        for IP,EN_PASS in DEVICES_IP:
            #print('Connection to device {}'.format(IP))
            if CONNECTION_TYPE == 'ssh':
                with pexpect.spawn('ssh {}@{}'.format(USER, IP)) as con_type:
                    con_type.expect('Password:')
                    con_type.sendline(PASSWORD)
                    self.setting_snmp(con_type) 
            if CONNECTION_TYPE == 'telnet':
                with pexpect.spawn('telnet {}'.format(IP)) as con_type:
                    self.setting_snmp(con_type)





        

        