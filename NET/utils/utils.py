import pexpect
from pexpect import pxssh
from netmiko import ConnectHandler
import getpass
import sys

class Configure():
    
    def __init__(self, TYPE, CONNECTION_TYPE, USER, PASSWORD, SERVER_IP, DEVICES_IP, EN_PASS, CONF_NAME): 
        print(TYPE, CONNECTION_TYPE, USER, PASSWORD, SERVER_IP, DEVICES_IP, EN_PASS, CONF_NAME)           
        device = {
                                'ip': DEVICES_IP, # адрес устройства
                                'username': USER, # имя пользователя
                                'password': PASSWORD, # пароль пользователя
                                'secret': EN_PASS, # пароль режима enable
                                }
                                

        if TYPE == 'Save':
            if CONNECTION_TYPE == 'ssh':
                try:
                    device['device_type'] = 'cisco_ios'
                    print(device)
                    connection = ConnectHandler(**device)
                    self.save_configuration(connection, SERVER_IP,CONF_NAME)
                except pxssh.ExceptionPxssh as e:
                    pass
                    # print("pxssh failed on login.")
                    # print(e)  
            if CONNECTION_TYPE == 'telnet':
                try:
                    device['device_type'] = 'cisco_ios_telnet'
                    print(device)
                    connection = ConnectHandler(**device)
                    self.save_configuration(connection, SERVER_IP,CONF_NAME)
                except Exception as e:
                    print(e)
    

        if TYPE == 'Set':
            if CONNECTION_TYPE == 'ssh':
                try:
                    device['device_type'] = 'cisco_ios'
                    connection = ConnectHandler(**device)
                    self.set_configuration(connection, SERVER_IP,CONF_NAME)
                except pxssh.ExceptionPxssh as e:
                    print("pxssh failed on login.")
                    print(e)  
            if CONNECTION_TYPE == 'telnet':
                try:
                    device['device_type'] = 'cisco_ios_telnet'
                    print(device)
                    connection = ConnectHandler(**device)
                    self.set_configuration(connection, SERVER_IP,CONF_NAME)
                except Exception as e:
                    print(e)
    


    def save_configuration(self, connection, SERVER_IP,CONF_NAME ):
        connection.enable()
        result = connection.send_command_timing('copy running-config tftp:\n'+SERVER_IP+'\n'+CONF_NAME+'\n')
        print(result) 
        
       
        

    def set_configuration(self, connection, SERVER_IP, CONF_NAME):
        connection.enable()
        result = connection.send_command_timing('copy tftp: running-config\n'+'192.168.122.1'+'\n'+'123'+'\n'+'running-config'+'\n') 
        print(result)

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

class NetFlow():
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

        
        
class Os(object):
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
                       