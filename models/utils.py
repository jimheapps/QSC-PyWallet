import socket

from pyqrllib.pyqrllib import str2bin, hstr2bin, bin2hstr



###############################################################################
CONNECTION_TIMEOUT = 50


###############################################################################
def check_connection(ip_address, port):
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Set a timeout for the connection attempt
        sock.settimeout(5)  # Set timeout to 5 seconds
        
        # Attempt to connect to the IP address and port
        sock.connect((ip_address, port))
        
        # If the connection is successful, return True
        return True
    except socket.error as e:
        # If connection fails, return False
        return False
    finally:
        sock.close()


def read_ip_port_list_from_file(file_path):
    ip_port_list = []
    with open(file_path, 'r') as file:
        for line in file:
            ip_port = line.strip()  # Remove leading/trailing whitespaces and newline characters
            ip_port_list.append(ip_port)
    return ip_port_list

def get_qaddress(addr_byte):
    return "q" + bin2hstr(bytes(addr_byte))

def get_node_IP(network):
    nodes = read_ip_port_list_from_file('./data/nodes.txt')
    ip, port = None, None
    for node in nodes:
        ip = node.split(':')[0]
        port = int(node.split(':')[1])
        state = check_connection(ip, port)
        print(f'-> node= {ip}:{port}, state= {state}')
        if state:
            break

    if ip is None or port is None:
        raise Exception("Sorry, no QSC node is available!")

    return f'{ip}:{port}' 