import sys, os
from multiprocessing import Pool
from subprocess import call

class NdsMapMerge:
	def getProvinceList(self):
		return filter(lambda x: x.endswith(".db"), os.listdir("."))

	def merge(self, file1, file2):
		result = self.resultFilename(file1, file2)
		print "merge", file1, file2, result
		call(["nds_merge.exe", "-m", file1, file2, result])

	def resultFilename(self, file1, file2):
		return file1.rstrip(".db") +"_"+file2.rstrip(".db")+".db"

	def run(self):
		pool = Pool()
		files = self.getProvinceList()

		while len(files) != 1:
			middle = len(files) / 2
			map(lambda x,y: self.merge(x, y), [x for x in files[:middle]], [y for y in files[-middle:]])
			result = map(lambda x,y: self.resultFilename(x, y), [x for x in files[:middle]], [y for y in files[-middle:]])
			if len(files) % 2 != 0:
				result.append(files[middle])
			files = result
		os.rename(files[0], "qvf.db")

def main():
	merge = NdsMapMerge()
	merge.run()


if __name__ == '__main__':
	main()
