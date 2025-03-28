# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 07:56:41 2025
@author: LENOVO L460

"""

class gauss_jordan():
    def __init__(self,n,v):
        self.n=int(n)
        self.v=int(v)

    def receive_elements(self):
        '''n,v where n is the number of rows and v is the number of columns'''
        print('lets represent the matrix with A')
        import numpy as np
        global mat
        mat=np.zeros((self.n,self.v))
        for x in range(self.n):
            for y in range(self.v):
                mat[x][y]=int(input('Enter row the value of the row element a{}{}: '.format(x+1,y+1)))
        
    
    def row_reduction(self):
        for x in range(self.n):
            y=x
            if mat[x][y]==0 :
                for rik in range(0,self.n):
                    if mat[rik][x] != 0:
                        mat[[x,rik]]=mat[[rik,x]]
                        mat[x]=mat[x]/mat[x][y]
                        print('\n\t-----{}-----\n'.format(mat))
                        if x==0:
                            for rows in range((self.n)-1):
                                column=0
                                if mat[rows+1][column] != 0:
                                    zero_factor=mat[rows+1][column]/mat[rows-rows][column]
                                    mat[rows+1]=mat[rows+1]-(zero_factor*mat[rows-rows])
                                
                                else:
                                    pass
                                    
                                    
                        elif x !=0 :
                            for rows in range(x):
                                zero_factor_1=mat[rows][x]/mat[x][x]  
                                mat[rows][x:]=mat[rows][x:]-(zero_factor_1*(mat[x][x:]))  
                                print('\n\t-----{}-----\n'.format(mat))
                                
                            for blows in range(x,(self.n)-1):
                                if mat[blows+1][x] != 0 :
                                    zero_factor_2=mat[blows+1][x]/mat[x][x]
                                    mat[blows+1][x:]=(mat[blows+1][x:])-(zero_factor_2*mat[x][x:])
                                    print('\n\t-----{}-----\n'.format(mat))
                        break
            
            if mat[x][y]!=0 :
                mat[x]=mat[x]/mat[x][y]
                print('--------{}-----\n'.format(mat))
                if x==0:
                    for rows in range((self.n)-1):
                        column=0
                        if mat[rows+1][column] != 0:
                            zero_factor=mat[rows+1][column]/mat[rows-rows][column]
                            mat[rows+1]=mat[rows+1]-(zero_factor*mat[rows-rows])
                        print('\n\t-----{}-----\n'.format(mat))
                            
                elif x !=0 :
                    for rows in range(x):
                        zero_factor_1=mat[rows][x]/mat[x][x]  
                        mat[rows][x:]=mat[rows][x:]-(zero_factor_1*(mat[x][x:]))  
                        print('\n\t-----{}-----\n'.format(mat))
                        
                    for blows in range(x,(self.n)-1):
                        if mat[blows+1][x] != 0 :
                            zero_factor_2=mat[blows+1][x]/mat[x][x]
                            mat[blows+1][x:]=(mat[blows+1][x:])-(zero_factor_2*mat[x][x:])
                            print('\n\t-----{}-----\n'.format(mat))
                        else :
                            pass
                    
        list=mat[:,((self.v)-1)]
        for index,items in enumerate(list):
            print('X{}={}'.format(index+1,items))                
        return mat