import os, sys
from subprocess import call
from multiprocessing import Pool
from multiprocessing import cpu_count

def parseParams(paramsFile):
	fp = open(paramsFile)
	for line in fp.readlines():
		line = line.strip()
		if line == "#":
			break

		yield line
		#params = line.split(" ")
		#yield params

	fp.close()

def show(info):
	print info

def main():
	if len(sys.argv) == 1:
		#debug mode
		paramsFile = "compile_map_nds.txt"
	elif len(sys.argv) == 2:
		paramsFile = sys.argv[1]
	else:
		print "params error"
		return

	pool = Pool(max(1, cpu_count()-1))
	try:
		print pool.map(os.system, parseParams(paramsFile))      
	except Exception, e:
		print "configure file error"
		raise

if __name__ == "__main__":
	main()


