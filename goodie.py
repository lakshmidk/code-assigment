# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 16:42:26 2021

@author: hp
"""


def find_goodies(goodies,N,K):
	goodies.sort(key = lambda x: x[1]) 
	result = max(goodies , key = lambda x:x[1])[1]
    
    
	for i in range(N-K+1): 
		price_diff = goodies[i+K-1][1]-goodies[i][1]
		if(price_diff < result):
			result = price_diff
			result_goodie = [goodies[j] for j in range(i,i+K)]
            
	result_goodies_list = [goodie[0]+" : "+str(goodie[1]) for goodie in result_goodie]
    
	result_goodies_list = "Here the goodies that are seleted for distribution are :\n" + "\n".join(result_goodies_list)
    
	price_result = "Difference between the chosen goodie with hishest price and lowest price is "+str(result)
    
	final_result = result_goodies_list +"\n"+ price_result
    
	with open("sample_output.txt","w") as output_file:
		output_file.write(final_result)
            
   
goodies = []

with open("sample_input.txt") as myfile:
	for line in myfile:
		goodie_name, price = line.partition(":")[::2]
		goodies.append((goodie_name,int(price)))
        
N = len(goodies)
K = int(input("Enter Number of Employee's : "))

if(K>0):
	find_goodies(goodies, N, K)