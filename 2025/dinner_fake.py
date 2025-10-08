def main(length,target_score,result:list):
    a_get=0
    b_get=0
    for i in range(length):
        tr = result[i]
        if tr=='A':
            a_get+=1
        if tr=='B':
            b_get+=1
        if (a_get>=target_score or b_get>=target_score) and abs(a_get-b_get)>=2:
            '''print('Yes\n'+str(a_get+b_get))
            return 'Yes\n'+str(a_get+b_get)'''
    print('No')
    return 'No'

if __name__ == '__main__':
    r=[]
    with open('dinner.in','r',encoding='utf-8') as f:
        din=f.read().splitlines()
        print(din)
    '''a=input('test_len')
    for _ in range(int(a)):
        b=input('').split(' ')
        c=input('')
        main(int(b[0]),int(b[1]),list(c))'''
    for _ in range(int(din.pop(0))):
        b,c=din.pop(0).split(' '),din.pop(0)
        d=main(int(b[0]),int(b[1]),list(c))
        r.append(d)
    with open('dinner.out','w',encoding='utf-8') as f:
        f.write('\n'.join(r))
