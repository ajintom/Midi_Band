
def note_bar(hexa):
	# Import a library of functions called 'pygame'
	import pygame
	data=int(hexa)

 
	# Initialize the game engine
	pygame.init()	
 
	# Define the colors we will use in RGB format
	BLACK = (  0,   0,   0)
	WHITE = (255, 255, 255)
	BLUE =  (  0,   0, 255)
	GREEN = (  0, 255,   0)
	RED =   (255,   0,   0)
 
	# Set the height and width of the screen
	size = [640, 480]
	screen = pygame.display.set_mode(size)
 
	pygame.display.set_caption("Plis Work!!!!")
	i=0	

	   #loop for inputtin the notes
		
	if data==48 or 60:		
		#arr.append(48)
		note_pos=10
	elif data==50 or 62:
		#arr.append(50)
		note_pos=40
	elif data==52 or 64:
		#arr.append(52)
		note_pos=80
	elif data==53 or 65:
		#arr.append(53)
		note_pos=120
	elif data==55 or 67:
		#arr.append(55)
		note_pos=160
	elif data==57 or 69:
		#arr.append(57)
		note_pos=200
	elif data==59 or 71:
		#arr.append(59)
		note_pos=240
        a=0
	while a!=1651:	
		screen.fill(BLACK)
		if a==5:
			pygame.draw.rect(screen, RED, [10, note_pos, 100, 20]) 
	   		pygame.display.flip()
		
		if a==150:
			pygame.draw.rect(screen, RED, [10, note_pos, 150, 20]) 
   			pygame.display.flip()
		if a==300:
			pygame.draw.rect(screen, RED, [10, note_pos, 200, 20]) 
    			pygame.display.flip()

		if a==450:
			pygame.draw.rect(screen, RED, [10, note_pos, 250, 20]) 
    			pygame.display.flip()
	
		if a==600:
			pygame.draw.rect(screen, RED, [10, note_pos, 300, 20]) 
    			pygame.display.flip()
			screen.fill(BLACK)
		if a==750:
			pygame.draw.rect(screen, RED, [10, note_pos, 350, 20]) 
    			pygame.display.flip()
			
		if a==900:
			pygame.draw.rect(screen, RED, [10, note_pos, 300, 20]) 
    			pygame.display.flip()
		
		if a==1050:
			pygame.draw.rect(screen, RED, [10, note_pos, 250, 20]) 
    			pygame.display.flip()
		if a==1200:
			pygame.draw.rect(screen, RED, [10, note_pos, 200, 20]) 
    			pygame.display.flip()

		if a==1350:
			pygame.draw.rect(screen, RED, [10, note_pos, 150, 20]) 
    			pygame.display.flip()			
		if a==1500:
			pygame.draw.rect(screen, RED, [10, note_pos, 100, 20]) 
    			pygame.display.flip()
		if a==1650:
			pygame.draw.rect(screen, RED, [10, note_pos, 0, 20]) 
    			pygame.display.flip()
		a=a+1
	
	

		
	pygame.quit()


