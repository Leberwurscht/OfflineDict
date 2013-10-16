#!/usr/bin/python
# -*- coding: utf8 -*-

import sys, re
filename = sys.argv[1]
tokensize = int(sys.argv[2])
numbersize = int(sys.argv[3])
numbersize2 = int(sys.argv[4])

def normalize(s):
  r = s.lower()
  r = r.replace(u'ä',u'a');
  r = r.replace(u'ö',u'o');
  r = r.replace(u'ü',u'u');
  r = r.replace(u'Ä',u'A');
  r = r.replace(u'Ö',u'O');
  r = r.replace(u'Ü',u'U');
  r = r.replace(u'ß',u'ss');
  r = r.replace(u'ñ',u'n');
  r = r.replace(u'á',u'a');
  r = r.replace(u'é',u'e');
  r = r.replace(u'í',u'i');
  r = r.replace(u'ó',u'o');
  r = r.replace(u'ú',u'u');
  r = r.replace(u'Á',u'A');
  r = r.replace(u'É',u'E');
  r = r.replace(u'Í',u'I');
  r = r.replace(u'Ó',u'O');
  r = r.replace(u'Ú',u'U');
  return r.encode("utf8")

pos = 0
for line in open(filename):
  linelength = len(line)

  if line.strip() and not line[0]=="#":
    length = len(line)
    line = unicode(line, 'utf8')
    i=line.rindex('\t')
    line = line[0:i]
    red = re.sub(r'\[.*?\]|\{.*?\}','',line,flags=re.UNICODE).strip()
    tokens = re.split(r'\W', red, flags=re.UNICODE)
    for token in tokens:
      ntoken = normalize(token)
      if len(ntoken)>tokensize: raise Exception("increase tokensize")
      if pos>10**numbersize-1: raise Exception("increase numbersize")
      if length>10**numbersize2-1: raise Exception("increase numbersize2")
      if ntoken: print ("%-"+str(tokensize)+"s %"+str(numbersize)+"d %"+str(numbersize2)+"d") % (ntoken, pos, length)

  pos += linelength
