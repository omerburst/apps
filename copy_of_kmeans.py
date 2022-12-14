# -*- coding: utf-8 -*-
"""Copy of kmeans.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_BXmAN0BXauOii6eX1ywopdYU39eOUxN
"""

# import libs
!pip install streamlit
import streamlit as st
import cv2
import numpy as np
import skimage.io as io
from skimage import measure, io, img_as_ubyte, morphology, util, color
import matplotlib.pyplot as plt
from skimage.color import label2rgb, rgb2gray
import numpy as np
import pandas as pd
import cv2
import imutils
#import matplotlib.pyplot as plt

# check versions
#np.__version__

# vars
DEMO_IMAGE = 'demo.png' # a demo image for the segmentation page, if none is uploaded
favicon = 'favicon.png'

# main page
st.set_page_config(page_title='AruCo', page_icon = favicon, layout = 'wide', initial_sidebar_state = 'auto')
st.title('Aruco')

# side bar
st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] . div:first-child{
        width: 350px
    }
    
    [data-testid="stSidebar"][aria-expanded="false"] . div:first-child{
        width: 350px
        margin-left: -350px
    }    
    </style>
    
    """,
    unsafe_allow_html=True,


)

#st.sidebar.title('Segmentation Sidebar')
#st.sidebar.subheader('Site Pages')

# using st.cache so streamlit runs the following function only once, and stores in chache (until changed)
@st.cache()

# take an image, and return a resized that fits our page
def image_resize(image, width=None, height=None, inter = cv2.INTER_AREA):
    dim = None
    (h,w) = image.shape[:2]
    
    if width is None and height is None:
        return image
    
    if width is None:
        r = width/float(w)
        dim = (int(w*r),height)
    
    else:
        r = width/float(w)
        dim = (width, int(h*r))
        
    # resize the image
    resized = cv2.resize(image, dim, interpolation=inter)
    
    return resized

# add dropdown to select pages on left
app_mode = st.sidebar.selectbox('Navigate',
                                  ['About App', 'Segment an Image'])

# About page
if app_mode == 'About App':
    st.markdown('In this app we will segment images using K-Means')
    
    
    # side bar
    st.markdown(
        """
        <style>
        [data-testid="stSidebar"][aria-expanded="true"] . div:first-child{
            width: 350px
        }

        [data-testid="stSidebar"][aria-expanded="false"] . div:first-child{
            width: 350px
            margin-left: -350px
        }    
        </style>

        """,
        unsafe_allow_html=True,


    )

    # add a video to the page
    st.video('https://www.youtube.com/watch?v=6CqRnx6Ic48')


    st.markdown('''
                ## About the app \n
                Hey, this web app is a great one to segment images using K-Means. \n
                There are many way. \n
                Enjoy! Yedidya


                ''')

# # Run image
# if app_mode == 'Segment an Image':
    
#     st.sidebar.markdown('---') # adds a devider (a line)
    
#     # side bar
#     st.markdown(
#         """
#         <style>
#         [data-testid="stSidebar"][aria-expanded="true"] . div:first-child{
#             width: 350px
#         }

#         [data-testid="stSidebar"][aria-expanded="false"] . div:first-child{
#             width: 350px
#             margin-left: -350px
#         }    
#         </style>

#         """,
#         unsafe_allow_html=True,


#     )

#     grayscale = img_as_ubyte(rgb2gray(DEMO_IMAGE))
#     # Load Aruco detector
#     parameters = cv2.aruco.DetectorParameters_create()
#     aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_50)
#     corners, _, _ = cv2.aruco.detectMarkers(DEMO_IMAGE, aruco_dict, parameters=parameters)
#     int_corners = np.int0(corners)
#     cv2.polylines(DEMO_IMAGE, int_corners, True, (0, 255, 0), 30)
#     aruco_area = cv2.contourArea (corners[0])
#     pixel_cm_ratio = 5*5 / aruco_area

#     def segment_image_kmeans(img, k=3, attempts=10): 

#       # Convert MxNx3 image into Kx3 where K=MxN
#       pixel_values  = img.reshape((-1,3))  #-1 reshape means, in this case MxN

#       #We convert the unit8 values to float as it is a requirement of the k-means method of OpenCV
#       pixel_values = np.float32(pixel_values)

#       # define stopping criteria
#       criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
      
#       _, labels, (centers) = cv2.kmeans(pixel_values, k, None, criteria, attempts, cv2.KMEANS_RANDOM_CENTERS)
      
#       # convert back to 8 bit values
#       centers = np.uint8(centers)

#       # flatten the labels array
#       labels = labels.flatten()
      
#       # convert all pixels to the color of the centroids
#       segmented_image = centers[labels.flatten()]
      
#       # reshape back to the original image dimension
#       segmented_image = segmented_image.reshape(img.shape)
      
#       return segmented_image, labels, centers

#     image = DEMO_IMAGE
#     k=3
#     attempts=10
#     segmented_kmeans, labels, centers = segment_image_kmeans(image, k, attempts)

#     st.image(grayscale, use_column_width=True)