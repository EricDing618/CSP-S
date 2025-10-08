def main(length,target_score,result:list):
    
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
