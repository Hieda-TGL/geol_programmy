filename = input('Enter name of input file:')
inputfile = open(filename, "r")
string = inputfile.read()
cont_series = []
set1 = set(string)
list1=list(set1)
for n in range(0, len(string)-1):
	m = n+2
	cont_series. append(string[n:m])

import itertools
cont_var = list(map(''.join, itertools.product(list1, repeat=2))) #가능한 접촉들을 리스트로 만들기

contvar_num = []
for i in cont_var:
	contvar_num.append(cont_series.count(i)) #이론적으로 가능한 접촉별 실제 출현회수

dict1 = dict(zip(cont_var,contvar_num))
sort_dict1 = sorted(dict1.items())
dict2 = dict(sort_dict1) #가능한 접촉경계와 그 출현회수를 병합하여 딕셔너리로 만듦

list_cont = list(dict2.keys())
list_freq = list(dict2.values())

def divide_list(l,n): #리스트 l의 길이가 n이면 반복
	for i in range(0, len(l), n):
		yield l[i:i+n]

n = len(set1) #몇개씩 잘라담을지 정하기

result1 = list(divide_list(list_cont, n)) #접촉경계 행렬
result2 = list(divide_list(list_freq, n)) #접촉경계별 출현회수 행렬

import numpy as np
cont_array = np.array(result1)
freq_array = np.array(result2)

import pandas as pd
import scipy.stats as stats
chi, p, dof, expected = stats.chi2_contingency(freq_array)
result3 = stats.chi2_contingency(freq_array)
result4 = freq_array/expected

from pandas import DataFrame
obs_cont = DataFrame(freq_array, columns = sorted(list1), index = sorted(list1))
expt_cont = DataFrame(expected, columns = sorted(list1), index = sorted(list1))
obs_ex_ratio = DataFrame(result4, columns = sorted(list1), index = sorted(list1))
ratio_list = list(result4.reshape(-1))
ratio_dict = dict(zip(sorted(cont_var), ratio_list))

print('----------------------------------------------------------')
print('Observed Contacts')
print(obs_cont)
print('----------------------------------------------------------')
print('Expected Contacts')
print(expt_cont)
print('----------------------------------------------------------')
print('Observed/Expected Ratio')
print(obs_ex_ratio)
print('----------------------------------------------------------')
print('chi = %f' % chi)
print('p = %f' % p)
print('Degree of freedom = %d' % dof)
print('----------------------------------------------------------')

s = input('Save Data? y/n : ')
if s == 'y':
    outputfile = input('Designate path and name of output file:')
    f = open(outputfile, 'w')
    f.write(str(ratio_dict))
    f.close
    print('----------------------------------------------------------')
    print('Data saved')
else:
    print('----------------------------------------------------------')
    print('Project aborted')