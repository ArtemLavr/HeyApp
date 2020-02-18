import pexpect
import getpass
import sys

class Configure():
    
    def __init__(self,CONNECTION_TYPE, USER, PASSWORD, SERVER_IP, DEVICES_IP):            
        

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
                    self.copy_configuration(con_type, EN_PASS, SERVER_IP)
            except Exception as e:
                print(e)

    def copy_configuration(self):
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
        

    def restore_configuration():
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


        
        