##import threading
##def print_thread_names():
##    print("Current thread name:", threading.current_thread().name)
### Create multiple threads
##threads = []
##for i in range(7):
##    thread = threading.Thread(target=print_thread_names)
##    threads.append(thread)
##    thread.start()
##
### Wait for all threads to complete
##for thread in threads:
##    thread.join()

##=================================================================
#3. Write a Python program that creates two threads to find and print even and odd numbers from 30 to 50.


##import threading
##def evn_thread():
##    for i in range(30,51,2):
##        print("List of even numbers:")
##
##        print(i,end=' ')
##def odd_thread():
##    print("\nList of odd numbers:")
##
##    for j in range(31,51,2):
##        print(j,end=' ')
##even=threading.Thread(target = evn_thread)
##odd=threading.Thread(target = odd_thread)
##even.start()
##odd.start()
##even.join()
##odd.join()

#============================================

#4. Write a Python program to calculate the factorial of a number using multiple threads.

##import threading
##
##def factorial(n):
##    fact=1
####    n=5
##    for i in range(1,n+1):
##        fact=fact*i
##    print(fact)
##one_fact = threading.Thread(target = factorial, args=(5,))
##two_fact = threading.Thread(target = factorial, args=(5,))
##one_fact.start()
##
##
##two_fact.start()
##one_fact.join()
##two_fact.join()






















