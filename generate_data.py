def generate():
    import random

    N = int(input('so bai bao:'))
    M = int(input('so nha khoa hoc:'))
    K = int(input('so nha khoa hoc toi thieu nghien cuu 1 bai bao:'))

    a = [] #list chứa số nhà khoa học tham gia mỗi bài báo, K <= a[i] <= M
    for i in range(N):
        a.append(random.randint(K, M))   #so nha khoa hoc tham gia nghien cuu bai bao thu i

    X = []
    for x in a:
        X.append(random.sample(range(1,M+1), x))    #random những nhà khoa học nào sẽ thực hiện bài báo thứ i

    f = open('data_sample.txt', 'w')

    f.write('{} {} {}\n'.format(N,M,K))
    for i in range(len(a)):
        f.write(str(a[i])+' ')
        f.writelines(str(X[i][j])+' ' for j in range (a[i]))
        f.write('\n')

    f.close()

def read_data(filename):
    with open(filename, 'r') as f:
        '''
        N: số bài báo
        M: số chuyên gia
        K: số chuyên gia tối thiểu
        '''
        N,M,K = [int(x) for x in f.readline().split()]
        A = [([0]*M) for i in range(N)]
        cost = [([0]*M) for i in range(N)]
        for i in range (N):
            lst = []
            lst = [int(x) for x in f.readline().split()]
            for j in range(1,len(lst)):
                A[i][lst[j]-1] = 1
        return N,M,K,A
    
def main():
    generate()
if __name__ == "__main__":
    main()