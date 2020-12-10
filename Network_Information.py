import socket
from typing import NewType
from tabulate import tabulate

"""Python small script that gives network information """
class Network_Information(object):
    def __init__(self,url = 'www.google.com') -> str:
        super().__init__()
        self.url = url
        self.host_name = socket.gethostname()
        self.ip_address = socket.gethostbyname(self.host_name)
        self.remote_ip = self.remote_info() # function that gives remote ip info
    
    def __repr__(self) -> str:
        #return super().__repr__()
        data = {"Host Name:": [self.host_name],
                "IP Address:": [self.ip_address],
                f"{self.url}": [self.remote_ip],
                }
        table = tabulate(data, headers="keys", tablefmt="grid")
        return table
    def remote_info(self):
        try:
            return socket.gethostbyname(self.url)
        except socket.error as err_msg:
            return err_msg
if __name__ == "__main__":
    domain = input("Type url to get Network Information(Ex:- google.com ) or Press Enter to RUN Default:")
    if len(domain) == 0:
        print(Network_Information())
    else:
        print(len(domain))
        print(Network_Information(url=domain))