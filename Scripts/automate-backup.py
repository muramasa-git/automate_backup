#!python
from netmiko import ConnectHandler
#import os

""" We can loop through a list of IP/Port from textfile. In this case, I am using
loop on Port because all device's IP Address are the same from local lab """

""" We can add more command based on our needs start on Line 31 """


with open('devices.txt') as routers:
    for port in routers: 
        CSR = {
            'device_type': 'cisco_ios_telnet',
            'ip': '192.168.144.128',
            'username': 'cisco',
            'password': 'cisco',
            'port': port 
        }
        
        net_connect = ConnectHandler(**CSR)

        hostname = net_connect.send_command('show run | i host')
        hostname_list = hostname.split(" ")
        device = hostname_list[len(hostname_list)-1]
        device = device.split("\n")[0]
        print ("Backing up " + device)
        
        filename = device + '.txt'

        showrun = net_connect.send_command('show run')
        showvlan = net_connect.send_command('show interface brief')
        showver = net_connect.send_command('show ver')
        log_file = open(filename, "a")
        log_file.write("show run\n\n")  
        log_file.write(showrun)
        log_file.write("\n")
        log_file.write("show interface brief\n\n") 
        log_file.write(showvlan)
        log_file.write("\n")
        log_file.write("show version\n\n") 
        log_file.write(showver)
        log_file.write("\n")
        
        net_connect.disconnect()