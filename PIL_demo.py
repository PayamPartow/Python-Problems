from PIL import Image , ImageFilter
import os #used to loop over files in the directory

image1 = Image.open('photo-1549692520-acc6669e2f0c.jpg')
#to rotate images and convert them to balck and white
image1.convert(mode='L').rotate(90).save('photo-1549692520-acc6669e2f0c(mod).jpg') 
#bluring our image using the Imagefilter module
image1.filter(ImageFilter.GaussianBlur(15)).save('photo-1549692520-acc6669e2f0c(blured).jpg')







# size_300  = (300,300) #deciding the file size for the resized images needs to be a 2 dimensional tupol
# size_700 = (700,700)
# for f in os.listdir('.'):
#      if f.endswith('.jpg'):
#         i = Image.open(f)               
#         fn, fext = os.path.splitext(f) #breaks everything up into a file name and a file extension
#         #print(fn, fext)
#         i.thumbnail(size_300) #creating the resized images
        
#         #i.save('pngs/{}.png'.format(fn)) #first pngs is the folder name second png is format
#         i.save('300/{}_300{}'.format(fn, fext))

#         i.thumbnail(size_700)
#         i.save('700/{}_700{}'.format(fn, fext))
#image1 = Image.open('photo-1549692520-acc6669e2f0c.jpg')
#image1.show() #displays the image to the screen
# image1.save('photo-1549692520-acc6669e2f0c.png') #saves the image with a different format
