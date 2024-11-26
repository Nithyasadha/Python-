'''1)
*
* *
* * *
* * * *
* * * * *
for n in range(1,6):
  print(n * ' *')

for n in range(1,6):
    print(f"{n*' *':<15}")'''

'''2)
* * * * * *
* * * * *
* * * *
* * *
* *
*

for i in range(6,0,-1):
    print(i *'*')'''



'''3)
         *
       * *
     * * *
   * * * *
 * * * * *

for n in range(1,6):
    print(f"{n * ' *':>15}")'''

'''4)
 *             
 * *           
 * * *         
 * * * *       
 * * * * *     
 

for n in range(1,6):
    print(f"{n * ' *':<15}")'''

'''5)
       *       
      * *      
     * * *     
    * * * *    
   * * * * *   '''

'''for i in range(1,6):
   print(f"{i*' *':^5}")'''

#5)
'''
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 

str_=' '
for i in range(1,6):
    str_+=str(i)+' '
    print(str_)'''

'''6)
A
A B
A B C
A B C D
A B C D E

str_=' '
al_='A','B','C','D','E'
for i in range(0,5):
    str_+=al_[i]+' '
    print(str_)'''

'''s_=' '
for ascii_v in range(ord('A'),ord('F')):
   s_+=chr(ascii_v)+' '
   print(s_)'''

'''7)
A B C D E
A B C D
A B C
A B
A

str_=' '
al_='A','B','C','D','E'
for i in range(len(al_),0,-1):
    print(' '.join(al_[:i]))'''

'''st_=' '
for i in range(5,0,-1):
    for j in range(i):
        st_=chr(ord('A')+j)
        print(st_,end=' ')
    print()'''

#i=5,4,3,2,1(5,1)
#i=5,j=(0,4),j=0,1,2,3,4
#st_=chr(ord('a')+1
    #=chr(97+0)
    #=chr(97+1)......
    

'''8)
*
* * 
*
* * * 
*
* * * * 
*
* * * * * 

star_=5
for i in range(1,star_+1):
    print('* '*i)
    if i!=star_:
        print('*')'''

'''for i in range(1,6):
    print(' *')
    print(i*' *')'''



                                    #----->Other Pattern<---------
#1)A
'''
*****      
*    *
*****
*    *
*    *'''

'''n=5
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or j==n-1:
            print('*',end=' ')
        elif i==2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''

#2)B
'''
* * * * * 
*       * 
* * * * * 
*       * 
* * * * * '''
'''n=5
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or j==n-1:
            print('*',end=' ')
        elif i==2 or i==4:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''

#3)C
'''
* * * * * 
*         
*         
*         
* * * * * '''
'''n=5
for i in range(n):
    for j in range(n):
        if i==0 or j==0 :
            print('*',end=' ')
        elif i==4:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''

#4)D
'''
* * * * * 
*       * 
*       * 
*       * 
* * * * * '''
'''n=5
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or j==n-1:
            print('*',end=' ')
        elif  i==4:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''

#5)E
'''
* * * * * 
*         
* * * * * 
*         
* * * * * '''
'''n=5
for i in range(n):
    for j in range(n):
        if i==0 or j==0 :
            print('*',end=' ')
        elif i==2 or i==4:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''

#6)F
'''
* * * * * 
*         
* * * * * 
*         
* '''
'''n=5
for i in range(n):
    for j in range(n):
        if i==0 or j==0 :
            print('*',end=' ')
        elif i==2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''

#7)H
'''
*       * 
*       * 
* * * * * 
*       * 
*       * '''
'''n=5
for i in range(n):
    for j in range(n):
        if  j==0 or j==n-1:
            print('*',end=' ')
        elif i==2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''
#8)G
'''
* * * * * 
*         
*   * * * 
*   *   * 
* * *   * '''
'''n=5
for i in range(n):
    for j in range(n):
        if i==0 or j==0:
            print('*',end=' ')
        elif(i==2 and j==2)or(i==2 and j==3):
            print('*',end=' ')
        elif i==2 and j==4:
            print('*',end=' ')
        elif(i==3 and j==2) or(i==3 and j==4):
            print('*',end=' ')
        elif(i==4 and j==1) or(i==4 and j==4) or (i==4 and j==2):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''

#9)I
'''
* * * * * 
    *     
    *     
    *     
* * * * * 
'''
'''n=5
for i in range(n):
    for j in range(n):
        if  i==0 or i==n-1:
            print('*',end=' ')
        elif j==2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''

#10)J
'''
* * * * * 
    *     
    *     
*   *     
* * * '''   

'''n=5
for i in range(n):
    for j in range(n):
        if  i==0 or j==2:
            print('*',end=' ')
        elif (i==0 and j==0) or(i==4 and j==1):
            print('*',end=' ')
        elif(j==4 and j==2) or (i==3 and j==0):
            print('*',end=' ')
        elif i==4 and j==0:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''


#11)L
'''
*         
*         
*         
*         
* * * * * '''
'''n=5
for i in range(n):
    for j in range(n):
        if i==n-1:
            print('*',end=' ')
        elif j==0:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''

#12)K
'''
*       * 
*     *   
* *       
*     *   
*       * '''
'''n=5
for i in range(n):
    for j in range(n):
        if ( j==0 ):
            print('*',end=' ')
        elif (i==0 and j==n-1):
            print('*',end=' ')
        elif (i==n-1 and j==n-1):
            print('*',end=' ')
        elif (i==1 and j==n-2):
            print('*',end=' ')
        elif (i==n-2 and j==n-2):
            print('*',end=' ')
        elif (i==2 and j==1):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''


#13)M
'''
*       * 
* *   * * 
*   *   * 
*       * 
*       * '''
'''n=5
for i in range(n):
    for j in range(n):
        if ( j==0 or j==n-1):
            print('*',end=' ')
        elif (i==1 and j==1):
            print('*',end=' ')
        elif (i==1 and j==3):
            print('*',end=' ')
        elif (i==2 and j==2):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''

#14)P
'''
* * * * * 
*       *  
* * * * * 
*         
*   '''
'''n=5
for i in range(n):
    for j in range(n):
        if ( j==0 or i==2 or i==0):
            print('*',end=' ')
        elif(i==1 and j==n-1):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''

#15)N
'''
*       * 
* *     * 
*   *   * 
*     * * 
*       * 
'''
'''n=5
for i in range(n):
    for j in range(n):
        if ( j==0 or j==n-1):
            print('*',end=' ')
        elif (i==1 and j==1):
            print('*',end=' ')
        elif(i==2 and j==2):
            print('*',end=' ')
        elif(i==3 and j==3):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''









            

        






