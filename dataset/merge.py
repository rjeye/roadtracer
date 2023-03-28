import numpy
import cv2 
import sys


path = sys.argv[1]
region = sys.argv[2]
x_start = int(sys.argv[3])
y_start = int(sys.argv[4])
x_end = int(sys.argv[5])
y_end = int(sys.argv[6])
out_fname = sys.argv[7]

x_len = x_end - x_start
y_len = y_end - y_start

merged_im = numpy.zeros((x_len * 4096, y_len * 4096, 3), dtype='uint8')

for i in range(x_len):
	for j in range(y_len):
		fname = '{}/{}_{}_{}_sat.png'.format(path, region, x_start + i, y_start + j)
		image_patch = cv2.imread(fname, cv2.IMREAD_COLOR)[:, :, 0:3].swapaxes(0, 1)
		merged_im[i*4096:(i+1)*4096, j*4096:(j+1)*4096, :] = image_patch

merged_im = merged_im.swapaxes(0, 1)
cv2.imwrite(out_fname, merged_im)


