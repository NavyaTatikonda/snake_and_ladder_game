import time

from random import randint
x = input("Your date of birth without spaces : ") ;
y = input("Your friend's date of birth without spaces : ");

if(x > y ) :
	print("Player1 should start first")
elif(x < y) : 
	print("Player2 should start first")
elif ( x == y) :
	print("Your wish ")
#################
for i in xrange (1,3) :
	print("You are now ready to start your game..")
	time.sleep(1)
#for x in xrange(1,9):
#	
#	print(x)
#	time.sleep(1)
	raw_input("Press any key to role the die!")

	x = str(randint(-6, 6))
	print("You can move " + x + " Steps ")
 	if(x==6) :
 		print("Your turn again!")  
