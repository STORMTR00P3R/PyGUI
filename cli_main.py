import requests
import socket

def get_city():  
  try:
    response = requests.get("https://api64.ipify.org?format=json")
    ip_data = response.json()
    ip_address = ip_data('ip')
    print(ip_address)
    
  except Exception as e:
    print("Error ocurred:", e)

def get_IPv4():
  hostname = socket.gethostname()
  ip_addr = socket.gethostbyname(hostname)
  print("Computer Name:", hostname)
  print("IPv4:", ip_addr)
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  s.connect(("8.8.8.8", 80))
  public_ip_addr = s.getsockname()[0]
  print("Public IPv4", public_ip_addr)

get_city()
get_IPv4()