#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 10:54:12 2017

@author: kendradavis
"""

import glob
import os
import shutil

def prepro(basedir):
    for item in glob.glob(os.path.join(basedir, 'sub-*','func','sub-*_task-bart_bold.nii.gz')):
        input=item
        output_path=item.split('.')[0]
        output=output_path+('_brain')
        os.system("/usr/local/fsl/bin/bet %s %s -F"%(input, output))
        pdb.set_trace()
def main():
    basedir = '/Users/kendradavis/Desktop/FMRI/SUBJECT'
    prepro(basedir)
main()


def prepro(basedir):
    #do something cool 
    print ('hello data in the path '+basedir)
def main():
    #load in all the global varaibles prepro needs, right now this is just the path to the data 
    basedir = '/Users/kendradavis/Desktop/FMRI/SUBJECT'
    prepro(basedir) #call prepro to do cool things
main()#call main to execute all our globals then run our prepro function