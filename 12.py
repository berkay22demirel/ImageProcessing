
# coding: utf-8

# In[ ]:

import matplotlib.pyplot as plt
import numpy as np
import math

def get_shear_matrix_for_factor_x(factor_x: int):
    shear_m=np.empty((2,2),np.float)
    shear_m[0,:] = np.array([1,factor_x])
    shear_m[1, :] = np.array([0,1])
    return shear_m

def get_rotation_matrix_for_angle(angle: float):
    theta = angle
    rotation_matrix = np.array([[math.cos(theta), -math.sin(theta)], [math.sin(theta), math.cos(theta)]], np.float)

    return rotation_matrix
def get_new_point(point: tuple, angle: float):
    """
    :param point:  a point in 2D, with coordinates x, y
    :param angle:  in radians
    :return: tuple representing a point with ratoted coordinates
    """
    rotation_matrix = get_rotation_matrix_for_angle(angle)

    point_vector=np.empty((2,1),float)

    point_vector[0,0]=point[0]
    point_vector[1,0]=point[1]

    new_point = np.matmul(rotation_matrix, point)

    x = int(new_point[0])
    y = int(new_point[1])

    return (x,y)

def display_plot(points):
    """
    :param points: np.matrix
    """

    point_list_x = points[:, 0]  #
    point_list_y = points[:, 1]  # [

    plt.plot(point_list_x, point_list_y)
    plt.show()
def get_my_T():
    points=np.empty((9,2),np.float)
    points[:,0] = np.array([20,25,25,35,35,10,10,20,20])
    points[:,1] = np.array([ 0, 0,30,30,35,35,30,30, 0])

    return points

def display_three_letters_on_same_plot(p_1: np.matrix , p_2: np.matrix, p_3: np.matrix):
    plt.plot(p_1[:,0], p_1[:,1],color="red")
    plt.plot(p_2[:, 0], p_2[:, 1], color="yellow")
    plt.plot(p_3[:, 0], p_3[:, 1], color="green")
    plt.xlim([-100,100])
    plt.ylim([-100,100])
    plt.show()


def display_two_letters_on_same_plot(p_1: np.matrix , p_2: np.matrix):
    plt.plot(p_1[:,0], p_1[:,1],color="red")
    plt.plot(p_2[:, 0], p_2[:, 1], color="yellow")
    plt.show()
def display_points(points):
    plt.plot(points[:,0], points[:,1])
    plt.show()

def rotate_a_letter_by_angle(letter:np.matrix,angle:np.float):
    m,n=letter.shape
    new_points = np.empty((m,n),np.float)
    for i in range(m):
        new_points[i,:] = get_new_point(letter[i,:],angle)
    return new_points

def shear_a_letter_by_factor_x(letter:np.matrix,factor_x:np.int):
    m,n=letter.shape
    new_letter = np.empty((m,n),np.float)
    shear_matrix=get_shear_matrix_for_factor_x(factor_x)
    for i in range(m):
        new_letter[i,:] = np.matmul(shear_matrix,letter[i,:])

    return new_letter


p=get_my_T()
p_1=rotate_a_letter_by_angle(get_my_T(), np.pi/2)
p_2=shear_a_letter_by_factor_x(p,1)
# display_two_letters_on_same_plot(p,p_2)
display_three_letters_on_same_plot(p,p_1,p_2)
# display_points(p_2)

