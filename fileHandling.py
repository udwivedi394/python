#Encode a binary string into bytearray
def bitstring_to_bytes(s):
	v = int(s, 2)
	#print v
	b = bytearray()
	while v:
		b.append(v & 0xff)
		v >>= 8
	#b = b[::-1]
	return b

#This part is for testing purpose of file handling
'''
file1 = open("Utkarsh_testing.txt", "w")

file1.write("Hi! This is Utkarsh!")
file1.close()

file2 = open("Utkarsh_testing.txt", "r")

print file2.read()
file2.close()
'''
encode_dict = {'f': 0, 'c':100, 'd':101, 'a':1100, 'b': 1101, 'e': 111}
decode_dict = {}

#Opening a binary file
file1 = open("binary_test.dat", "wb")
#encoded_str = "010110011011100111110100"
#encoded_str = "01011001"
encoded_str = ''
actual_string = 'fdcbaeee'

for ch in list(actual_string):
	encoded_str += str(encode_dict.get(ch))

print encoded_str
for i in range(0,len(encoded_str),8):
	b = bitstring_to_bytes(encoded_str[i:i+8])
	file1.write(b)
file1.close()

for key,value in encode_dict.iteritems():
	decode_dict[int(str(value),2)] = key

file2 = open("binary_test.dat", "rb")
try:
	str1 = ''
	while 1:
		byte = file2.read(1)
		if len(byte) == 0:
			break
		byte = ord(byte)
		#print byte
		filt = 1<<7
		while byte:
			str1 += str((byte&filt)>>7)
			val = int(str1,2)
			if decode_dict.get(val):
				print decode_dict[val],
				str1 = ''
			byte = (byte<<1)&0xff
finally:
	file2.close()
