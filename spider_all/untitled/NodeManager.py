from multiprocessing.managers import BaseManager
from multiprocessing import Process, Queue
from URLManager import UrlManager
from DataOutput import DataOutput
import time


class NodeManager:
    def start_manager(self, url_q, result_q):
        # 把创建的两个队列注册在网络上，利用register方法，callable参数关联了Queue对象，
        # 将Queue对象在网络中暴露
        BaseManager.register('get_task_queue', callable=lambda: url_q)
        BaseManager.register('get_result_queue', callable=lambda: result_q)
        # 绑定端口8001，设置验证口令‘baike’。这个相当于对象的初始化
        manager = BaseManager(address=('', 8001), authkey='baike'.encode('utf-8'))
        # 返回manager对象
        return manager

    def url_manager_pro(self, url_q, conn_q, root_url):
        url_manager = UrlManager()
        url_manager.add_new_url(root_url)
        while True:
            while url_manager.has_new_url():
                # 获取url
                new_url = url_manager.get_new_url()
                # 将URL发给爬虫节点
                url_q.put(new_url)
                print('old_url=', url_manager.old_url_size())
                # 加一个判断条件，当爬去1000个链接后就关闭,并保存进度
                if url_manager.old_url_size() > 1000:
                    # 通知爬虫节点工作结束
                    url_q.put('end')
                    print('控制节点发起结束通知!')
                    # 关闭管理节点，同时存储set状态
                    url_manager.save_progress('new_urls.txt', url_manager.new_urls)
                    url_manager.save_progress('old_urls.txt', url_manager.old_urls)
                    return
            try:
                urls = conn_q.get()
                url_manager.add_new_urls(urls)
            except BaseException as e:
                time.sleep(0.1)

    def result_solve_pro(self, result_q, conn_q, store_q):
        while True:
            try:
                if not result_q.empty():
                    content = result_q.get(True)
                    if content['new_urls'] == 'end':
                        print('结果分析进程接受通知然后结束!')
                        store_q.put('end')
                        return
                    conn_q.put(content['new_urls'])
                    store_q.put(content['data'])
                else:
                    time.sleep(0.1)
            except BaseException as e:
                time.sleep(0.1)

    def store_pro(self, store_q):
        output = DataOutput()
        while True:
            if not store_q.empty():
                data = store_q.get()
                if data == 'end':
                    print('存储进程接受通知然后结束!')
                    output.output_end(output.filepath)

                    return
                output.store_data(data)
            else:
                time.sleep(0.1)
        pass


if __name__ == '__main__':
    #初始化4个队列
    url_q = Queue()
    result_q = Queue()
    store_q = Queue()
    conn_q = Queue()
    #创建分布式管理器
    node = NodeManager()
    manager = node.start_manager(url_q, result_q)
    #创建URL管理进程、 数据提取进程和数据存储进程
    url_manager_proc = Process(target=node.url_manager_pro, args=(url_q, conn_q, 'http://baike.baidu.com/view/284853.htm',))
    result_solve_proc = Process(target=node.result_solve_pro, args=(result_q, conn_q, store_q))
    store_proc = Process(target=node.store_pro, args=(store_q,))
    #启动3个进程和分布式管理器
    url_manager_proc.start()
    result_solve_proc.start()
    store_proc.start()
    manager.get_server().serve_forever()























