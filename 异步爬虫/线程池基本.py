from multiprocessing.dummy import Pool
import time

start_time = time.time()
def get_page(str):
    print('start:',str)
    time.sleep(2)
    print('end:', str)

nlist = ['aa', 'bb', 'cc', 'dd']

pool = Pool(4) #4个线程
pool.map(get_page, nlist)

end_time = time.time()
print(end_time - start_time)