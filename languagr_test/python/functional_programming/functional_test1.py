# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        模块1
# Purpose:
#
# Author:      yangdi
#
# Created:     08/02/2014
# Copyright:   (c) yangdi 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def even_filter(nums):
    return filter(lambda x: x % 2 == 0, nums)

def multi_3(nums):
	return map(lambda x: x * 3, nums)

def show(nums):
	return reduce(lambda x,y: str(x) + "," + str(y), nums)

def main():
	#pipleline_func()
	print show(multi_3(even_filter([1,2,3,4,5,6])))

#half-search
def get_half(nums, i, j):
	return nums[(i + j) / 2]

def half_search(nums, value):
	return map(get_half)

def multi(x):
	def multix(y):
		return x * y
	return multix

multi3 = multi(3)
multi4 = multi(4)
print multi3(5)

def show2(a):
	print a

if __name__ == '__main__':
	show2(even_filter([1,2,3,4,5,6]))
    #main()

