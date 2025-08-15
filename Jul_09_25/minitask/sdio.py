with open('D:\internship\python I_O operations\minitask\students.txt', 'r') as inf,open('results.txt','w') as outf:
    data=[]
    for line in inf:
        l=line.strip()
        print(l)
        data.append(l.split(','))
    
    val=0
    inval=0
    null_str=''
    for i in data:
        try:
            if i[0] is null_str or i[1] is null_str:
                outf.write(f'{i[0]}: Invalid (missing name or marks)\n')
                inval+=1
            elif 0>int(i[1]) or int(i[1])>100:
                outf.write(f'{i[0]} : Invalid (marks out of range)\n')
                inval+=1
            else:
                outf.write(f'{i[0]} : Valid Score = {i[1]}\n')
                val+=1
        except ValueError:
            outf.write(f'{i[0]} : Invalid (non numeric marks)\n')
            inval+=1
    
    print(f'''Invalid entries are {inval} \n valid entries are {val}''')
