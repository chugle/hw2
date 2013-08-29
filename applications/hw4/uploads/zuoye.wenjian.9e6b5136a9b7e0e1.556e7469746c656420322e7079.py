#! /usr/bin/env python
#coding=utf-8
import os

files=os.listdir(os.getcwd())
print files
l=[1,23,3]
htmlfile= filter(lambda f:os.path.splitext(f)[1]=='html',files)
print htmlfile
