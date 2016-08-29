import os
from netmiko import ConnectHandler
import getpass

ssh_username = raw_input("Enter Username> ")
ssh_password = getpass.getpass("Enter Password> ")

torSwitch={
'device_type': 'cisco_ios',
'ip': '192.168.1.3',
'username': ssh_username,
'password': ssh_password,
}

coreSwitch={
'device_type': 'cisco_ios',
'ip': '192.168.1.2',
'username': ssh_username,
'password': ssh_password,
}

ASA={
'device_type': 'cisco_asa',
'ip': '192.168.1.1',
'username': ssh_username,
'password': ssh_password,
}


all_devices = [torSwitch,coreSwitch]

for a_device in all_devices:
 net_connect = ConnectHandler(**a_device) 
 command = 'show arp'                         
 output = net_connect.send_command(command)
 elem = net_connect.find_prompt()
 elem = elem.replace("#","")
 filename = os.path.join(os.path.dirname(os.path.realpath(elem)), "PRE_TEST_" + elem + '.txt')                            
 fileobj = open(filename,"ab")
 fileobj.write("\n\n>>>>>>>>>>>Device {0}<<<<<<<<<<<<".format(a_device['device_type']) + "\r\n")
 fileobj.write(output + "\r\n" )
 fileobj.write(">>>>>>>>END<<<<<<<<" + "\r\n")
 fileobj.close()
