#!/usr/bin/python              
"""
48bits presents:
8===============================================D~~~
WhatsApp msgstore crypt5 decryptor by grbnz0 and nullsub
8===============================================D~~~
 
"""
                                                                                                                                                                                   
import sys
import hashlib
import StringIO
from M2Crypto import EVP
 
key = bytearray([141, 75, 21, 92, 201, 255, 129, 229, 203, 246, 250, 120, 25, 54, 106, 62, 198, 33, 166, 86, 65, 108, 215, 147])
iv = bytearray([0x1E,0x39,0xF3,0x69,0xE9,0xD,0xB3,0x3A,0xA7,0x3B,0x44,0x2B,0xBB,0xB6,0xB0,0xB9])
 
def decrypt(db,acc):
  fh = file(db,'rb')
  edb = fh.read()
  fh.close()
  m = hashlib.md5()
  m.update(acc)
  md5 = bytearray(m.digest())
  for i in xrange(24): key[i] ^= md5[i&0xF]
  cipher = EVP.Cipher('aes_192_cbc', key=key, iv=iv, op=0)
  sys.stdout.write(cipher.update(edb))
  sys.stdout.write(cipher.final())
 
if __name__ == '__main__':
  if len(sys.argv) != 3:
    print 'usage %s <db> <accountname> > decrypted.db' % sys.argv[0]
  else:
    decrypt(sys.argv[1],sys.argv[2])

