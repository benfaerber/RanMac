import random, os, time, socket

interface = 'wlp4s0'
# Input your original mac address
original = ''

print("RanMac v1.0")
mode = input("Mode 1: Random mac, Mode 2: Original mac ")

def ranMac():
    return [ 0x00, 0x16, 0x3e,
        random.randint(0x00, 0x7f),
        random.randint(0x00, 0xff),
        random.randint(0x00, 0xff) ]

def pMac(mac):
    return ':'.join(map(lambda x: "%02x" % x, mac))

server = "www.google.com"
def isConnected():
	try:
		host = socket.gethostbyname(server)
		s = socket.create_connection((host, 80), 2)
		print("Successfully connected to " + server + "\n")
		return True
	except:
			print("Could not connect to " + server + "\n")
			pass
	return False

mac = ""
def connect():
	if mode == '1':
		mac = pMac(ranMac())
	else:
		mac = original
	print("Changing to " + mac)
	print()
	print("Taking " + interface + " down")
	os.system("sudo ifconfig " + interface + " down")
	time.sleep(1)
	print("Changing mac to " + mac + " on " + interface)
	os.system("sudo ifconfig " + interface + " hw ether " + mac)
	time.sleep(1)
	print("Relaunching " + interface)
	os.system("sudo ifconfig " + interface + " up")
	time.sleep(1)
	

connect()

while isConnected() == False:
	connect()
print("Connected")