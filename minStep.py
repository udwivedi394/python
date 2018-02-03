INT_MAX = 456413131

def minStep(cur_pos, step, destination):
	if abs(cur_pos) > destination:
		return INT_MAX

	if cur_pos+step == destination:
		return step

	posetive = minStep(cur_pos+step, step+1, destination)
	#BackTrack
	negative = minStep(cur_pos-step, step+1, destination)

	return min(posetive, negative)

print minStep(0, 0, 6)
