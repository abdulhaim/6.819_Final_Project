import sys
import Augmentor

folder_name='tensorflow-for-poets-2/tf_files/earthquake_damage_intensity'
p= Augmentor.Pipeline(source_directory=folder_name,save_format="jpg")
#p.flip_left_right(0.5)
#p.black_and_white(0.1)
p.gaussian_distortion(probability=0.4, grid_width=7, grid_height=6
                      , magnitude=6, corner="ul", method="in", mex=0.5, mey=0.5, sdx=0.05, sdy=0.05)

p.rotate(0.3, 10,10)
p.skew(0.4,0.5)
p.skew_tilt(0.6,0.8)
p.skew_left_right(0.5, magnitude=0.8)
p.sample(10000)



# #!/usr/bin/env python
# from glob import glob                                                           
# import cv2 
# pngs = glob('./*.jpg')

# for j in pngs:
#     img = cv2.imread(j)
#     cv2.imwrite(j[:-3] + 'png', img)