# import library
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# make dictionary for selection of movies
d = {
    1 : 'movie_1',
    2 : 'movie_2',
    3 : 'movie_3',
    4 : 'movie_4',
    5 : 'movie_5'
}

# make dictionary for select available timings
time_m = {
    'a' : '8:00 AM',
    'b' : '9:30 AM',
    'c' : '12:00 PM',
    'd' : '2:00 PM',
    'e' : '5:00 PM',
    'f' : '8:30 PM',
    'g' : '10:00 PM'
}

# make dictionary for select theater
place = {
    1 : 'INOX',
    2 : 'RAJHANS',
    3 : 'PVR'
}


# making function to movie selection
# it will select by user
def select_movie():
    print("available movies: ")
    print('---------------------')
    print('''
1 = movie_1
2 = movie_2
3 = movie_3
4 = movie_4
5 = movie_5
      ''')

    
    n = input("which movie?")    # ask user to select movie
    n = int(n)
    return n                     # return that key value inside dictionary d


# function for select timings
def timings(m):
    print("available timings for movie: {}".format(m))
    print('-------------------------------------------')
    print(''' 
    a = 8:00 AM , b = 9:30 AM
    c = 12:00 PM , d = 2:00 PM, e = 5:00 PM, f = 8:30 PM, g = 10:00 PM 
    ''')
    time = input("select the time slot for movie: ")
    # user enter timings with appropriate key of dictionary time_m
    
    return time # will return key


def theater():
    # this all for indication to user
    print("theater: ")
    print('-----------------------')
    print('''
    1 : INOX
    2 : RAJHANS
    3 : PVR ''')
    t = input("which theater: ")  # will ask user to enter theater code
    t = int(t)                    # by default string than convert it into int
    return t                      # return key value enter by user


def sitting():
    # this will display setting arrangement to user
    print('R. * * * * * * * * * *')
    print('A. - - - - - - - - - -')
    print('B. - - - - - - - - - -')
    print('C. - - - - - - - - - -')
    print('D. - - - - - - - - - -')
    print('E. - - - - - - - - - -')
    print('F. - - - - - - - - - -')
    print(' - - - -Screen This Side - - - - - -')
    print('select row: ')
    # 3 different types of seats
    # with different price
    print("A-c price: 200Rs.")
    print("D-F price: 150Rs.")
    print('R : 300')
    # 2 different type of seat catogary 
    print('which catagory? ')
    print('1 == recliner')
    print('2 == simple')
    cat = int(input())
    while(True):
        if(cat == 1):              # if user enter 1 than store recliner catagory
            category = 'recliner'  # and it will directly select R row
            row = 'R'
            return row,category
            break
        else:                      # else user select 2 than simple catagory
            category = 'simple'
            row = input('select row: ')
            if(row == 'R'):        
                # here in simple catagory if user enter R roW(for recliner)
                # tha will show error and ask you to purchase recliner
                # if user say yes than it will provide R row
                # and say no than again ask for row selection
                print('**cant select R row**')
                print('** THIS FOR RECLINER** ')
                print('do you want recliner seat?????')
                c_seat = input()
                if(c_seat == 'yes'):
                    category = 'recliner'
                    row = 'R'
                    return row,category
                    break
                else:
                    pass
                    
            else:
                return row,category
                break
                
                        

# function for calculation of price and ticket s
# take row as the argument in function
def tickets(r):
    
    print('selsected row: {}'.format(r)) # it will show which row user selected
    print('')    
    print('how many tickets do you want to buy?')
    num = int(input())     # ask user to enter tickes quntity
    
    # according to user select the row
    # use condition to calculate the price bcz of different price
    if(r>='A' and r<='C'):
        amount = 200
        t_amount = num*amount   # multiply tickets number with price
    elif(r>='D' and r<='F'):
        amount = 150
        t_amount = num*amount
    elif(r == 'R'):
        amount = 300
        t_amount = num*amount
        
    return num,amount,t_amount # return multiple variable 
        
       
 # make function to shoe all details of move and payment details   
def movie_details(m,t,th,num,am,tm,R,c):
    print('')
    print("MOVIE DETAILS: ")
    print('---------------')
    print("movie  : {}".format(m))
    print('time   : {}'.format(t))
    print('theater: {}'.format(th))
    print('seat catagory : {}'.format(c))
    print('ROW: {}'.format(R))
    print('')   
    print('tickets: {}'.format(num))
    print('total amount: ')
    print('{}X{}'.format(num,am))
    print(tm)
    

# select movie
# -----------------------------------------------------------------

# movie rating
#m = np.array(['movie_1','movie_2','movie_3','movie_4','movie_5'])
#r = np.array([92.7,98.0,99.5,87.5,90.0])
#plt.bar(m,r)
#plt.xlabel('MOVIE',color='r')
#plt.ylabel('RATING',color='r')
#plt.grid()
#plt.show()

n = select_movie()       # call function to movie selection
movie = d.get(n)         # it will store value with appropriate key
list1 = d.keys()         # list1 will store available movie codes        
list1 = list(list1)

# loop
''' making this loop if user will select movie is not
    available than it will show error and ask you to select
    again and you will say no than exit the progrrame
'''
while(True):
    # if user select availbale movie than will store
    if(n in list1):
        print('movie: ',d[n]) 
        break
    else:
        print('this movie is not available!!')
        choice = input('CAN I SHOW YOU AVAILABLE MOVIE LIST?')
        if(choice == 'yes'):
            n = select_movie()
            movie = d.get(n)
        else:
            print('thanks for visiting this site!!!!')
            exit(0)
    

# select timings
# -------------------------------------------------------------------
t = timings(movie)      # t will store key with selected time
time = time_m.get(t)    # time variable store value with key
list2 = time_m.keys()
list2 = list(list2)

# make loop for error
# if user enter time which not available than it will throw error
# and aks for appropriate time
while(True):
    if(t in list2):
        print('MOVIE_TIME: ',time_m[t])
        break
    else:
        print('this time is not available')
        print('choose available time')
        t = timings(movie)
        time = time_m.get(t)
    
    
# select theater
# ---------------------------------------------------------------------
#call theater function
t = theater()                  # t  == code of theater
th = place.get(t)              # th == name of theater


# select row 
#-----------------------------------------------------------------------------
R,c = sitting()


num,amount,t_amount = tickets(R)
print(amount)

movie_details(movie,time,th,num,amount,t_amount,R,c)