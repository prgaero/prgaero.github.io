#!/usr/bin/env python

# Compute pb for each pixel based on threshold-ed Canny Responses

def canny_pb(im, threshold, sigma):
	pb = 0
	for t in threshold:
		for s in sigma:
			pb = pb + (edge(im, 'canny', t, s))
	
	# Linear Scale: 0 to 1
	low  = min(pb(:))
	high = max(pb(:))
	pb = (pb - low) / (pb - high)

	return pb
