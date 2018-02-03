def power2Sol(num):
	i = 1
	while i <= num:
		i <<= 1
	return i>>1

print power2Sol(17)
