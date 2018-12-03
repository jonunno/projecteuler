# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 13:23:06 2018

Problem 31 from project euler.org

Worked on 
2018/09/25 (solved but I can make the code a bit neater (see r2))

@author: Jon
"""

init_total = 200


comb = 0


for i in range(0,init_total+1,200):
    
    if i == init_total:
        comb += 1
        break
    else:
        for j in range(i,init_total+1,100):
            
            if j == init_total:
                comb += 1
                break
            else:
                for k in range(j,init_total+1,50):
                    
                    if k == init_total:
                        comb += 1
                        break
                    else:
                        for l in range(k,init_total+1,20):
                            
                            if l == init_total:
                                comb += 1
                                break
                            else:
                                for m in range (l,init_total+1,10):
                                    
                                    if m == init_total:
                                        comb += 1
                                        break
                                    else: 
                                        for n in range(m,init_total+1,5):
                                            
                                            if n == init_total:
                                                comb += 1
                                                break
                                            else: 
                                                for o in range(n,init_total+1,2):
                                                    
                                                    if o == init_total:
                                                        comb += 1
                                                        break
                                                    else: 
                                                        for p in range(o,init_total+1,1):
                                                            if p == init_total:
                                                                comb += 1
                                                                break
                                    
                                    
print(comb)

#
#
#for i in range(0,init_total+1,200):
#    test_total = 0
#    
#    test_total += i
#    if test_total + 200 > init_total:
#        comb += 1
#        break
#    print(test_total)
#    for j in range(0,init_total+1,100):
#        
#        if test_total + 100 > init_total:
#            comb += 1
#            break
#        print(test_total)
#        for k in range(0,init_total+1,50):
#        
#            if test_total + 50 > init_total:
#                comb += 1
#                break
#            print(test_total)
#            for l in range(0,init_total+1,20):
#            
#                if test_total + 20 > init_total:
#                    comb += 1
#                    break
#                print(test_total)
#                for m in range(0,init_total+1,10):
#                
#                    if test_total + 10 > init_total:
#                        comb += 1
#                        break
#                    """
#                    for n in range(0,init_total+1,5):
#                    
#                        if test_total + 5 > init_total:
#                            comb += 1
#                            break
#                        
#                        for o in range(0,init_total+1,2):
#                        
#                            if test_total + 2 > init_total:
#                                comb += 1
#                                break
#                            
#                            for p in range(0,init_total+1,1):
#                            
#                                if test_total + 1 > init_total:
#                                    comb += 1
#                                    break
#                            
#                                test_total += 1
#                            test_total += 2                    
#                        test_total += 5
#                        """
#                    test_total += 10
#                test_total += 20
#            test_total += 50
#        test_total += 100
            
#            for l in range(0,init_total+1,20):
#                
#                for m in range(0,init_total+1,10):
#                    
#                    for n in range(0,init_total+1,5):
#                        
#                        for o in range(0,init_total+1,2):
#                            
#                            for p in range(0,init_total+1,1):
    