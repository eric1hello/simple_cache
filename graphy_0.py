#!/usr/bin/python3
import sys
import re
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
mapping_ways = [1, 2, 4, 8, 12, 16]
line_size = [32, 64, 128]
swap_style = [0, 1, 2]
class rate:
	def __init__(self, cache_size, line_size, way, swap):
		self.way = int(way)
		self.line_size = int(line_size)
		self.size = int(cache_size)
		self.swap = int(swap)
		self.miss_rate = 0
		self.read = 0
		self.write = 0
	def __str__(self):
		return "%s %s" %(self.way,self.line_size)

rates = []
def work():
	global rates
	with open('input', 'r')as f:
		line = f.readline()
		while line:
			if line.find('line_size') >=0:
				reg = re.compile("cache_size: (\d+) Bytes.+line_size: (\d+).+mapping ways (\d+).+swap_style (\d+)")
				ans = reg.findall(line)
				ans = ans[0]
				arate = rate(ans[0], ans[1],ans[2],ans[3])
				f.readline()
				f.readline()
				line = f.readline()
				reg2 = re.compile(".+hit rate.+/([\d|\.]+)")
				ans2 = reg2.findall(line)
				ans2 = ans2[0]
				arate.miss_rate = float(ans2)
				line = f.readline()
				reg3 = re.compile(".+ (\d+) Bytes")
				ans3 = reg3.findall(line)[0]
				arate.read = int(ans3)
				line = f.readline()
				ans4 = reg3.findall(line)[0]
				arate.write = int(ans4)
				rates.append(arate)
			line = f.readline()

def draw_way():

	line_size = [32,64,128]
	swap = [0,1,2]
	swap_description = ["FIFO",'LRU','RAND']
	color_map = 'rgbyck'
	plts = []
	my_patches = []
	# for line in swap:
	line = 1
	x = []
	y = []
	y1 = []
	y2 = []
	for node in rates:
		# print(type(node.swap), type(node.line_size))
		if	(node.line_size == 32) and (node.swap == line) :
			# y.append(node.miss_rate)
			y1.append(node.read)
			y2.append(node.write)
			x.append(node.way)
		# plt.subplot(221+ swap.index(line))
	plt.plot(x, y1, color_map[line], )
	# plt.plot(x, y2,color_map[line+1])
	print(x,y1,y2)
	my_patches.append(mpatches.Patch(color=color_map[line],label=swap_description[line]))
	line += 1
	my_patches.append(mpatches.Patch(color=color_map[line],label=swap_description[line]))
	
	plt.legend(handles=my_patches)

def draw_cache_line_size():

	line_size = [32,64,128]
	swap = [0,1,2]
	swap_description = ["FIFO",'LRU','RAND']
	color_map = 'rgbyck'
	plts = []
	my_patches = []
	# for line in swap:
	line = 1
	x = []
	y = []
	y1 = []
	y2 = []
	for node in rates:
		# print(type(node.swap), type(node.line_size))
		if	(node.way ==8) and (node.swap == line) :
			# y.append(node.miss_rate)
			x.append(node.line_size)
			y1.append(node.read)
			y2.append(node.write)
		# plt.subplot(221+ swap.index(line))
	# plt.plot(x, y, color_map[line])
	plt.plot(x, y1, color_map[line])
	plt.plot(x, y2,color_map[line+1])
	# my_patches.append(mpatches.Patch(color=color_map[line],label=swap_description[line]))
	# line += 1
	# my_patches.append(mpatches.Patch(color=color_map[line],label=swap_description[line]))
	my_patches.append(mpatches.Patch(color=color_map[line],label="Read"))
	line += 1
	my_patches.append(mpatches.Patch(color=color_map[line],label="Write"))
	plt.legend(handles=my_patches)

def draw_swap():
	line_size = [32,64,128]
	swap = [0,1,2]
	swap_description = ["FIFO",'LRU','RAND']
	color_map = 'rgbyck'
	plts = []
	my_patches = []
	index = np.arange(3)

	# for line in swap:
	line = 0
	x = [[],[],[]]
	y = [[],[],[]]
	y1 = []
	y2 = []
	for node in rates:
		temp_x = []
		temp_y = []
		# print(type(node.swap), type(node.line_size))
		if	(node.line_size == 32) and (node.way==8) :
			# y.append(node.miss_rate)
			x[node.swap].append(node.size)
			y[node.swap].append(node.miss_rate)
			# y1.append(node.read)
			# y2.append(node.write)
		# plt.subplot(221+ swap.index(line))
	bar_width = 0.4
	plt.plot(x[line],y[line],color_map[line])
	my_patches.append(mpatches.Patch(color=color_map[line],label="FIFO"))
	line+=1
	plt.plot(x[line],y[line],color_map[line])
	my_patches.append(mpatches.Patch(color=color_map[line],label="LRU"))
	line+=1
	plt.plot(x[line],y[line],color_map[line])
	my_patches.append(mpatches.Patch(color=color_map[line],label="RAND"))
	line += 1
	for i in range(len(y[0])):
		print("|%d|%f|%f|%f|" %(x[0][i]>>10,y[0][i],y[1][i],y[2][i]))
	plt.legend(handles=my_patches)

def draw_cache_size():
	line_size = [32,64,128]
	size = [8, 16, 32, 64, 128,256,512]
	swap = [0,1,2]
	swap_description = ["FIFO",'LRU','RAND']
	color_map = 'rgbyck'
	plts = []
	my_patches = []
	# for line in swap:
	line = 1
	x = []
	y = []
	y1 = []
	y2 = []
	for node in rates:
		# print(type(node.swap), type(node.line_size))
		if	(node.way ==8) and (node.swap == 1) and node.line_size == 32 :
			# y.append(node.miss_rate)
			x.append(node.size)
			y1.append(node.read)
			y2.append(node.write)
		# plt.subplot(221+ swap.index(line))
	# print(x,y)
	# plt.plot(x, y, color_map[line])
	plt.plot(x, y1, color_map[line])
	plt.plot(x, y2,color_map[line+1])
	# my_patches.append(mpatches.Patch(color=color_map[line],label=swap_description[line]))
	# line += 1
	# my_patches.append(mpatches.Patch(color=color_map[line],label=swap_description[line]))
	my_patches.append(mpatches.Patch(color=color_map[line],label="Read"))
	line += 1
	my_patches.append(mpatches.Patch(color=color_map[line],label="Write"))
	plt.legend(handles=my_patches)
def draw():
	global rates
	y  = []
	x = []
	for node in rates:
		# print(type(node.swap), type(node.line_size))
		if	(node.line_size == 64) and (node.swap == 0):
			y.append(node.miss_rate)
			x.append(node.way)
	print(x)
	print(y)

	plt.subplot(221)
	plt.plot(x, y, 'r')
	plt.grid(True)

work()
# draw_way()
# draw_cache_line_size()
draw_swap()
# draw_cache_size()


plt.show()
