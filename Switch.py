import openpyxl
import netmiko
from netmiko import ConnectHandler
from tabulate import tabulate


class Switch:
    def __init__(self, name, ports, description, vlan_ID):
        self.ssh = None
        self.name = name
        self.ports = ports
        self.description = description
        self.vlan_Id = vlan_ID

    def get_name(self):
        return self.name

    def get_port(self):
        return self.port

    # Setter methods
    def set_name(self, name):
        self.name = name

    def set_port(self, port):
        self.port = port

    def __str__(self):
        table = [
            [self.name, self.port]
        ]
        return tabulate(table, tablefmt="grid")

    def connect(self, ip):
        device = {
            'device type': 'cisco_ios',
            'ip': ip,
            'username': 'admin',
            'password': 'switch',
        }
        self.ssh = ConnectHandler(**device)

    def disconnect(self):
        if self.ssh is not None:
            self.ssh.disconnect()
            self.ssh = None


