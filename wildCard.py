def wildCard(text, pattern):
	j=0 	#Counter for text
	i=0	#Counter for pattern

	while i < len(pattern) and j < len(text):
		ch = pattern[i]
		if ch not in ('?', '*'):
			if ch == text[j]:
				i += 1
				j += 1
			else:
				j += 1
	if i == len(pattern):
		return True
	return False

print wildCard("baaabab", "baaaba")
