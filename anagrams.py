import string

W = ["bhargav", "miss", "ssim", "bharvag", "ab", "abb", "bba"]
W = W.rstrip(",") 
A = []

my_array = [chr(i) for i in range(ord('a'), ord('z')+1)]
index = 0

def anagrams(W):
	for i in W:
		if i in my_array:
			index = my_array.index(i)
			index += 1
		else:
			print ("Not a valid input")

def valid(anagrams):
	global A
	if W in A:
		print ("TRUE")
	else:
		print ("FALSE")
		A = A.append(W)

anagrams(W)
valid(anagrams)
