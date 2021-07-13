import sys
import os
import glob
import shutil
from PIL import Image


'''
about this program:
	/resize img to 1200pixel
	/convert img from jpg to png
	/remove unneeded jpg image
	/extract match name file

Usage:
	you should put 2 args.
	First one is target that means original folder name to be converted and resized.
	Second one is dst that means destination folder name.
	Third one is dst_match that means match file containing folder name.

'''

PATH_high_jpg = "/home/daikiishiguro/AWS_data/after(High)"
PATH_low_jpg = "/home/daikiishiguro/AWS_data/after(Low)"


def main():
	target = sys.argv[1]
	dst = sys.argv[2]
	dst_match = sys.argv[3]
	os.makedirs(dst, exist_ok=True)
	os.makedirs(dst_match, exist_ok=True)
	size = 1200
#Sorted Low image processing
	# Img in target folder will be saved to dst folder after resized
	Resize(target, dst, size)

	jpg2png(dst)

	rm_jpg(dst)

	match_Sort(dst, dst_match)

	Resize(match_dst, dst_match, size)
	
	jpg2png(dst_match)
	
	rm_jpg(dst_match)

def match_Sort(dst, match):
	sorted_folder = dst
	original_folder = PATH_high_jpg
	dst_folder = match
	
	for i in glob.glob(sorted_folder + '/*.*'):
		file1 = os.path.splitext(os.path.basename(i))[0]
		for k in glob.glob(original_folder + '/*.*'):
			file2 = os.path.splitext(os.path.basename(k))[0]
			if file1 == file2:
				shutil.copy(k, dst_folder)

def rm_jpg(dst):
	for i in glob.glob(dst + '/*.jpg'):
		os.remove(i)
	for j in glob.glob(dst + '/*.JPG'):
		os.remove(j)

def convert(img_path, dst):
	filename = os.path.splitext(os.path.basename(img_path))[0]
	im = Image.open(img_path)
	im.save(dst + '/' + filename + '.png')

def jpg2png(dst):
	for i in glob.glob(dst + '/*.*'):
			convert(i, dst)

def Scale_to_width(img, longersize):
	if img.width>img.height:
		height = round(img.height * longersize / img.width)
		return img.resize((longersize, height))
	else:
		width = round(img.width * longersize / img.height)
		return img.resize((width, longersize))

def Resize(target, dst, size):
	print(target, dst, size)
	file_crop = glob.glob(target + '/*.*')
	for file in file_crop:
		img = Image.open(file)
		img_resize = Scale_to_width(img, size)
		filename = os.path.basename(file)
		img_resize.save(dst + '/' + filename, quality=95)
		
	

if __name__ == '__main__':
	main()
