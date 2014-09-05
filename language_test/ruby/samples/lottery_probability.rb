=begin
	get the probability of prize money by lottery
	red/blue ball
	get 6 red ball in 33 number and 1 blue ball in 16 number
	0 + 0 5
	1 + 1 5
	2 + 1 5
	3 + 1 10
	4 + 0 10
	4 + 1 200
	5 + 0 200
	5 + 1 3000
	6 + 0 more
	6 + 1 more
=end

def factorial(x, n)
	m = (x - n + 1)
	(m..x).reduce(:*)
end


def combination(n, k)
	factorial(n, k) / factorial(k, 1)
end

def probabilityRed(reward, total)
	# get 6 from 33, one reward
	#1 / 33 + 1/ 32 + 1/ 31 + ... + 1 / 28
	puts combination(total, 1)
	Rational(combination(reward, 1), combination(total, 1))
end

puts probabilityRed(1, 16)