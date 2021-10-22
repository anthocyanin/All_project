import sys,  os

pyfile = (sys.platform[:3] == 'win' and 'python.exe') or 'python'
pyPATH = sys.executable


def fixwindowspath(cmdline):
    splitline = cmdline.lstrip().split(' ')
    fixpath  = os.path.normpath(splitline[0])
    return ' '.join([fixpath] + splitline[1:])


class LaunchMode:
    def __init__(self, lable, command):
        self.what = lable
        self.where = command

    def __call__(self, *args, **kwargs):
        self.announce(self.what)
        self.run(self.where)

    def announce(self, text):
        print(text)

    def run(self,cmdline):
        assert False, 'run  must be  defined'


class System(LaunchMode):
    def run(self, cmdline):
        cmdline = fixwindowspath(cmdline)
        os.system('%s  %s' % (pyPATH, cmdline))


class Popen(LaunchMode):
    def run(self, cmdline):
        cmdline = fixwindowspath(cmdline)
        os.popen(pyPATH + " " + cmdline)


class Fork(LaunchMode):
    def run(self, cmdline):
        assert hasattr(os, 'fork')
        cmdline = cmdline.split()
        if os.fork() == 0:
            os.execvp(pyPATH, [pyfile] + cmdline)


class Start(LaunchMode):
    def run(self, cmdline):
        assert sys.platform[:3] == 'win'
        cmdline = fixwindowspath(cmdline)
        os.startfile(cmdline)


class StartArgs(LaunchMode):
    def run(self,cmdline):
        assert sys.platform[:3] == 'win'
        os.system('start' + cmdline)


class Spawn(LaunchMode):
    def run(self, cmdline):
        os.spawnv(os.P_DETACH, pyPATH, (pyfile, cmdline))


class Top_level(LaunchMode):
    def run(self,cmdline):
        assert False, 'sorry - mode not yet implemented'


if sys.platform[:3] == 'win':
    PortableLauncher = Spawn
else:
    PortableLauncher = Fork


class QuietPortableLauncher(PortableLauncher):
    def announce(self, text):
        pass


def selftest():
    file = 'echo.py'
    input('default mode:')
    laucher = PortableLauncher(file, file)
    laucher()
    input('system mode:')
    System(file, file)()

    if sys.platform[:3] == 'win':
        input('Dos start mode:')
        StartArgs(file, file)()


if __name__ == '__main__':
    selftest()











