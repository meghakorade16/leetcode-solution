from queue import Queue
from threading import Thread

class HtmlParser(object):
    def getUrls(self, url):
        """
       :type url: str
       :rtype List[str]
       """


class Solution:
    def gethostname(url: str):
        return url.split('/')[2]

    def crawl(startUrl: str, parser: HtmlParser):
        answer = set()
        hostname = Solution.gethostname(startUrl)
        q = Queue()

        def worker():
            nonlocal hostname, parser
            while True:
                url = q.get()
                if url not in answer and Solution.gethostname(url) == hostname:
                    answer.add(url)
                    for u in parser.getUrls(url):
                        q.put(u)
                q.task_done()

        for _ in range(4):
            Thread(target=worker, daemon=True).start()
        q.put(startUrl)
        q.join()
        return list(answer)


if __name__ == '__main__':
    Solution.crawl('http://news.google.com', htmlParser=HtmlParser)
