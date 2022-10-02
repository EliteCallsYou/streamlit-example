##########################################################################################################

import pandas as pd
import streamlit as st
from PIL import Image
import cv2 as cv

#####################################################


original_title = "<p style='font-family:Courier; color:Blue; font-size: 16px;'>Which image from the pj20_jets mission do u want</p>"
st.markdown(original_title, unsafe_allow_html=True)
image_name = st.selectbox( '',
 ('', 'JNCE_2019149_20C00028_V01-raw','JNCE_2019149_20C00030_V01-raw',
 'JNCE_2019149_20C00043_V01-raw','JNCE_2019149_20C00045_V01-raw',
 'JNCE_2019149_20C00046_V01-raw','JNCE_2019149_20C00048_V01-raw' ), label_visibility='collapsed')

if image_name != '' :
	dic_json = {
		'JNCE_2019149_20C00028_V01-raw':'20-28.json',
		'JNCE_2019149_20C00030_V01-raw':'20-30.json',
		'JNCE_2019149_20C00043_V01-raw':'20-43.json',
		'JNCE_2019149_20C00045_V01-raw':'20-45.json',
		'JNCE_2019149_20C00046_V01-raw':'20-46.json',
		'JNCE_2019149_20C00048_V01-raw':'20-48.json'
	}
	img_json = dic_json[ image_name ]
	image_name += '.png'

	img_json = 'json_files/' + img_json
	image_name = 'images/'+image_name

	#####################################################


	if 'last' not in st.session_state:
		st.session_state['last'] = '#'

	if st.session_state['last'] != image_name :
		from Example1 import func_hello
		func_hello( image_name, img_json )
		st.session_state['last'] = image_name


	def change_brightness(img, value):
		hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
		h, s, v = cv.split(hsv)
		v = cv.add(v,value)
		v[v > 255] = 255
		v[v < 0] = 0
		final_hsv = cv.merge((h, s, v))
		img = cv.cvtColor(final_hsv, cv.COLOR_HSV2BGR)
		return img

	def blur( img, value ) :
		if value <= 0 :
			value = value*-1
			value = value + (value-1)%2
			img = cv.GaussianBlur(img,(value,value),0)
		else :
			value_ = value*0.01
			img = cv.detailEnhance(img, sigma_s=10, sigma_r=value_)
		return img

	####################################################

	link = '/home/elitecallsyou/Desktop/Nasa/Example1.png'
	img = cv.imread(link)

	#####################################################

	#########################################################
	st.write('')
	original_title = "<p style='font-family:Courier; color:orange; font-size: 16px;'>Contrast:</p>"
	st.markdown(original_title, unsafe_allow_html=True)

	brightness = st.slider(label='', min_value=-50, max_value=50, value=0,label_visibility='collapsed')

	#########################################################

	st.write('')
	original_title = "<p style='font-family:Courier; color:Brown; font-size: 16px;'>Blurness:</p>"
	st.markdown(original_title, unsafe_allow_html=True)

	blurness = st.slider(label='', min_value=-20,max_value=20,value=0,label_visibility='collapsed' )

	#########################################################

	img = change_brightness( img,value=brightness )
	img = blur( img,blurness )

	######################################

	# # Saving file and opening through a PIL #
	cv.imwrite( '/home/elitecallsyou/Desktop/Nasa/result.png', img )
	image = Image.open('/home/elitecallsyou/Desktop/Nasa/result.png')

	# Streamlit output image #
	st.image(image, caption=None, width=None,use_column_width=None, clamp=False, channels="RGB", output_format="auto")
