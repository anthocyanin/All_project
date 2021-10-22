import os

pid = os.fork()

if pid == 0:
    print('i am child process %s, my parent process is %s' % (os.getpid(), os.getppid()))
else:
    print('i am parent process %s, i just created child process %s' % (os.getpid(),  pid))









