from bluepy.btle import Scanner, DefaultDelegate


class ScanDelegate (DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, device, isnewdev, isnewdata):
        if isnewdev:
            print("Discovered device", device.addr)

        if isnewdata:
            print("Received new data from", device.addr)
            #print("raw data is: {}" .format(device.rawData))
'''read data not completed yet'''
class ReadDelegate(DefaultDelegate):
	def __init__(self):
		self.data = 'b'
		
	def reset(self):
		self.data = 'b'
		
	def handleNotification(self, chandle, data)
		print("data is")
		print(data)
		self.data = self.data + data
		
	@property
	def data_length(self):
		return len(self.data)        


scanner = Scanner().withDelegate(ScanDelegate())
print("scanning ...")
devices = scanner.scan(10.0, True)

for dev in devices:
    print("Device %s (%s), RSI=%d db" % (dev.addr, dev.addrType, dev.rssi))
    for (tag, desc, value) in dev.getScanData():
        print("%s = %s" % (desc, value))
        





        
print("**************")
