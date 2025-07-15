import os
import netmiko

# from dotenv import load_dotenv
# load_dotenv()
#
# Pass = os.getenv('PASS')
# print(Pass)


def test():
    from netmiko import ConnectHandler

    mikrotik_router_021 = {
    'device_type': 'mikrotik_routeros',
    'host': '164.132.182.20',
    'port': '22',
    'username': 'admin+ct',
    'password': 'admin'
    }

    sshCli = ConnectHandler(**mikrotik_router_021)
    print(sshCli.find_prompt())

    # output = sshCli.send_command("/interface ethernet print")
    # print(output)

    # command = "/export"
    # output = sshCli.send_command(command)
    # print(output)

    # file = open("BackUp-Config-Mikrotik-Netmiko.txt", "w")
    # file.write(output)
    # file.close()

    sshCli.disconnect()

# test()

# if __name__ == "__main__":
#     test()


