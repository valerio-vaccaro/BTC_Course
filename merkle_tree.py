import hashlib

doc1 = "AAAAAA"
doc2 = "BBBBBB"
doc3 = "CCCCCC"
doc4 = "DDDDDD"
doc5 = "EEEEEE"
doc6 = "FFFFFF"
doc7 = "GGGGGG"

hash1 = hashlib.sha256(doc1).hexdigest()
print("hash _______1 "+hash1+" from "+doc1)
hash2 = hashlib.sha256(doc2).hexdigest()
print("hash _______2 "+hash2+" from "+doc2)
hash3 = hashlib.sha256(doc3).hexdigest()
print("hash _______3 "+hash3+" from "+doc3)
hash4 = hashlib.sha256(doc4).hexdigest()
print("hash _______4 "+hash4+" from "+doc4)
hash5 = hashlib.sha256(doc5).hexdigest()
print("hash _______5 "+hash5+" from "+doc5)
hash6 = hashlib.sha256(doc6).hexdigest()
print("hash _______6 "+hash6+" from "+doc6)
hash7 = hashlib.sha256(doc7).hexdigest()
print("hash _______7 "+hash7+" from "+doc7)


hash12 = hashlib.sha256(hash1+hash2).hexdigest()
print("hash ______12 "+hash12+" from "+hash1+hash2)
hash34 = hashlib.sha256(hash3+hash4).hexdigest()
print("hash ______34 "+hash34+" from "+hash3+hash4)
hash56 = hashlib.sha256(hash5+hash6).hexdigest()
print("hash ______56 "+hash56+" from "+hash5+hash6)
hash77 = hashlib.sha256(hash7+hash7).hexdigest()
print("hash ______77 "+hash7+" from "+hash7+hash7)

hash1234 = hashlib.sha256(hash12+hash34).hexdigest()
print("hash ____1234 "+hash1234+" from "+hash12+hash34)
hash5677 = hashlib.sha256(hash56+hash77).hexdigest()
print("hash ____5677 "+hash5677+" from "+hash56+hash77)

hash12345677 = hashlib.sha256(hash1234+hash5677).hexdigest()
print("hash 12345677 "+hash12345677+" from "+hash1234+hash5677)
