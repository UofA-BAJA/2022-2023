# 12 Mar 2014

# in case any of this upsets Python purists it has been converted from an equivalent JRuby program

# this is designed to work with ... ArduinoPC.ino ...

# the purpose of this program and the associated Arduino program is to demonstrate a system for sending 
#   and receiving data between a PC and an Arduino.

# The key functions are:
#    sendToArduino(str) which sends the given string to the Arduino. The string may 
#                       contain characters with any of the values 0 to 255
#
#    recvFromArduino()  which returns an array. 
#                         The first element contains the number of bytes that the Arduino said it included in
#                             message. This can be used to check that the full message was received.
#                         The second element contains the message as a string


# the overall process followed by the demo program is as follows
#   open the serial connection to the Arduino - which causes the Arduino to reset
#   wait for a message from the Arduino to give it time to reset
#   loop through a series of test messages
#      send a message and display it on the PC screen
#      wait for a reply and display it on the PC

# to facilitate debugging the Arduino code this program interprets any message from the Arduino
#    with the message length set to 0 as a debug message which is displayed on the PC screen

# the actual process of sending a message to the Arduino involves
#   prefacing the message with a byte value of 254 (startMarker)
#   following that startMarker with a byte whose value is the number of characters in the original message
#   then the message follows
#      any bytes in the message with values of 253, 254 or 255 into a pair of bytes
#          253 0    253 1   or 253 2       as appropriate
#   suffixing the message with a byte value of 255 (endMarker)


# receiving a message from the Arduino involves
#    waiting until the startMarker is detected
#    saving all subsequent bytes until the end marker is detected
#    converting the pairs of bytes (253 0 etc) back into the intended single byte



# NOTES
#       this program does not include any timeouts to deal with delays in communication
#
#       for simplicity the program does NOT search for the comm port - the user must modify the
#         code to include the correct reference.
#         search for the line "ser = serial.Serial("/dev/ttyS80", 57600)"
#
#       the function bytesToString(str) is just a convenience to show the contents of a string as
#          a series of byte values to make it easy to verify data with non-ascii characters
#
#       this program does NOT include a checkbyte that could be used to verify that there are no
#          errors in the message. This could easily be added.
#
#       as written the Arduino program can only receive a maximum of 16 bytes. 
#          This must include the start- and end-markers, the length byte and any extra bytes needed 
#             to encode values of 253 or over
#          the arduino program could easily be modified to accept longer messages by changing
#                #define maxMessage 16
#
#       as written the Arduino program does NOT check for messages that are too long
#         it is assumed that the PC program will ensure compliance
#         extra code could be added to the Arduino program to deal with too-long messages
#           but it would add a lot of code that may confuse this demo.

#=====================================

#  Function Definitions

#======================================
import struct

def recvFromArduino():
  global startMarker, endMarker
  
  ck = []
  x = "z" # any value that is not an end- or startMarker
   # to allow for the fact that the last increment will be one too many
  
  t = 0
 
  
  # wait for the start character
  while  ord(x) != startMarker:
    #print("found start marker")
    x = ser.read()
  
  # save data until the end marker is found
  while ord(x) != endMarker:
    x = ser.read()
    ck.append(x)
    t += 1



  #print("found end marker")


  #ck.append(x)
  print(datetime.datetime.now())
  decodeHighBytes(ck)
#  print "RETURNDATA " + str(returnData[0])
  
  

#======================================

def decodeHighBytes(ck: list):

  global specialByte, byteCount
  special_shift = bytes([165])
  
  next_byte = special_shift
  x = []
  for byteIndex, byte in enumerate(ck):
    

    if ord(byte) == startMarker or ord(byte) == endMarker:
      continue
     
    if ord(byte) == specialByte:
      next_byte = ck[byteIndex + 1]
      temp = bytes([ord(next_byte) ^ ord(special_shift)])
     
      x.append(temp)
      #print(temp)


    x.append(byte)

  better_print_message(x)

def printmessage(x: list):
  global byteCount
  l = len(x)
  print("LENGTH OF BYTES IS ", l)
  count = 0
  ints = []
  for i in range(int(l / 2)):
    b = bytearray([ord(x[2*i]), ord(x[(2*i) + 1])])
    k = int.from_bytes(b, "little", signed=True)
    print(k)

def better_print_message(x: list):
  l = len(x)
  print("LENGTH OF BYTES IS ", l)
  fr = make_int(x[0], x[1])
  fl = make_int(x[2], x[3])
  br = make_int(x[4], x[5])
  bl = make_int(x[6], x[10])
  rrr = make_int(x[8], x[11])
  frr = make_int(x[10], x[11])
  flr = make_int(x[12], x[13])

 



def make_int(byte1, byte2) -> int:
  b = bytearray([ord(byte1), ord(byte2)])  
  return int.from_bytes(b, "little", signed=True)

def make_int_float(byte1, byte2, byte3, byte4) -> int:
  b = bytearray([ord(byte1), ord(byte2), ord(byte3),ord(byte4),])  
  print(struct.unpack('<f', b))
  #print(ints)

#======================================

# THE DEMO PROGRAM STARTS HERE

#======================================

import serial
import datetime

# NOTE the user must ensure that the next line refers to the correct comm port
ser = serial.Serial("COM9", 115200)

byteCount = 0
startMarker = 250
endMarker = 251
specialByte = 252


for i in range(10):
  
  recvFromArduino()

ser.close()

