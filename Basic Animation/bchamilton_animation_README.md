Ben Hamilton
Basic Animation
This is just meant to be basic animation work
October 24, 2025

import pygame

#obvious first step
#Now because this is going to use a sprite sheet, I have to load the frames in that sheet
#So let's introduce a function that lets that happen.

define function loadFrames(the image, width of sprite, height of sprite, columns in sheet, rows in sheet)
	variable picture get's the loaded image and converts it with transparency
	create an empty variable called frames
	#this is where I will store all the frames
	for each row in the range rows
		for each column in the range columns
			variable x will get the column multiplied by the width of the sprite
			variable y will get the row multiplied by the height of the sprite
			frame will get a subsurface image of the frame
			#This isn't creating a surface so much as creating a reference that the program can use to find
			#the sprite that we're talking about. Like an index at the end of a book that points to a page
			#with the thing in it.
			the empty list frames gets the frame added to it
	return frames
	
#With that done, we can now define our main function

define main function
	initiate pygame
	
	variable screen gets the pygame display thats 640 pixels wide and 480 pixels tall
	the display's caption tells you what is happening
	
	background gets the image "country-platform-preview.png"
	convert that
	set the background to the display size
	
	variable frames calls the loadFrames("PrinceRanger.png", 32, 32, 8, 4) function
	#This tells us that the sprite is 32x32 pixels and there are 8 columns and 4 rows
	walk_row gets 2
	walk_frames gets a range of frames from frames list, specifically walk_row times 8 through walk_row + 1 times 8
	#This is just 16:24 in the frames list
	walk_frames is made over twice as large (32x32 -> 80x)
	
	current_frame get 0
	frame_x gets 44
	frame_y gets 340
	#This just means the guy is solidly on the path
	direction gets "right"
	#I'm particularly proud of this little guy, it was the key maybe the most impressive thing I did in this program
	speed gets 5
	
	clock gets the pygame time.Clock() function
	keepGoing while loop
		set clock to 30 ticks per second
		for event in pygame event get function
			if pygame quit happens end the loop
			if the mouse clicks
				get the mouse position
				print where the mouse was
				#Not to toot my own horn but this is how I found where to put my sprite and I felt like a genius
				#I also marked it out so it doesn't happen in the final product but it's there.
				
		current_frame gets (current_frame - 0.2) % length of walk_frames
		frame gets walk_frames[int(current_frame)]
		#To explain this because this took me way too long to get right, it cycles too fast for current_frame
		#to be walk_frames, but if you make it wait a bit between each walk_frames by making it not quite a 
		#whole number it makes the whole thing slower
		
		if direction is right
			frame_x adds the value of speed
			if frame_x + 80 is greater than or equal to 640
			#frame_x is the left corner of the sprite so I need the to turn 80 pixels earlier and 640 is the edge
			#of the screen
				walk_frames is pygames transform flipped for all its frames
				direction is set to left
		elif direction is left
			frame_x subtracts the value of speed
			if frame_x is less than or equal to 0
				flip walk_frames back around
				direction is right
		else
			frame_x is 0
			direction is right
			
		#That may not be the cleanest code anyone's every written but I felt like Alan Turing after solving
		#enigma finally making the sprite turn around instead keep on frolicing to the left like it was doing
		
		screen.blit background
		screen.blit(frame, [frame_x, frame_y])
		pygame.display.flip()
		
		#I'll be honest I've watched your videos, I've looked this up and it still doesn't make sense to me. It 
		#doesn't work if I don't do it, so I do it, but the best I can tell you is it makes the screen not black 
		#and it makes the sprite be where the sprite is meant to be. I suppose that's all it really needs to be isn't it.
		
	pygame.quit()
	
call main