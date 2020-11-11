from itertools import permutations
import random,os,ast



#           0  1  2 
#           3  4  5
#           6  7  8

# 0  1  2   0  1  2   0  1  2 
# 3  4  5   3  4  5   3  4  5
# 6  7  8   6  7  8   6  7  8

#           0  1  2
#           3  4  5
#           6  7  8

#           0  1  2
#           3  4  5
#           6  7  8



front_face=['R','R','R', # 0  1  2
            'R','R','R', # 3  4  5
            'R','R','R'] # 6  7  8

top_face=['W','W','W', # 0  1  2
          'W','W','W', # 3  4  5
          'W','W','W'] # 6  7  8

bottom_face=['Y','Y','Y', # 0  1  2
             'Y','Y','Y', # 3  4  5
             'Y','Y','Y'] # 6  7  8

left_face=['G','G','G', # 0  1  2
           'G','G','G', # 3  4  5
           'G','G','G'] # 6  7  8

right_face=['B','B','B', # 0  1  2
            'B','B','B', # 3  4  5
            'B','B','B'] # 6  7  8

back_face=['O','O','O', # 0  1  2
           'O','O','O', # 3  4  5
           'O','O','O'] # 6  7  8
program_switch=True
def get_random(num):
    return random.randrange(num)

#-----------------------------------------------#
#-----------------------------------------------#
#-----------------------------------------------#
'''this section consists of functions that
   rotates each face of the cube and takes
   the direction of the rotation of the face
   as an argument'''

def rotate_top(direction):
    if direction=='right':
        #actual face
        extra=top_face[0]
        top_face[0]=top_face[6]
        top_face[6]=top_face[8]
        top_face[8]=top_face[2]
        top_face[2]=extra
        extra=top_face[1]
        top_face[1]=top_face[3]
        top_face[3]=top_face[7]
        top_face[7]=top_face[5]
        top_face[5]=extra

        #sides of face
        extra=front_face[0]
        front_face[0]=right_face[0]
        right_face[0]=back_face[8]
        back_face[8]=left_face[0]
        left_face[0]=extra
        
        extra=front_face[1]
        front_face[1]=right_face[1]
        right_face[1]=back_face[7]
        back_face[7]=left_face[1]
        left_face[1]=extra

        extra=front_face[2]
        front_face[2]=right_face[2]
        right_face[2]=back_face[6]
        back_face[6]=left_face[2]
        left_face[2]=extra
        
    elif direction=='left':
        #actual face
        extra=top_face[0]
        top_face[0]=top_face[2]
        top_face[2]=top_face[8]
        top_face[8]=top_face[6]
        top_face[6]=extra
        extra=top_face[1]
        top_face[1]=top_face[5]
        top_face[5]=top_face[7]
        top_face[7]=top_face[3]
        top_face[3]=extra

        #sides of face

        extra=front_face[0]
        front_face[0]=left_face[0]
        left_face[0]=back_face[8]
        back_face[8]=right_face[0]
        right_face[0]=extra

        extra=front_face[1]
        front_face[1]=left_face[1]
        left_face[1]=back_face[7]
        back_face[7]=right_face[1]
        right_face[1]=extra

        extra=front_face[2]
        front_face[2]=left_face[2]
        left_face[2]=back_face[6]
        back_face[6]=right_face[2]
        right_face[2]=extra

def rotate_front(direction):
    if direction=='right':
        #actual face
        extra=front_face[0]
        front_face[0]=front_face[6]
        front_face[6]=front_face[8]
        front_face[8]=front_face[2]
        front_face[2]=extra
        extra=front_face[1]
        front_face[1]=front_face[3]
        front_face[3]=front_face[7]
        front_face[7]=front_face[5]
        front_face[5]=extra

        #sides of face
        extra=top_face[6]
        top_face[6]=left_face[8]
        left_face[8]=bottom_face[2]
        bottom_face[2]=right_face[0]
        right_face[0]=extra

        extra=top_face[7]
        top_face[7]=left_face[5]
        left_face[5]=bottom_face[1]
        bottom_face[1]=right_face[3]
        right_face[3]=extra

        extra=top_face[8]
        top_face[8]=left_face[2]
        left_face[2]=bottom_face[0]
        bottom_face[0]=right_face[6]
        right_face[6]=extra

        
    elif direction=='left':
        #actual_face
        extra=front_face[0]
        front_face[0]=front_face[2]
        front_face[2]=front_face[8]
        front_face[8]=front_face[6]
        front_face[6]=extra

        extra=front_face[1]
        front_face[1]=front_face[5]
        front_face[5]=front_face[7]
        front_face[7]=front_face[3]
        front_face[3]=extra

        #sides of face
        extra=top_face[6]
        top_face[6]=right_face[0]
        right_face[0]=bottom_face[2]
        bottom_face[2]=left_face[8]
        left_face[8]=extra

        extra=top_face[7]
        top_face[7]=right_face[3]
        right_face[3]=bottom_face[1]
        bottom_face[1]=left_face[5]
        left_face[5]=extra

        extra=top_face[8]
        top_face[8]=right_face[6]
        right_face[6]=bottom_face[0]
        bottom_face[0]=left_face[2]
        left_face[2]=extra

        
def rotate_bottom(direction):
    if direction=='right':
        #actual face
        extra=bottom_face[0]
        bottom_face[0]=bottom_face[6]
        bottom_face[6]=bottom_face[8]
        bottom_face[8]=bottom_face[2]
        bottom_face[2]=extra

        extra=bottom_face[1]
        bottom_face[1]=bottom_face[3]
        bottom_face[3]=bottom_face[7]
        bottom_face[7]=bottom_face[5]
        bottom_face[5]=extra

        #sides of face
        extra=front_face[6]
        front_face[6]=left_face[6]
        left_face[6]=back_face[2]
        back_face[2]=right_face[6]
        right_face[6]=extra

        extra=front_face[7]
        front_face[7]=left_face[7]
        left_face[7]=back_face[1]
        back_face[1]=right_face[7]
        right_face[7]=extra

        extra=front_face[8]
        front_face[8]=left_face[8]
        left_face[8]=back_face[0]
        back_face[0]=right_face[8]
        right_face[8]=extra

        
    elif direction=='left':
        #actual face
        extra=bottom_face[0]
        bottom_face[0]=bottom_face[2]
        bottom_face[2]=bottom_face[8]
        bottom_face[8]=bottom_face[6]
        bottom_face[6]=extra

        extra=bottom_face[1]
        bottom_face[1]=bottom_face[5]
        bottom_face[5]=bottom_face[7]
        bottom_face[7]=bottom_face[3]
        bottom_face[3]=extra

        #sides of face
        extra=front_face[6]
        front_face[6]=right_face[6]
        right_face[6]=back_face[2]
        back_face[2]=left_face[6]
        left_face[6]=extra

        extra=front_face[7]
        front_face[7]=right_face[7]
        right_face[7]=back_face[1]
        back_face[1]=left_face[7]
        left_face[7]=extra

        extra=front_face[8]
        front_face[8]=right_face[8]
        right_face[8]=back_face[0]
        back_face[0]=left_face[8]
        left_face[8]=extra

def rotate_back(direction):
    if direction=='right':
        #actual face
        extra=back_face[0]
        back_face[0]=back_face[6]
        back_face[6]=back_face[8]
        back_face[8]=back_face[2]
        back_face[2]=extra

        extra=back_face[1]
        back_face[1]=back_face[3]
        back_face[3]=back_face[7]
        back_face[7]=back_face[5]
        back_face[5]=extra

        #sides of face
        extra=top_face[0]
        top_face[0]=right_face[2]
        right_face[2]=bottom_face[8]
        bottom_face[8]=left_face[6]
        left_face[6]=extra

        extra=top_face[1]
        top_face[1]=right_face[5]
        right_face[5]=bottom_face[7]
        bottom_face[7]=left_face[3]
        left_face[3]=extra

        extra=top_face[2]
        top_face[2]=right_face[8]
        right_face[8]=bottom_face[6]
        bottom_face[6]=left_face[0]
        left_face[0]=extra
        

    elif direction=='left':
        #actual face
        extra=back_face[0]
        back_face[0]=back_face[2]
        back_face[2]=back_face[8]
        back_face[8]=back_face[6]
        back_face[6]=extra

        extra=back_face[1]
        back_face[1]=back_face[5]
        back_face[5]=back_face[7]
        back_face[7]=back_face[3]
        back_face[3]=extra

        #sides of face
        extra=top_face[0]
        top_face[0]=left_face[6]
        left_face[6]=bottom_face[8]
        bottom_face[8]=right_face[2]
        right_face[2]=extra

        extra=top_face[1]
        top_face[1]=left_face[3]
        left_face[3]=bottom_face[7]
        bottom_face[7]=right_face[5]
        right_face[5]=extra

        extra=top_face[2]
        top_face[2]=left_face[0]
        left_face[0]=bottom_face[6]
        bottom_face[6]=right_face[8]
        right_face[8]=extra
        
def rotate_left(direction):
    if direction=='right':
        #actual face
        extra=left_face[0]
        left_face[0]=left_face[6]
        left_face[6]=left_face[8]
        left_face[8]=left_face[2]
        left_face[2]=extra

        extra=left_face[1]
        left_face[1]=left_face[3]
        left_face[3]=left_face[7]
        left_face[7]=left_face[5]
        left_face[5]=extra
        
        #sides of face
        extra=top_face[0]
        top_face[0]=back_face[0]
        back_face[0]=bottom_face[0]
        bottom_face[0]=front_face[0]
        front_face[0]=extra

        extra=top_face[3]
        top_face[3]=back_face[3]
        back_face[3]=bottom_face[3]
        bottom_face[3]=front_face[3]
        front_face[3]=extra

        extra=top_face[6]
        top_face[6]=back_face[6]
        back_face[6]=bottom_face[6]
        bottom_face[6]=front_face[6]
        front_face[6]=extra

        
    elif direction=='left':
        #actual face
        extra=left_face[0]
        left_face[0]=left_face[2]
        left_face[2]=left_face[8]
        left_face[8]=left_face[6]
        left_face[6]=extra

        extra=left_face[1]
        left_face[1]=left_face[5]
        left_face[5]=left_face[7]
        left_face[7]=left_face[3]
        left_face[3]=extra

        
        #sides of face
        extra=top_face[0]
        top_face[0]=front_face[0]
        front_face[0]=bottom_face[0]
        bottom_face[0]=back_face[0]
        back_face[0]=extra

        
        extra=top_face[3]
        top_face[3]=front_face[3]
        front_face[3]=bottom_face[3]
        bottom_face[3]=back_face[3]
        back_face[3]=extra

        
        extra=top_face[6]
        top_face[6]=front_face[6]
        front_face[6]=bottom_face[6]
        bottom_face[6]=back_face[6]
        back_face[6]=extra
    
def rotate_right(direction):
    if direction=='right':
        #actual face
        extra=right_face[0]
        right_face[0]=right_face[6]
        right_face[6]=right_face[8]
        right_face[8]=right_face[2]
        right_face[2]=extra

        extra=right_face[1]
        right_face[1]=right_face[3]
        right_face[3]=right_face[7]
        right_face[7]=right_face[5]
        right_face[5]=extra

        #sides of face
        extra=top_face[2]
        top_face[2]=front_face[2]
        front_face[2]=bottom_face[2]
        bottom_face[2]=back_face[2]
        back_face[2]=extra

        extra=top_face[5]
        top_face[5]=front_face[5]
        front_face[5]=bottom_face[5]
        bottom_face[5]=back_face[5]
        back_face[5]=extra

        extra=top_face[8]
        top_face[8]=front_face[8]
        front_face[8]=bottom_face[8]
        bottom_face[8]=back_face[8]
        back_face[8]=extra
        
        
    elif direction=='left':
        #actual face
        extra=right_face[0]
        right_face[0]=right_face[2]
        right_face[2]=right_face[8]
        right_face[8]=right_face[6]
        right_face[6]=extra

        extra=right_face[1]
        right_face[1]=right_face[5]
        right_face[5]=right_face[7]
        right_face[7]=right_face[3]
        right_face[3]=extra

        #sides of face
        extra=top_face[2]
        top_face[2]=back_face[2]
        back_face[2]=bottom_face[2]
        bottom_face[2]=front_face[2]
        front_face[2]=extra

        extra=top_face[5]
        top_face[5]=back_face[5]
        back_face[5]=bottom_face[5]
        bottom_face[5]=front_face[5]
        front_face[5]=extra

        extra=top_face[8]
        top_face[8]=back_face[8]
        back_face[8]=bottom_face[8]
        bottom_face[8]=front_face[8]
        front_face[8]=extra
#-----------------------------------------------#
#-----------------------------------------------#
#-----------------------------------------------#

      
def scramble_cube(ammount):
    '''scrambles the cube by randomly calling the
       face rotation functions to the ammount specified by
       argmuent passed '''
    options=['r_f','r_t','r_bo','r_ba','r_r','r_l']
    directions=['right','left']
    for i in range(ammount):
        face=options[get_random(len(options))]
        direction=directions[get_random(len(directions))]
        if face=='r_f':
            rotate_front(direction)
        elif face=='r_t':
            rotate_top(direction)
        elif face=='r_bo':
            rotate_bottom(direction)
        elif face=='r_ba':
            rotate_back(direction)
        elif face=='r_r':
            rotate_right(direction)
        elif face=='r_l':
            rotate_left(direction)

def print_cube():
    '''this functions prints out the map of net map
       of the cube'''
    space='          '
    form='|{}|'
    item=''

    
    item+=space
    for i in top_face[0:3]:
        item+=form.format(i)
    print(item)
    item=''
    item+=space
    for i in top_face[3:6]:
        item+=form.format(i)
    print(item)
    item=''
    item+=space
    for i in top_face[6:9]:
        item+=form.format(i)
    print(item)
    item=''
    
    print('')
    
    
    for i in left_face[0:3]:
        item+=form.format(i)
    item+=' '
    for i in front_face[0:3]:
        item+=form.format(i)
    item+=' '
    for i in right_face[0:3]:
        item+=form.format(i)
    print(item)
    item=''

    for i in left_face[3:6]:
        item+=form.format(i)
    item+=' '
    for i in front_face[3:6]:
        item+=form.format(i)
    item+=' '
    for i in right_face[3:6]:
        item+=form.format(i)
    print(item)
    item=''

    for i in left_face[6:9]:
        item+=form.format(i)
    item+=' '
    for i in front_face[6:9]:
        item+=form.format(i)
    item+=' '
    for i in right_face[6:9]:
        item+=form.format(i)
    print(item)
    item=''
    print('')

    item+=space
    for i in bottom_face[0:3]:
        item+=form.format(i)
    print(item)
    item=''
    item+=space
    for i in bottom_face[3:6]:
        item+=form.format(i)
    print(item)
    item=''
    item+=space
    for i in bottom_face[6:9]:
        item+=form.format(i)
    print(item)
    item=''
    print('')

    item+=space
    for i in back_face[0:3]:
        item+=form.format(i)
    print(item)
    item=''
    item+=space
    for i in back_face[3:6]:
        item+=form.format(i)
    print(item)
    item=''
    item+=space
    for i in back_face[6:9]:
        item+=form.format(i)
    print(item)
    
    

#========================================#
'''this section contains functions that are used to potentially
   write the solution of the solved cube if one were to make a program to
   attempt to solve it'''
def get_sol_file_names():
    file=open('solution_logs/sol_file_names.txt','r')
    info=ast.literal_eval(file.read())
    file.close()
    return info

def add_sol_file_name(name):
    info=get_sol_file_names()
    info.append(name)
    file=open('solution_logs/sol_file_names.txt','w')
    for i in str(info):
        file.write(i)
    file.close()
    
def remove_sol_file_name(name):
    info=get_sol_file_names()
    info.remove(name)
    file=open('solution_logs/sol_file_names.txt','w')
    for i in str(info):
        file.write(i)
    file.close()
    
def write_solution(info):
      

    def check_available_file_name():
        names=get_sol_file_names()
        num=1
        fname='solution_'
        for i in range(len(names)+1):
            if fname+str(num) in names:
                num+=1
            else:
                return fname+str(num)
            
    available_name=check_available_file_name()+'.txt'
    file=open(available_name,'w')
    for i in str(info):
        file.write(i)
    file.close()
#========================================#
    
def face_move(face,dire):
    if face=='r_f':
        rotate_front(dire)
    elif face=='r_t':
        rotate_top(dire)
    elif face=='r_bo':
        rotate_bottom(dire)
    elif face=='r_ba':
        rotate_back(dire)
    elif face=='r_r':
        rotate_right(dire)
    elif face=='r_l':
        rotate_left(dire)



    








#scramble_cube()


































