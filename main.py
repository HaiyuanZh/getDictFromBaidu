#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys, getopt, time, random, datetime

# 打印函数
def prt(word):
   #print(time.strftime('%Y-%m-%d %H:%M:%S ',time.localtime(time.time())), word)
   print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3], word)

# 读文件函数
def readfile(inputfile, inteval, randomint):
   file_object = open(inputfile, 'rU')
   try:
      for line in file_object:
         prt(line)
         time.sleep((inteval + random.randint(1, randomint)) / 1000)
   finally:
      file_object.close()

# 处理参数
def para(argv):
   try:
      opts, args = getopt.getopt(argv,"hi:s:r:",["ifile=","inteval=", "additioninteval="])
   except getopt.GetoptError:
      print(sys.argv[1] + ' -i <inputfile> -s <nn> -r <mm>')
      sys.exit(2)
   for opt, arg in opts:
      if opt in ("-h", "--help"):
         print(sys.argv[1] + ' -i <inputfile> -s <nn> -r <mm>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-s", "--inteval"):
         inteval = int(arg)
         if inteval < 100:  #不允许小于100毫秒
            inteval = 100
      elif opt in ("-r", "--additioninteval"):
         randomInteval = int(arg)
         if randomInteval < 2:
            randomInteval = 2
   return inputfile, inteval, randomInteval



if __name__ == "__main__":
   i, s, r = para(sys.argv[1:])
   readfile(i, s, r)


