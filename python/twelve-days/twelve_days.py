def recite(start_verse, end_verse):
    v = []
    for i in range(start_verse,end_verse+1):
		v.append(ss(i))
    return v

def ss(ind):
	num = ['first','second','third','fourth','fifth','sixth','seventh','eighth','ninth','tenth','eleventh','twelfth']
	gifts = ['twelve Drummers Drumming, ', 'eleven Pipers Piping, ', 'ten Lords-a-Leaping, ', 'nine Ladies Dancing, ', 'eight Maids-a-Milking, ', 'seven Swans-a-Swimming, ', 'six Geese-a-Laying, ', 'five Gold Rings, ', 'four Calling Birds, ', 'three French Hens, ', 'two Turtle Doves, and ', 'a Partridge in a Pear Tree.']
	return "".join(["On the {} day of Christmas my true love gave to me: ".format(num[ind-1])] + gifts[-ind:])
