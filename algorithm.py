import os
from PIL import Image
import cv2

source_files = []

allowed_exts = ['jpeg', 'jpg', 'png']
def No_of_Image_Files(input_directory): 
    i = 0
    print(input_directory)
    for filename in os.listdir(input_directory):
        path = input_directory+filename

        #ext = filename.split('.')
        file = os.path.split(path)
        ext = file[1].split('.')
                
        if( len(ext) > 1 and (ext[1].lower() in allowed_exts)):
            print(ext[1])
            i += 1
            source_files.append(path)
        
    print("No of image files in the folder are: " + str(i) + '\n')
    print(source_files)
    print('\n')
 
def watermark_with_transparency(input_image_path,
                                output_image_path,
                                watermark_image_path,
                                position):

    base_image = Image.open(input_image_path)
    #print(base_image)

    watermark = Image.open(watermark_image_path).convert("RGBA")
    width, height = base_image.size

    if (base_image.size[0] > base_image.size[1]):
        ratio = base_image.size[0]/800
        watermark = watermark.resize((int(watermark.width*ratio),int(watermark.height*ratio)),resample=0)

    if (base_image.size[1] > base_image.size[0]):
        ratio = base_image.size[1]/1600
        watermark = watermark.resize((int(watermark.width*ratio),int(watermark.height*ratio)),resample=0)

    # percentage = base_image.size[1]/1600

    base_image_copy = base_image.copy()

    # watermark = watermark.resize((int(watermark.width*percentage),int(watermark.height*percentage)),resample=0)

    
    if(position == 1):
        position = (0,0)

    if(position == 2):
        position = ((base_image.width-watermark.width),0)

    if(position == 3):
        position = (0,(base_image.height-watermark.height))
    
    if(position == 4):
        position = ((base_image.width-watermark.width),(base_image.height-watermark.height))
    
    base_image_copy.paste(watermark,position,watermark)
    
    base_image_copy.save(output_image_path)


# Source folder
# WaterMark
# Output Folder Dir
# File Type: JPEG ya PNG
# Postion : 1,2,3,4

def algorithm_call(source_folder, watermark, output_folder, fileType, position):
    
    No_of_Image_Files(source_folder+'\\')

    img_no = 1

    for image in source_files:
        destination = output_folder +'\\' + str(img_no) + "."+str.lower(fileType)

        # top-left -> 1         top-right -> 2
        # bottom-left -> 3      bottom-right -> 4

        watermark_with_transparency(image, destination ,watermark,position)
        print('image '+ str(img_no) + ' Done\n')
        img_no += 1

    source_files.clear()
    print("..........Done..........\n")   

#