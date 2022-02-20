import os

file = os.listdir("Test")

file = ["asewfw.THM", "fiawuhiaoush.LRV"]
for i in file:
  if "thm" or "lrv" in i.lower():
	  os.remove(i)
