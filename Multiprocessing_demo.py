import multiprocessing
import concurrent.futures
import time

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'


# using the multiprocessing library 
# p1 = multiprocessing.Process(target=do_something)
# p2 = multiprocessing.Process(target=do_something)

# p1.start()
# p2.start()

# p1.join() #using the join method so the p1 and p2 processes finish before continuing the rest of the script
# p2.join()

# doing the same thing but for 10 processes this time 
# processes= []
# for _ in range(10):  # the _ indicates that its throw away value we are not using 
#     p = multiprocessing.Process(target=do_something, args=[1.5]) #sleeps for 1.5 secs
#     p.start()
#     processes.append(p) #adding all ten processes to a list 

# for process in processes:
#     process.join()

#using the concurrent.futures module
with concurrent.futures.ProcessPoolExecutor() as executor: #automatically joins processes
    secs = [5, 4, 3, 2, 1]
    # results = [executor.submit(do_something, sec) for sec in secs] #using list comprehension to run 10 processes concurrently
    results = executor.map(do_something, secs) #returns the results in order that they started

    
    
    # for f in concurrent.futures.as_completed(results): #iterates through the results as they are completed
    #     print(f.result())
    for result in results: #prints results in order they were started
        print(result)

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')