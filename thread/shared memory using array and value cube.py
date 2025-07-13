import multiprocessing as mp

def cube(mylist,result,cube_sum):
    for idx,element in enumerate(mylist):
        result[idx] = element ** 3

    cube_sum.value = sum(result[:])

    print(result)
    print(cube_sum)

if __name__ == "__main__":

    mylist = [1,2,3,4]
    result=mp.Array('i',4)
    cube_sum = mp.Value('i')

    p1=mp.Process(target=cube,args=(mylist,result,cube_sum))
    p1.start()
    p1.join()
    print(result[:])
    print(cube_sum.value)