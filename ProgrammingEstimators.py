#from __future__ import division

#Complete the mean function to make it return the mean of a list of numbers

data1=[49., 66, 24, 98, 37, 64, 98, 27, 56, 93, 68, 78, 22, 25, 11]

def mean(data):
    #Insert your code here
    return (sum(data)/len(data))

print(mean(data1))

from math import sqrt #So Sqrt function works


#Complete the median function to make it return the median of a list of numbers
data2=[1,2,5,10,-20]
def median(data):
    #Insert your code here
    sdata=sorted(data)
    m = int((len(data)-1)/2) ##return integer
    #return(m)
    return sdata[m]
    
print(median(data2))


#Complete the mode function to make it return the mode of a list of numbers
data3=[1,2,5,10,-20,5,5]
def mode(data):
    #Insert your code here
    modeF = 0  
    for i in range(len(data)):
        mode1 = data.count(data[i]) # count the nbr of occurrences of element i in list
        if (mode1 > modeF):
            modeF = mode1
            ElemModeF = data[i]
    return ElemModeF
print(mode(data3))


#Complete the variance function to make it return the variance of a list of numbers
data4=[13.04, 1.32, 22.65, 17.44, 29.54, 23.22, 17.65, 10.12, 26.73, 16.43]
#data4=[13.04, 1.32,22.65, 17.44 ]
def variance(data):
    #Insert your code here
    mu = mean(data4)
    ndata = []
    for i in range(len(data)):
        dif = (data[i]- mu)
        ndata.append(dif**2) # Raise to exp 2

    return(mean(ndata))
    
print(variance(data4))


#Complete the stddev function to make it return the standard deviation 
#of a list of numbers
data5=[13.04, 1.32, 22.65, 17.44, 29.54, 23.22, 17.65, 10.12, 26.73, 16.43]
def stddev(data):
    #Insert your code here
    return sqrt(variance(data))
print(stddev(data5))

