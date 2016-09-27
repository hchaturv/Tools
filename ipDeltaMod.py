'''
Authors :    Harsh Chaturvedi/ Kashif Memon
Usecase:    This script was originally wriiten
            for a project. The aim was to read values written
            in a file one by one into sets of 99. A set of
            features (Average, Geometric Mean, Harmonic Mean,
            Standard Deviation and Variance) are then calculated
            on every set. These features are then written to a csv
            which is used to extract meaningful inferences. The csvs created
            by this file can be directly fed to tools like Weka.
Usage:      python responseTimeDelta.py <txt file with response time values> <target csv file> <size of each set> <label to be given>


'''

import numpy as np
import math
import sys

def gmean(a, axis=0, dtype=None):
    if not isinstance(a, np.ndarray):  # if not an ndarray object attempt to convert it
        log_a = np.log(np.array(a, dtype=dtype))
    elif dtype:  # Must change the default dtype allowing array type
        if isinstance(a,np.ma.MaskedArray):
            log_a = np.log(np.ma.asarray(a, dtype=dtype))
        else:
            log_a = np.log(np.asarray(a, dtype=dtype))
    else:
        log_a = np.log(a)
    return np.exp(log_a.mean(axis=axis))

#Calculate feature values for a batch of 100 samples
def featureCalc(values):
    len1 = len(values)
    mean = np.mean(values)
    stdev = np.std(values)
    var = np.var(values)
    har_mean = len1 / np.sum(1.0/val for val in values)
    geo_mean = gmean(values)
    csv = open(secondarg,'a')
    csv.write(fourtharg + ', '+str(mean) + ', ' + str(stdev) + ', ' + str(var) + ', ' + str(har_mean) + ', ' + str(geo_mean) + '\n')
    csv.close
    print 'Mean: ', mean
    print 'Std Dev: ', stdev
    print 'Variance: ', var
    print 'Harmonic Mean: ', har_mean
    print 'Geometric Mean: ', geo_mean
    return


firstarg = str(sys.argv[1]) # The input text file with numbers in it.
secondarg = str(sys.argv[2]) # The target csv file to which the feature sets have to be written
thirdarg = int(str(sys.argv[3])) # The size of each set.
fourtharg = str(sys.argv[4]) # The label to be given to the set.
file2 = open(secondarg,'w')
file2.write('type,1,2,3,4,5\n')
file2.close()

# The following code will split the file in batches of 100 and will calculate the feature
# values on them
# The function featureCalc does this part
# Once 100 values are read, they are fed to featureCalc which calculates the values and
# appends them to the csv file.
# Once this is done, the array is flushed and the count is reset.

file1 = open (firstarg,'r')
values = []
count = 0
setCount = 1
line = '1'
line_temp = 0

while line != '':
    try:
        line = (file1.readline())
        sys.stdout.write(line)
        #line = line.rstrip()
        if count > thirdarg:
            #print "Count became greater than 999, calling featureCalc"
            featureCalc(values)
            count = 0
            values = []
            setCount += 1
        if line == '' and setCount > 99:
            break
        if not line == '\n':
            line_temp = float(line)
            if not line_temp == 0:
                values.append (line_temp)
                print count
                print setCount
                count += 1
    except:
        print "Found a non number %s " % line
if count > 0:
    featureCalc(values)
