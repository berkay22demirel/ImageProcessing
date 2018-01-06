
# coding: utf-8

# In[ ]:

import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.misc import imsave
get_ipython().magic('matplotlib inline')


def convert_RGB_to_monochrome_BW(image_1,threshold=100):
    img_1=plt.imread(image_1)
    img_2=np.zeros((img_1.shape[0],img_1.shape[1]))
    for i in range(img_2.shape[0]):
        for j in range(img_2.shape[1]):
            if(img_1[i,j,0]/3+img_1[i,j,1]/3+img_1[i,j,1]/3)>threshold:
                img_2[i,j]=1
            else:
                img_2[i,j]=0
    return img_2


def create_mask_internal():
    i_m_1=np.array([[1,0],[0,0]])
    i_m_2=np.array([[0,1],[0,0]])
    i_m_3=np.array([[0,0],[1,0]])
    i_m_4=np.array([[0,0],[0,1]])
    i_m_l=[i_m_1,i_m_2,i_m_3,i_m_4]
    
    return i_m_l

def create_mask_external():
    
    e_m_1=np.array([[0,1],[1,1]])
    e_m_2=np.array([[1,0],[1,1]])
    e_m_3=np.array([[1,1],[0,1]])
    e_m_4=np.array([[1,1],[1,0]])
    e_m_l=[e_m_1,e_m_2,e_m_3,e_m_4]
    
    return e_m_l

def count_object(image_name_with_path,threshold=150):
    img_file_1=image_name_with_path
    img_file_2=convert_RGB_to_gray_level(img_file_1)
    img_file_3=convert_RGB_to_monochrome_BW(img_file_1,threshold)
    image=img_file_3
    c_1=0
    c_2=0   
    m,n=image.shape
    for i in range(m-1):
        for j in range(n-1):
            for mask in create_mask_internal():
                if False not in (img_file_3[i:i+2,j:j+2]==mask):
                    #print("e mask bulundu")
                    c_1=c_1+1
            for mask in create_mask_external():
                if False not in (img_file_3[i:i+2,j:j+2]==mask):
                    #print("i mask bulundu")
                    c_2=c_2+1
    number_of_objects=math.fabs((c_2-c_1)/4)
    print("resimde toplam T sayısı : ",number_of_objects)
    return number_of_objects

def convert_RGB_to_gray_level(image_1):
    
    img_1=plt.imread(image_1)
    
    img_2=np.zeros((img_1.shape[0],img_1.shape[1]))
    
    for i in range(img_2.shape[0]):
        
        for j in range(img_2.shape[1]):
            
            img_2[i,j]=img_1[i,j,0]/3+img_1[i,j,1]/3+img_1[i,j,1]/3
    return img_2

image_file_1=r"GG.jpg"
image_file_2=r"GG.jpg"

image_file_1=convert_RGB_to_monochrome_BW(image_file_1,threshold=100)
plt.imshow(image_file_1,cmap='gray')
plt.show()
count_object(image_file_2)

