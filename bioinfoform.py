# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 16:26:09 2019

@author: uasmt
"""

import tkinter as tk
import numpy as np

#blosum62 tablosu
blosum62 = {
        ('W', 'F'): 1, ('L', 'R'): -2, ('S', 'P'): -1, ('V', 'T'): 0,
        ('Q', 'Q'): 5, ('N', 'A'): -2, ('Z', 'Y'): -2, ('W', 'R'): -3,
        ('Q', 'A'): -1, ('S', 'D'): 0, ('H', 'H'): 8, ('S', 'H'): -1,
        ('H', 'D'): -1, ('L', 'N'): -3, ('W', 'A'): -3, ('Y', 'M'): -1,
        ('G', 'R'): -2, ('Y', 'I'): -1, ('Y', 'E'): -2, ('B', 'Y'): -3,
        ('Y', 'A'): -2, ('V', 'D'): -3, ('B', 'S'): 0, ('Y', 'Y'): 7,
        ('G', 'N'): 0, ('E', 'C'): -4, ('Y', 'Q'): -1, ('Z', 'Z'): 4,
        ('V', 'A'): 0, ('C', 'C'): 9, ('M', 'R'): -1, ('V', 'E'): -2,
        ('T', 'N'): 0, ('P', 'P'): 7, ('V', 'I'): 3, ('V', 'S'): -2,
        ('Z', 'P'): -1, ('V', 'M'): 1, ('T', 'F'): -2, ('V', 'Q'): -2,
        ('K', 'K'): 5, ('P', 'D'): -1, ('I', 'H'): -3, ('I', 'D'): -3,
        ('T', 'R'): -1, ('P', 'L'): -3, ('K', 'G'): -2, ('M', 'N'): -2,
        ('P', 'H'): -2, ('F', 'Q'): -3, ('Z', 'G'): -2, ('X', 'L'): -1,
        ('T', 'M'): -1, ('Z', 'C'): -3, ('X', 'H'): -1, ('D', 'R'): -2,
        ('B', 'W'): -4, ('X', 'D'): -1, ('Z', 'K'): 1, ('F', 'A'): -2,
        ('Z', 'W'): -3, ('F', 'E'): -3, ('D', 'N'): 1, ('B', 'K'): 0,
        ('X', 'X'): -1, ('F', 'I'): 0, ('B', 'G'): -1, ('X', 'T'): 0,
        ('F', 'M'): 0, ('B', 'C'): -3, ('Z', 'I'): -3, ('Z', 'V'): -2,
        ('S', 'S'): 4, ('L', 'Q'): -2, ('W', 'E'): -3, ('Q', 'R'): 1,
        ('N', 'N'): 6, ('W', 'M'): -1, ('Q', 'C'): -3, ('W', 'I'): -3,
        ('S', 'C'): -1, ('L', 'A'): -1, ('S', 'G'): 0, ('L', 'E'): -3,
        ('W', 'Q'): -2, ('H', 'G'): -2, ('S', 'K'): 0, ('Q', 'N'): 0,
        ('N', 'R'): 0, ('H', 'C'): -3, ('Y', 'N'): -2, ('G', 'Q'): -2,
        ('Y', 'F'): 3, ('C', 'A'): 0, ('V', 'L'): 1, ('G', 'E'): -2,
        ('G', 'A'): 0, ('K', 'R'): 2, ('E', 'D'): 2, ('Y', 'R'): -2,
        ('M', 'Q'): 0, ('T', 'I'): -1, ('C', 'D'): -3, ('V', 'F'): -1,
        ('T', 'A'): 0, ('T', 'P'): -1, ('B', 'P'): -2, ('T', 'E'): -1,
        ('V', 'N'): -3, ('P', 'G'): -2, ('M', 'A'): -1, ('K', 'H'): -1,
        ('V', 'R'): -3, ('P', 'C'): -3, ('M', 'E'): -2, ('K', 'L'): -2,
        ('V', 'V'): 4, ('M', 'I'): 1, ('T', 'Q'): -1, ('I', 'G'): -4,
        ('P', 'K'): -1, ('M', 'M'): 5, ('K', 'D'): -1, ('I', 'C'): -1,
        ('Z', 'D'): 1, ('F', 'R'): -3, ('X', 'K'): -1, ('Q', 'D'): 0,
        ('X', 'G'): -1, ('Z', 'L'): -3, ('X', 'C'): -2, ('Z', 'H'): 0,
        ('B', 'L'): -4, ('B', 'H'): 0, ('F', 'F'): 6, ('X', 'W'): -2,
        ('B', 'D'): 4, ('D', 'A'): -2, ('S', 'L'): -2, ('X', 'S'): 0,
        ('F', 'N'): -3, ('S', 'R'): -1, ('W', 'D'): -4, ('V', 'Y'): -1,
        ('W', 'L'): -2, ('H', 'R'): 0, ('W', 'H'): -2, ('H', 'N'): 1,
        ('W', 'T'): -2, ('T', 'T'): 5, ('S', 'F'): -2, ('W', 'P'): -4,
        ('L', 'D'): -4, ('B', 'I'): -3, ('L', 'H'): -3, ('S', 'N'): 1,
        ('B', 'T'): -1, ('L', 'L'): 4, ('Y', 'K'): -2, ('E', 'Q'): 2,
        ('Y', 'G'): -3, ('Z', 'S'): 0, ('Y', 'C'): -2, ('G', 'D'): -1,
        ('B', 'V'): -3, ('E', 'A'): -1, ('Y', 'W'): 2, ('E', 'E'): 5,
        ('Y', 'S'): -2, ('C', 'N'): -3, ('V', 'C'): -1, ('T', 'H'): -2,
        ('P', 'R'): -2, ('V', 'G'): -3, ('T', 'L'): -1, ('V', 'K'): -2,
        ('K', 'Q'): 1, ('R', 'A'): -1, ('I', 'R'): -3, ('T', 'D'): -1,
        ('P', 'F'): -4, ('I', 'N'): -3, ('K', 'I'): -3, ('M', 'D'): -3,
        ('V', 'W'): -3, ('W', 'W'): 11, ('M', 'H'): -2, ('P', 'N'): -2,
        ('K', 'A'): -1, ('M', 'L'): 2, ('K', 'E'): 1, ('Z', 'E'): 4,
        ('X', 'N'): -1, ('Z', 'A'): -1, ('Z', 'M'): -1, ('X', 'F'): -1,
        ('K', 'C'): -3, ('B', 'Q'): 0, ('X', 'B'): -1, ('B', 'M'): -3,
        ('F', 'C'): -2, ('Z', 'Q'): 3, ('X', 'Z'): -1, ('F', 'G'): -3,
        ('B', 'E'): 1, ('X', 'V'): -1, ('F', 'K'): -3, ('B', 'A'): -2,
        ('X', 'R'): -1, ('D', 'D'): 6, ('W', 'G'): -2, ('Z', 'F'): -3,
        ('S', 'Q'): 0, ('W', 'C'): -2, ('W', 'K'): -3, ('H', 'Q'): 0,
        ('L', 'C'): -1, ('W', 'N'): -4, ('S', 'A'): 1, ('L', 'G'): -4,
        ('W', 'S'): -3, ('S', 'E'): 0, ('H', 'E'): 0, ('S', 'I'): -2,
        ('H', 'A'): -2, ('S', 'M'): -1, ('Y', 'L'): -1, ('Y', 'H'): 2,
        ('Y', 'D'): -3, ('E', 'R'): 0, ('X', 'P'): -2, ('G', 'G'): 6,
        ('G', 'C'): -3, ('E', 'N'): 0, ('Y', 'T'): -2, ('Y', 'P'): -3,
        ('T', 'K'): -1, ('A', 'A'): 4, ('P', 'Q'): -1, ('T', 'C'): -1,
        ('V', 'H'): -3, ('T', 'G'): -2, ('I', 'Q'): -3, ('Z', 'T'): -1,
        ('C', 'R'): -3, ('V', 'P'): -2, ('P', 'E'): -1, ('M', 'C'): -1,
        ('K', 'N'): 0, ('I', 'I'): 4, ('P', 'A'): -1, ('M', 'G'): -3,
        ('T', 'S'): 1, ('I', 'E'): -3, ('P', 'M'): -2, ('M', 'K'): -1,
        ('I', 'A'): -1, ('P', 'I'): -3, ('R', 'R'): 5, ('X', 'M'): -1,
        ('L', 'I'): 2, ('X', 'I'): -1, ('Z', 'B'): 1, ('X', 'E'): -1,
        ('Z', 'N'): 0, ('X', 'A'): 0, ('B', 'R'): -1, ('B', 'N'): 3,
        ('F', 'D'): -3, ('X', 'Y'): -1, ('Z', 'R'): 0, ('F', 'H'): -1,
        ('B', 'F'): -3, ('F', 'L'): 0, ('X', 'Q'): -1, ('B', 'B'): 4
        }


def maximum(a, b, c): 
    list = [a, b, c]
    return 0 if a<0 and b<0 and c<0 else max(list) 

#Ödev 2
def score_2(seq1, seq2, blosum, gap):
    gap_penalty = int(gap)
    u1 = len(seq1)
    u2 = len(seq2)
    seq1 = seq1.upper()
    seq2 = seq2.upper()
    score = 0
    matrix = []
    listOfScoreMatrix = [[]]
    for i in range(u2+1):
        matrix.append([])
        if i == 0:
            matrix[i].append('+')
            for j in range(u1):
                matrix[i].append(seq1[j])
        else:
            matrix[i].append(seq2[i-1])
            for j in range(u1):
                matrix[i].append(0)
    
    for r,row in enumerate(matrix):
        for c,col in enumerate(row):
            if r>0 and c>0:
                A = matrix[r][0] 
                B = matrix[0][c]
                matrix[r][c] = blosum[(A,B)] if (A,B) in blosum else blosum[(B,A)]
        
    d = maximum(u1,u2,0)
    r = u2
    c = u1
    g = 0
    for i in range(d):
        if matrix[0][c] == matrix[r][0] or r==c:    
            score +=matrix[r][c]
            listOfScoreMatrix.append([r,c])
            c-=1
            r-=1
        else:
            g +=1
            c-=1
    
    score += g*gap_penalty
    return score,matrix,listOfScoreMatrix

def score_3(seq1,seq2,gap_pen,mismatch,match):
    u1 = len(seq1)
    u2 = len(seq2)
    matrix = []
    i = 2
    biggest_number = 0
    r_of_bg = 0
    c_of_bg = 0
    
    for i in range(u2+2):
        matrix.append([])
        if i == 0:
            matrix[i].append('+')
            for j in range(u1+1):
                if j == 0:
                    matrix[i].append('-')
                else:
                    matrix[i].append(seq1[j-1])
        elif i== 1:
            matrix[i].append('-')
            for j in range(u1+1):
                matrix[i].append(0)
        else:
            matrix[i].append(seq2[i-2])
            for j in range(u1+1):
                matrix[i].append(0)
    
    for r,row in enumerate(matrix):
        for c,col in enumerate(row):
            first_row = matrix[r][0] 
            first_col = matrix[0][c]
            
            if c>1 and r>1:
                up = matrix[r-1][c]
                left = matrix[r][c-1]
                upleft =matrix[r-1][c-1]
                
                if first_row == first_col:
                    matrix[r][c] = upleft + match
                    if matrix[r][c] > biggest_number:
                        biggest_number = matrix[r][c]
                        r_of_bg = r
                        c_of_bg = c
                else:
                    u = up+gap_pen
                    l = left+gap_pen
                    ul = upleft + mismatch
                    
                    matrix[r][c] = maximum(u,l,ul)
    
    return matrix,biggest_number,r_of_bg,c_of_bg

def local_Alignment(seq1,seq2,gap_pen,mismatch,match):
    matrix, bg,r,c = score_3(seq1,seq2,gap_pen,mismatch,match)
    listseq1 = []
    listseq2 = []
    listOfScoreMatrix = [[]]
    listOfScoreMatrix.append([r,c])
    m=0
    mm = 0
    g=0
    for i in range(r):
        last = matrix[r][c]
        up = matrix[r-1][c]
        left = matrix[r][c-1]
        upleft =matrix[r-1][c-1]
        
        if matrix[0][c] == matrix[r][0]:
            listseq1.append(matrix[0][c])
            listseq2.append(matrix[r][0])
            r -=1
            c -=1
            m +=1
            listOfScoreMatrix.append([r,c])
        else:
            if isinstance(upleft, int) and last-upleft == mismatch:
                print(last,upleft)
                print(mismatch)
                listseq1.append(matrix[0][c])
                listseq2.append(matrix[r][0])
                r -=1
                c -=1
                mm +=1
                listOfScoreMatrix.append([r,c])
            elif isinstance(up, int) and last-up == gap_pen:
                listseq1.append('-')
                listseq2.append(matrix[r][0])
                r -=1
                g +=1
                listOfScoreMatrix.append([r,c])
            elif isinstance(left, int) and last-left == gap_pen:
                listseq1.append(matrix[0][c])
                listseq2.append('-')
                c -=1
                g +=1
                listOfScoreMatrix.append([r,c])
    score = gap_pen*g + match*m + mismatch*mm
    return matrix,listseq1,listseq2,m,mm,g,score,listOfScoreMatrix

def check (a,b,lm):
    for i in range(len(lm)):
        if lm[i] == [a,b]:
            return True
    return False

def drawMatrix(matrix,window2,lm):
    x = 0
    y = 0
    for i in range(len(matrix)):
        x=0
        for j in range(len(matrix[0])):
            colour = "white"
            if check(i,j,lm):
                colour ="red"
            o = tk.Text(window2,width="6",height="3",bg=colour)
            o.configure(font=("Times New    Roman", 12, "bold"))
            o.place(x=x,y=y)
            if str(matrix[i][j]) != "+":
                o.insert(tk.END,str(matrix[i][j]))
            x+=50
        y+=50
    return x,y


def score_4(seq1, seq2):
    u1 = len(seq1)
    u2 = len(seq2)
    matrix = []
    for i in range(u2+1):
        matrix.append([])
        if i == 0:
            matrix[i].append('+')
            for j in range(u1):
                matrix[i].append(seq1[j])
        else:
            matrix[i].append(seq2[i-1])
            for j in range(u1):
                matrix[i].append(0)
    
    for r,row in enumerate(matrix):
        for c,col in enumerate(row):
            if r>0 and c>0:
                A = matrix[r][0] 
                B = matrix[0][c]
                matrix[r][c] = True if A==B else False
    return matrix


def drawMatrix2(s1,s2,window2,data):
    x = 0
    y = 0
    for i in range(len(data)+1):
        x=0
        for j in range(len(data[0])+1):
            result= ""
            colour = "white"
            if i==0 and j>0:
                result = s1[j-1]
            else:
                if j==0 and i>0:
                    result = s2[i-1]
                else:
                    if data[i-1][j-1]=='True' and i!=0:
                        colour ="red"
            o = tk.Text(window2,width="6",height="3",bg=colour)
            o.configure(font=("Times New Roman", 12, "bold"))
            o.place(x=x,y=y)
            o.insert(tk.END,result)
            
            x+=50
        y+=50
    return x,y

def createWindowForGlobal(matrix,score,lm):
    window2 = tk.Toplevel(window)
    x,y = drawMatrix(matrix,window2,lm)
    y+=5    
    result = "Score : " + str(score) 
    o = tk.Text(window2,width="50",height="2",bg="white")
    o.place(x=0,y=y)
    o.insert(tk.END,result)
    y+=50
    window2.geometry(str(x)+'x'+str(y))

def createWindowForLocal(matrix,s1,s2,ma,mm,gap,score,lm):
    window2 = tk.Toplevel(window)
    x,y = drawMatrix(matrix,window2,lm)
    y+=5
    s1 = s1[::-1]
    s2 = s2[::-1]
    a = "Sequence 1 : "+ "\n" + str(s1) + "\n"
    b = "Sequence 2 : "+ "\n" + str(s2) + "\n"
    c = "Match : " + str(ma) + "\n"
    d = "MissMatch : " + str(mm) + "\n"
    e = "Gap : " + str(gap) + "\n"
    f = "Score : " + str(score) + "\n"
    result = a + b+ c+ d+ e+f 
    o = tk.Text(window2,width="60",height="25",bg="white")
    o.place(x=0,y=y)
    o.insert(tk.END,result)
    y+=150
    window2.geometry(str(x)+'x'+str(y))

def createWindowForDotPlot(s1,s2,data):
    window2 = tk.Toplevel(window)
    x,y = drawMatrix2(s1,s2,window2,data)
    window2.geometry(str(x)+'x'+str(y))
    
def click1():
    errorinfo.delete(1.0, tk.END)
    try:
        gap = int(gappen.get())
    except ValueError:
        errorinfo.insert(tk.END,"Please Enter a number in The Gap Penalty")
    seq1 = seq1entery.get()
    seq2 = seq2entery.get()
    if gap == "" or seq1 =="" or seq2=="":
        errorinfo.insert(tk.END,"Please Fill in the blank fields; Gap Penalty,\nFirst and Second Sequences")
    else:
        score,matrix,listofm = score_2(seq1,seq2,blosum62,gap)
        createWindowForGlobal(matrix,score,listofm)
    
def click2():
    errorinfo.delete(1.0, tk.END)
    try:
        gap = int(gappen.get())
        missm = int(missmatch.get())
        ma = int(match.get())
    except ValueError:
        errorinfo.insert(tk.END,"Please Enter a number For Gap Penalty,\nMissmatch and Match Point ")
    seq1 = seq1entery.get()
    seq2 = seq2entery.get()
    if gap == "" or seq1 =="" or seq2=="":
        errorinfo.insert(tk.END,"Please Fill in the ALL blank fields;")
    else:
        matrix,s1,s2,m,mm,g,score,listofm = local_Alignment(seq1,seq2,gap,missm,ma)
        createWindowForLocal(matrix,s1,s2,m,mm,g,score,listofm)
    
def click3():
    errorinfo.delete(1.0, tk.END)
    seq1 = seq1entery.get()
    seq2 = seq2entery.get()
    if seq1 =="" or seq2=="":
        errorinfo.insert(tk.END,"Please Fill in the Sequences fields;")
    else:
        data = score_4(seq1,seq2)
        data = np.delete(data, [0], axis=1)
        data = np.delete(data, [0], axis=0)
        createWindowForDotPlot(seq1,seq2,data)
        
w = 600
h = 310
window = tk.Tk()
window.geometry(str(w)+'x'+str(h))
window.title("Bioinformatic")

tk.Label(window,text='COMPARE TWO SEQUENCE OF AMINOACIDS USING METHODS',fg='red',font='none 12 bold').place(x=50,y=0)

tk.Label(window,text='Please Use Letters For Sequences and The Others have to be a NUMBER',fg='red',font='none 7 bold').place(x=100,y=30)
tk.Label(window,text='First Sequence : ',fg='black',font='none 12 bold').place(x=100,y=50)
seq1entery = tk.Entry(window,width=30,bg='white')
seq1entery.place(x=300,y=50)

tk.Label(window,text='Second Sequence : ', fg='black',font='none 12 bold').place(x=100,y=80)
seq2entery = tk.Entry(window,width=30,bg='white')
seq2entery.place(x=300,y=80)

tk.Label(window,text=' Use Gap Penalty For Local and Global Alignment ',fg='red',font='none 7 bold').place(x=170,y=110)
tk.Label(window,text='Gap Penalty     : ', fg='black',font='none 12 bold').place(x=100,y=125)
gappen = tk.Entry(window,width=30,bg='white')
gappen.place(x=300,y=125)

tk.Label(window,text=' Use Missmatch and Match Point just For Local Alignment ',fg='red',font='none 7 bold').place(x=150,y=155)
tk.Label(window,text='Missmatch Point : ',fg='black',font='none 12 bold').place(x=100,y=170)
missmatch = tk.Entry(window,width=30,bg='white')
missmatch.place(x=300,y=170)

tk.Label(window,text='Match Point     : ',fg='black',font='none 12 bold').place(x=100,y=200)
match = tk.Entry(window,width=30,bg='white')
match.place(x=300,y=200)

button1 = tk.Button(window,text='Global Aligment',command=click1)
button1.place(x=150,y=230) 
button2 = tk.Button(window,text='Local Aligment',command=click2)
button2.place(x=250,y=230) 
button3 = tk.Button(window,text='Sequence Aligment',command=click3)
button3.place(x=350,y=230) 

errorinfo = tk.Text(window,width="50",height="2")
errorinfo.place(x=90,y=260)
window.mainloop()


