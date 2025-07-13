from numpy.dtypes import StringDType
import numpy as np
import codecs as cd
byte_string = b"Arpit"
print(byte_string)
print(byte_string.decode("utf-8"))
print(str(byte_string,encoding="utf-8"))

byte_stringa = b"\x20\x61\x62"
print(cd.decode(byte_stringa,encoding="utf-8"))
print(cd.encode(cd.decode(byte_stringa,encoding="utf-8"),'utf-8'))

print(np.array([1, object(), 3.4], dtype=StringDType(coerce=True)))