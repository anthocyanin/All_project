import os, sys


for i in range(10):
    if sys.platform[:3] == 'win':
        pypath = sys.executable
        os.spawnv(os.P_WAIT, pypath, ('python', 'child.py', str(i)))
    else:
        pid = os.fork()
        if pid != 0:
            print('Process %d spawned' % pid)
        else:
            os.execlp('/Users/gonghuidepro/anaconda3/bin/python', 'python', 'child.py', str(i))

print('main process exiting')

