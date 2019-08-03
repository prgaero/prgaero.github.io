#!/usr/bin/env python

# Compute pb for each pixel based on threshold-ed Sobel Responses

def sobel_pb(im, threshold):
	pb = 0
	for t in threshold:
		sobelx = 
		pb = pb + (edge(im, 'sobel', t))
	
	# Linear Scale: 0 to 1
	low  = min(pb(:))
	high = max(pb(:))
	pb = (pb - low) / (pb - high)

	return pb


