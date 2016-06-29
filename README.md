# MyCustomTool

## save url tool
虽然有 pocket，evernote 等强大的网页剪辑工具，但是对我并没有那么适用，因为很多网页并不会经常去整理，出于实效性、重要性考虑，自己写了个程序，保存本周必看的精彩文章，用 html 保存，出于自用考虑，格式非常简单，如下。
![](http://7xu83c.com1.z0.glb.clouddn.com/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202016-06-29%20%E4%B8%8B%E5%8D%883.25.09.png)

使用方法
<pre>
$ python saveUrl.py -h
usage: saveUrl.py [-h] [-u URL] [-t TITLE] [-newblock NEWBLOCK] [-b BLOCKNAME]
                  [-newfile NEWFILE] [-f FILENAME] [-c]

optional arguments:
  -h, --help          show this help message and exit
  -u URL              url you want to save
  -t TITLE            title you want to save
  -newblock NEWBLOCK  create a block
  -b BLOCKNAME        save under this block
  -newfile NEWFILE    generate a new file
  -f FILENAME         the file to write, default is weeklyReading.html
  -c                  empty the file
</pre>

Eg.
<pre>
$ python saveUrl.py -newfile weeklyReading.html -newblock 演示 -u http://www.shuang0420.com/2016/06/11/爬虫总结（一）
$ python saveUrl.py -u http://www.shuang0420.com/2016/06/12/爬虫总结-二-scrapy/
$ python saveUrl.py -u http://www.shuang0420.com/2016/06/15/爬虫总结-三-scrapinghub/
</pre>

![](http://7xu83c.com1.z0.glb.clouddn.com/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202016-06-29%20%E4%B8%8B%E5%8D%883.30.21.png)

之后会继续完善，考虑做浏览器插件。
---------------------------------------------------- 我是分割线 ------------------------------------------------------
写完之后才意识到，我做的这玩意儿叫 -- 书签！当我想到这个名词的时候我竟无语凝噎。一定是最近工作太忙脑袋都晕了。。忽略这个工具，愉快的用 chrome 自带的书签吧，它的导出书签功能，其实就是我上面做的这效果了（书签 --> 整理 --> 导出书签）
![](http://7xu83c.com1.z0.glb.clouddn.com/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202016-06-29%20%E4%B8%8B%E5%8D%884.41.02.png)

嗯，收拾收拾书签，一切重新开始～
