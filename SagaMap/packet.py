# -*- coding: utf-8 -*-
import struct 

def reverseByteNumber(data, offset, length):
	ddata = data[offset:length]
	ddata = bytearray([i for i in reversed(ddata)])
	return ddata

class Packet(object):
	ID = 0
	data = []
	size = 0
	sessionID = 0

	def getSessionID(self):
		self.sessionID = struct.unpack("I", self.data[2:6])[0]
		return self.sessionID

	def setSessionID(self, value):
		dbytes = struct.pack("I", value)
		dbytes = bytearray(dbytes)
		self.data[2] = dbytes[0]
		self.data[3] = dbytes[1]
		self.data[4] = dbytes[2]
		self.data[5] = dbytes[3]

	def setLength(self):
		dbytes = struct.pack("H", self.size)
		dbytes = bytearray(dbytes)
		self.data[0] = dbytes[0]
		self.data[1] = dbytes[1]

	def getLength(self):
		dlength = bytearray(self.data[0:2])
		self.size = struct.unpack("h", dlength)[0]
		return self.size

	def getPacketID(self):
		did = reverseByteNumber(self.data, 6, 8)
		self.ID = struct.unpack("H", did)[0]
		return self.ID

	def setID(self, value):
		did = struct.pack("H", value)
		did = reverseByteNumber(did, 0, 2)
		self.data[6] = did[0]
		self.data[7] = did[1]

	def getUInt(self, offset):
		ddata = bytearray(self.data[offset: offset+4])
		return struct.unpack("I", ddata)[0]

	def getInt(self, offset):
		ddata = bytearray(self.data[offset:offset+4])
		return struct.unpack("i", ddata)[0]

	def getFloat(self, offset):
		#ddata = reverseByteNumber(self.data, offset, offset+4)
		ddata = bytearray(self.data[offset:offset+4])
		return struct.unpack("i", ddata)[0] / 1000

	def setFloat(self, offset, value):
		dvalue = int(value * 1000)
		self.setUInt(offset, dvalue)

	def setUShort(self, offset, value):
		ddata = struct.pack("H", value)
		ddata = bytearray(ddata)
		self.data[offset] = ddata[0]
		self.data[offset+1] = ddata[1]

	def getUShort(self, offset):
		ddata = reverseByteNumber(self.data, offset, offset+2)
		ddata = bytearray(ddata)
		return struct.unpack("H", ddata)

	def setUInt(self, offset, value):
		ddata = struct.pack("I", value)
		ddata = bytearray(ddata)
		self.data[offset] = ddata[0]
		self.data[offset+1] = ddata[1]
		self.data[offset+2] = ddata[2]
		self.data[offset+3] = ddata[3]

	def setInt(self, offset, value):
		ddata = struct.pack("i", value)
		ddata = bytearray(ddata)
		self.data[offset] = ddata[0]
		self.data[offset+1] = ddata[1]
		self.data[offset+2] = ddata[2]
		self.data[offset+3] = ddata[3]

	def setString(self, data, offset, length):
		byte = str.encode(data, "UTF-16le")
		self.setBytes(byte, offset, length)

	def setBytes(self, data, offset, length):
		le = len(data)
		length = length if le >= length else le
		for i in range(length):
			self.data[offset + i] = data[i]

	def setStringArrayResize(self, data, offset, length):
		buffer = self.data
		lenf = len(buffer) + length
		ddata = [0] * lenf

		for i,v in enumerate(buffer):
			ddata[i] = v

		self.data = ddata
		self.size = lenf
		self.setLength()
		self.setString(data, offset, length)
