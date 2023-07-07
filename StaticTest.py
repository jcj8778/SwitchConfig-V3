from Switch import Switch


class StaticTest(Switch):

    def __init__(self, name, ports, description, vlan_ID):
        super().__init__(name, ports, description, vlan_ID)

    def CommandOutput(self, command):
        output = self.ssh.send_command(command)
        return output


