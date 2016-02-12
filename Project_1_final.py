# Regie Daquioag
# CST 205 Project 1
# Project 1 CST 205 
# In this project we were suppose take 9 images with a man in every image but in different places.
# We were suppose to find the median of the 9 images and sent it to a new image where the man is 
# no longer there. We basically did photoshop with code... 


list = [] # makes a list of images

#for ix in range (0,9): # from 0-8 (9 pictures)
#  file = pickAFile() # picks a picture 
#  image = makePicture(file)# makes a picture that will be stored
#  list.append(image) # adds picture object to the list

folder = "/Users/regie/Desktop/CST_205_Project_1/"
# for ix in range (1,10): # from 1-9 (9 pictures)
for ix in range (1,10):
  image = folder + str(ix) + ".png"
  myPicture = makePicture(image)
  list.append(myPicture)

height = getHeight(myPicture) # gets the height for the new pictures
width = getWidth(myPicture) # gets the width of the new picture

redPixel =[] # makes an empty list for the reds
bluePixel = [] # makes an empty list for the blues
greenPixel = [] # makes an empty list for the greens

newPicture = makeEmptyPicture(width,height) # just making a new image that is empty

def findTheMedian(PixelList): # the function that will find the median of the 9 imagees
  lengthOfList = len(PixelList) # gets the length of the list of pixels
  sortTheValues = sorted(PixelList) # sorts the pixels 
  median = ((lengthOfList/2)) # gets the median of the all the pixels
  return sortTheValues[median] # returns the median pixel

# nested for loop that goes to the same pixel for each 9 pictures, for every pixel incrementing  by one
for x in range(0, width):
  for y in range(0, height):
    for pic in range(0,len(list)):
    
      pixel = getPixelAt(list[pic],x,y) # gets the pixel at the certain position depending on width and height
      redImg = getRed(pixel) # gets the pixel for the red color
      blueImg = getBlue(pixel) # gets the pixel for the blue color
      greenImg = getGreen(pixel) #gets the pixel for the green color
      
      redPixel.append(redImg) #add the red pixels to the list
      bluePixel.append(blueImg) #add the blue pixels to the list
      greenPixel.append(greenImg) #add the green pixels to the list
    
    # median calculations
    setRed(getPixel(newPicture,x,y), findTheMedian(redPixel)) # set red-nes of pixel at (newPicture, x, y) with value findTheMedian()
    setBlue(getPixel(newPicture,x,y), findTheMedian(bluePixel)) # set blue-nes of pixel at (newPicture, x, y) with value findTheMedian()
    setGreen(getPixel(newPicture,x,y), findTheMedian(greenPixel)) # set green-nes of pixel at (newPicture, x, y) with value findTheMedian()
    
    # clears our red, blue, green value lists
    redPixel = [] # temporary list for the red pixels which is now being deleted
    bluePixel = [] # temporary list for the blue pixels which is now being deleted
    greenPixel = []# temporary list for the green pixels which is now being deleted
       
show(newPicture) 
