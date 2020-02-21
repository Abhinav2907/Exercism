def is_isogram(string):
    for l in 'abcdefghijklmnopqrstuvwxyz':
		count = 0
		for word in string:
			if l == word.lower():
				count +=1
		if count > 1:
			return False
    return True
