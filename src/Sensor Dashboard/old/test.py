
import re
import struct
import os
s = '''<440,307,669,406>
<461,567,539,334>
<371,664,402,523>
<545,333,490,624>
<568,505,630,315>
<445,554,340,695>
>
<665,576,433,601>
<455,468,477,480>
<461,567,539,334>
<371,664,402,523>
<545,333,490,624>
<568,505,630,315>
<445,554,340,695>
>
<665,576,433,601>
<455,468,477,480>
<461,567,539,334>
<371,664,402,523>
<545,333,490,624>
<568,505,630,315>
<445,554,340,695>
<300,656,506,499>
<689,611,654,363>
<363,369,309,571>
<696,489,513,383>'''

pattern=r"(?<=\<)(.*?)(?=\>)"
string=s

datapackets_flag = re.search(pattern=pattern, string=string)

#print(datapackets_flag)

datapackets = re.finditer(pattern=pattern, string=string)

#print([i.start() for i in datapackets])

p = "<S390,355,456,461SR749.42,737.30,583.78RG6167.16113281,3703.69995117G>"

k = re.search(f"(?<=S)(.*)(?=S)", p)
x = re.split(",", k.group())
print([int(i) for i in x ])

class poop():

    def __init__(self) -> None:
        self.load = 1

    def on_josh(self):
        print("i pooped on josh")

class bacteria(poop):

    def __init__(self) -> None:
        super().__init__()



ipoop = poop()

ipoop.on_josh()

print(ipoop.load)

ipoop.load = 2

print(ipoop.load)

b = bacteria()

b.load

x = [1,2,3,4,5,6]

z =  ['\x0f', '\x00']

t = [print(type(temp)) for temp in z]


print(x[1:])
#h = struct.unpack("h", b"".join(z))
h = bytes("".join(z), "utf-8")
print(h)
print(bool(3))