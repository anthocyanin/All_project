from .proxypool.scheduler import Scheduler
import sys
import io

# 这句代码什么意思呢
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def main():
    try:
        s = Scheduler()
        s.run()
    except:
        main()


if __name__ == '__main__':
    main()


