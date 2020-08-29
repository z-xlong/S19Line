1 #!/usr/bin/env python
2 # -*- coding: utf-8 -*- 



def CreateS19Line(addressLength, address, dataBytes):
    #s19line = Sx length address data checksum
    #length = len(address) + len(md5) + len(checksum)
    #checksum = 0xFF - byte(len) - byte(address) - byte(data)
    s19Line = ""
    if (2 == addressLength):
        s19Line = "S1"
    elif (3 == addressLength):
        s19Line = "S2"
    elif (4 == addressLength):
        s19Line = "S3"
    else:
        return "Error"

    length = addressLength + len(dataBytes) + 1
    lengthBytes = length.to_bytes(1, byteorder='big')

    addressBytes = address.to_bytes(addressLength, byteorder='big')

    # dataBytes

    checksum = 0
    for i in lengthBytes + addressBytes + dataBytes:
        checksum += i
    checksum = 0xFF - checksum &0xFF
    checksumBytes = checksum.to_bytes(1, byteorder='big')

    s19Line += lengthBytes.hex().upper()
    s19Line += addressBytes.hex().upper()
    s19Line += dataBytes.hex().upper()
    s19Line += checksumBytes.hex().upper()
    s19Line += '\n'

    return s19Line
# end of: CreateS19Line(head, address, md5Bytes):





######################## Demo ########################
import hashlib

lineEnd = 'S80400991949'
data = 'asfdafasjfogjslgjsdfgjlskdj'

address = 0
addressLen = 0x00
md5 = hashlib.md5(data.encode("ASCII"))

if 'S9' == lineEnd[0:2]:
    addressLen = 2
elif 'S8' == lineEnd[0:2]:
    addressLen = 3
elif 'S7' == lineEnd[0:2]:
    addressLen = 4
else:
    print("error")

line = CreateS19Line(addressLen, address, md5.digest())

print(line)
######################## Demo ########################
