"""
1242. Web Crawler Multithreaded
"""

from queue import Queue
import threading

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        def hostname(url):
            # return url.split("/")[2]
            start = len("http://")
            i = start
            while i < len(url) and url[i] != "/":
                i += 1
            return url[start:i]

        seen_lock = threading.Lock()
        seen = set([startUrl])
        queue = Queue()
        queue.put(startUrl)
        startHostname = hostname(startUrl)
        ret = []

        def worker():
            while True:
                cur = queue.get()
                if cur == None:
                    return

                for url in htmlParser.getUrls(cur):
                    if startHostname == hostname(url):
                        with seen_lock:
                            if url not in seen:
                                queue.put(url)
                                seen.add(url)

                        # seen_lock.acquire()
                        # if url not in seen:
                        #     queue.put(url)
                        #     seen.add(url)
                        # seen_lock.release()
                queue.task_done()

        num_workers = 8
        workers = []
        for i in range(num_workers):
            t = threading.Thread(target=worker)
            t.start()
            workers.append(t)

        queue.join()
        for i in range(num_workers):
            queue.put(None)
        for t in workers:
            t.join()

        return list(seen)
