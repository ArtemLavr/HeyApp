import pexpect
from pexpect import pxssh
import getpass
import sys

class Configure():
    
    def __init__(self, TYPE, CONNECTION_TYPE, USER, PASSWORD, SERVER_IP, DEVICES_IP, EN_PASS, CONF_NAME):            
                
        if TYPE == 'Save':
            if CONNECTION_TYPE == 'ssh':
                try:
                    s = pxssh.pxssh()
                    s.login(DEVICES_IP, USER, PASSWORD)
                    self.save_configuration(s, EN_PASS, SERVER_IP, CONF_NAME)
                except pxssh.ExceptionPxssh as e:
                    print("pxssh failed on login.")
                    print(e)  
            if CONNECTION_TYPE == 'telnet':
                try:
                    with pexpect.spawn('telnet {}'.format(DEVICES_IP)) as s:
                        s.expect('Password:')
                        s.sendline(PASSWORD)
                        self.save_configuration(s, EN_PASS, SERVER_IP,CONF_NAME)
                except Exception as e:
                    print(e)
    

        if TYPE == 'SET':
            if CONNECTION_TYPE == 'ssh':
                try:
                    s = pxssh.pxssh()
                    s.login(DEVICES_IP, USER, PASSWORD)
                    self.set_configuration(EN_PASS, SERVER_IP, CONF_NAME)
                except pxssh.ExceptionPxssh as e:
                    print("pxssh failed on login.")
                    print(e)  
            if CONNECTION_TYPE == 'telnet':
                try:
                    with pexpect.spawn('telnet {}'.format(DEVICES_IP)) as s:
                        s.expect('Password:')
                        s.sendline(PASSWORD)
                        self.set_configuration(s, EN_PASS, SERVER_IP, CONF_NAME)
                except Exception as e:
                    print(e)
    


    def save_configuration(self, s, EN_PASS, SERVER_IP,CONF_NAME ):
        s.sendline('enable')
        s.sendline('copy running-config tftp:')
        s.sendline(SERVER_IP)
        s.sendline(CONF_NAME)
        
       
        

    def set_configuration(self, s, EN_PASS, SERVER_IP, CONF_NAME):
        s.sendline('enable')
        s.sendline(EN_PASS)
        s.sendline('copy tftp: running-config')
        s.sendline(SERVER_IP)
        s.sendline(CONF_NAME)
        s.sendline('running-config')
        s.sendline('copy start run')


class SnmpSet():
    def __init__(self, CONNECTION_TYPE, USER_NAME, PASSWORD, DEVICES_IP, EN_PASS, SNMP_SERVER):
        
        if CONNECTION_TYPE == 'ssh':
            try:
                with pexpect.spawn('ssh {}@{}'.format(USER_NAME, DEVICES_IP)) as con_type:
                    con_type.expect('Password:')
                    con_type.sendline(PASSWORD)
                    self.setting_snmp(con_type)
            except Exception as e:
                print(e)
        if CONNECTION_TYPE == 'telnet':
            try:
                with pexpect.spawn('telnet {}'.format(DEVICES_IP)) as con_type:
                    con_type.expect('Password:')
                    con_type.sendline(PASSWORD)
                    self.setting_snmp(con_type, EN_PASS, SNMP_SERVER)
            except Exception as e:
                print(e)

    def setting_snmp(self, con_type, EN_PASS, SNMP_SERVER):
        con_type.expect('[#>]')
        con_type.sendline('enable')
        con_type.expect('Password:')
        con_type.sendline(EN_PASS)
        con_type.expect('#')
        con_type.sendline('conf t')
        con_type.expect('#')
        con_type.sendline('snmp-server community public RO')
        con_type.expect('#')
        con_type.sendline('snmp-server enable traps')
        con_type.expect('#')
        con_type.sendline('snmp-server host {} public'.format(SNMP_SERVER))

class Pass(object):
    """docstring for """
    def __init__(self, arg):
        super(Pass, self).__init__()
        self.arg = arg
        
        
class Os(object):
    """docstring for Os"""
    def __init__(self, arg):
        super(Os, self).__init__()
        self.arg = arg
                       