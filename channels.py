#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import cv2

# opencv uses BGR when reading an image
# interesting channels: B G R V L
def get_bgr_channels(image, filename=''):
	if is_monochannel(image):
		return image
	return cv2.split(image)

def get_gray_image(image, filename=''):
	if is_monochannel(image):
		return image
	return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def get_hls_channels(image, filename=''):
	if is_monochannel(image):
		return image
	image = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)
	return cv2.split(image)

def get_hsv_channels(image, filename=''):
	if is_monochannel(image):
		return image
	image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
	return cv2.split(image)

def is_monochannel(image):
	return len(image.shape) < 3