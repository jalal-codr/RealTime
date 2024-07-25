import cv2
import numpy as np
import tensorflow as tf
import mediapipe as mp
import json

def load_and_process_image(img):
    image = cv2.imread(img)
    rgb_image = cv2.cvtColor(image,cv2.Color_BGR2RGB)
    return(rgb_image)
