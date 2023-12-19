import socket
import nmap

# print(socket.gethostbyname("www.mesanjib.wordpress.com"))
# print(socket.gethostbyname("www.sanjib.pythonanywhere.com"))

nmap_path = [r"C:\Program Files (x86)\Nmap\nmap.exe",]
scanner = nmap.PortScanner(nmap_search_path=nmap_path)
print(scanner.nmap_version())
scanner.scan('192.168.146.1', '22-455', '-v')
print(scanner.scaninfo())
print(scanner.csv())
print(scanner.scanstats())
print(scanner['192.168.146.1'].state())
print(scanner['192.168.146.1'].all_protocols())
print(scanner['192.168.146.1']['tcp'].keys())