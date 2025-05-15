import streamlit as st
from img_functions import *
from PIL import Image
import cv2
import numpy as np


# Functio untuk header
def header(image):
    st.header("Input")       
    st.image(image)

def my_data():
    st.subheader("Arya Wiratama (312310224)")

def main():
    st.header("Welcome to image transformation with Opencv")
    my_data()
    file_uploaded = st.file_uploader("Please upload an image file....", type=['jpg', 'png', 'jpeg'])
    if file_uploaded is not None:
        image = Image.open(file_uploaded)
        image_cv2 = np.array(image)
        image_cv2 = cv2.cvtColor(image_cv2, cv2.COLOR_BGR2BGRA)

        
        option = st.selectbox("Select the transformation you want to apply", ('Select', 'Affine', 'Rotation', 'Flipping'))
        
        if option == 'Select':
            st.write("Pilih salah satu antara Affine, Rotation, Flipping")
            pass
        
        elif option == 'Affine':
            st.write("Yout Selected: ", option)
            header(image)
            
            st.markdown("Image after **affline transformation**:wave:...")
            st.image(warpaffine((image_cv2)))

        elif option == 'Rotation':
            st.write("Yout Selected: ", option)
            header(image)
            
            ang = st.slider("Select the angle of rotation...", min_value=0, max_value=360)
            st.write(f"Slider value : {ang} degree")

            st.markdown("Image after **Rotation**:wave:...")
            st.image(img_rotation(image_cv2, ang))

        elif option == 'Flipping':
            st.write("Yout Selected: ", option)
            header(image)
            
            flip_out = st.selectbox("Select an option: ", ('Select', 0, 1, -1))
            st.write("You selected : ", flip_out)

            if flip_out == 'Select':
                pass
            else: 
                st.header("Flipped image....")
                st.image(img_flipping(image_cv2, flip_out))

        else:
            pass
        
        
if __name__ == "__main__":
    main()



