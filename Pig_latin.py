vowels=['a','e','i','o','u']

s=raw_input("please input a word:")
if s[0] not in vowels:   #the first letter is consonant sound
	if s[1] in vowels:  #the second letter is vowel sound
		s=s[1:]+s[0]+'ay'
		
	else:
		'the second letter is also consonant sound\
		then we need found the consonant sound cluster and its size'
		
		size=2
		for i in range(2,len(s)):
			if s[i] not in vowels:
				size+=1
			else:
				break
		s=s[size:]+s[:size]+'ay'
		
else: #the first letter is vowel sound
	s=s[:]+'way'
	
print("the final s is:",s)