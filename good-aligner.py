#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 00:13:35 2020

@author: ethanjohnsong
"""

from __future__ import print_function
import cv2
import numpy as np
from shutil import copyfile


MAX_MATCHES = 1000
GOOD_MATCH_PERCENT = 0.15


def alignImages(im1, im2):

  # Convert images to grayscale
  im1Gray = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
  im2Gray = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)
  
  # Detect ORB features and compute descriptors.
  orb = cv2.ORB_create(MAX_MATCHES)
  keypoints1, descriptors1 = orb.detectAndCompute(im1Gray, None)
  keypoints2, descriptors2 = orb.detectAndCompute(im2Gray, None)
  
  # Match features.
  matcher = cv2.DescriptorMatcher_create(cv2.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING)
  matches = matcher.match(descriptors1, descriptors2, None)
  
  # Sort matches by score
  matches.sort(key=lambda x: x.distance, reverse=False)

  # Remove not so good matches
  numGoodMatches = int(len(matches) * GOOD_MATCH_PERCENT)
  matches = matches[:numGoodMatches]


  # Draw top matches
  #imMatches = cv2.drawMatches(im1, keypoints1, im2, keypoints2, matches, None)
  #cv2.imwrite("matches.jpg", imMatches)
  
  # Extract location of good matches
  points1 = np.zeros((len(matches), 2), dtype=np.float32)
  points2 = np.zeros((len(matches), 2), dtype=np.float32)

  for i, match in enumerate(matches):
    points1[i, :] = keypoints1[match.queryIdx].pt
    points2[i, :] = keypoints2[match.trainIdx].pt

  """
  # Find homography
  h, mask = cv2.findHomography(points1, points2, cv2.RANSAC)

  # Use homography
  height, width, channels = im2.shape
  im1Reg = cv2.warpPerspective(im1, h, (width, height))
  """

  h, rigid_mask = cv2.estimateAffinePartial2D(points1, points2)

  height, width, channels = im2.shape
  im1Reg = cv2.warpAffine(im1, h, (width, height))

  return im1Reg, h


if __name__ == '__main__':
  
  path = input("What is the foldername? ")
    
  os.mkdir(path + "/aligned/")
    
  refFilename = path + "/1.JPG"
  print("Reading reference image : ", refFilename)
  imReference = cv2.imread(refFilename, cv2.IMREAD_COLOR)
  copyfile(path + "/1.JPG", path + "/aligned/aligned-1.JPG")
  
  imFilename = path + "/2.JPG"
  print("Reading image to align : ", imFilename);  
  im = cv2.imread(imFilename, cv2.IMREAD_COLOR)
  print("Aligning images ...")
  
  imReg, h = alignImages(im, imReference)
  
  outFilename = path + "/aligned/aligned-2.JPG"
  print("Saving aligned image : ", outFilename); 
  cv2.imwrite(outFilename, imReg)
  
  refFilename = path + "/aligned/aligned-2.JPG"
  print("Reading reference image : ", refFilename)
  imReference = cv2.imread(refFilename, cv2.IMREAD_COLOR)
  
  imFilename = path + "/3.JPG"
  print("Reading image to align : ", imFilename);  
  im = cv2.imread(imFilename, cv2.IMREAD_COLOR)
  print("Aligning images ...")
  
  imReg, h = alignImages(im, imReference)
  
  outFilename = path + "/aligned/aligned-3.JPG"
  print("Saving aligned image : ", outFilename); 
  cv2.imwrite(outFilename, imReg)
  
  refFilename = path + "/aligned/aligned-3.JPG"
  print("Reading reference image : ", refFilename)
  imReference = cv2.imread(refFilename, cv2.IMREAD_COLOR)
  
  imFilename = path + "/4.JPG"
  print("Reading image to align : ", imFilename);  
  im = cv2.imread(imFilename, cv2.IMREAD_COLOR)
  print("Aligning images ...")
  
  imReg, h = alignImages(im, imReference)
  
  outFilename = path + "/aligned/aligned-4.JPG"
  print("Saving aligned image : ", outFilename); 
  cv2.imwrite(outFilename, imReg)
  
  refFilename = path + "/aligned/aligned-4.JPG"
  print("Reading reference image : ", refFilename)
  imReference = cv2.imread(refFilename, cv2.IMREAD_COLOR)
  
  imFilename = path + "/5.JPG"
  print("Reading image to align : ", imFilename);  
  im = cv2.imread(imFilename, cv2.IMREAD_COLOR)
  print("Aligning images ...")
  
  imReg, h = alignImages(im, imReference)
  
  outFilename = path + "/aligned/aligned-5.JPG"
  print("Saving aligned image : ", outFilename); 
  cv2.imwrite(outFilename, imReg)
  
  refFilename = path + "/aligned/aligned-5.JPG"
  print("Reading reference image : ", refFilename)
  imReference = cv2.imread(refFilename, cv2.IMREAD_COLOR)
  
  imFilename = path + "/6.JPG"
  print("Reading image to align : ", imFilename);  
  im = cv2.imread(imFilename, cv2.IMREAD_COLOR)
  print("Aligning images ...")
  
  imReg, h = alignImages(im, imReference)
  
  outFilename = path + "/aligned/aligned-6.JPG"
  print("Saving aligned image : ", outFilename); 
  cv2.imwrite(outFilename, imReg)
    
    
  """
  # Read reference image
  refFilename = "3.JPG"
  print("Reading reference image : ", refFilename)
  imReference = cv2.imread(refFilename, cv2.IMREAD_COLOR)
  
  imFilename = "2.JPG"
  print("Reading image to align : ", imFilename);  
  im = cv2.imread(imFilename, cv2.IMREAD_COLOR)
  print("Aligning images ...")
  
  imReg, h = alignImages(im, imReference)
  
  outFilename = "aligned2/aligned-2.JPG"
  print("Saving aligned image : ", outFilename); 
  cv2.imwrite(outFilename, imReg)
  
  imFilename = "4.JPG"
  print("Reading image to align : ", imFilename);  
  im = cv2.imread(imFilename, cv2.IMREAD_COLOR)
  print("Aligning images ...")
  
  imReg, h = alignImages(im, imReference)
  
  outFilename = "aligned2/aligned-4.JPG"
  print("Saving aligned image : ", outFilename); 
  cv2.imwrite(outFilename, imReg)
  
  refFilename = "aligned2/aligned-2.JPG"
  print("Reading reference image : ", refFilename)
  imReference = cv2.imread(refFilename, cv2.IMREAD_COLOR)
  
  imFilename = "1.JPG"
  print("Reading image to align : ", imFilename);  
  im = cv2.imread(imFilename, cv2.IMREAD_COLOR)
  print("Aligning images ...")
  
  imReg, h = alignImages(im, imReference)
  
  outFilename = "aligned2/aligned-1.JPG"
  print("Saving aligned image : ", outFilename); 
  cv2.imwrite(outFilename, imReg)
  
  refFilename = "aligned2/aligned-4.JPG"
  print("Reading reference image : ", refFilename)
  imReference = cv2.imread(refFilename, cv2.IMREAD_COLOR)
  
  imFilename = "5.JPG"
  print("Reading image to align : ", imFilename);  
  im = cv2.imread(imFilename, cv2.IMREAD_COLOR)
  print("Aligning images ...")
  
  imReg, h = alignImages(im, imReference)
  
  outFilename = "aligned2/aligned-5.JPG"
  print("Saving aligned image : ", outFilename); 
  cv2.imwrite(outFilename, imReg)
  """