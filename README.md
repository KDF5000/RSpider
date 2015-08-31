# RSpider
一个基于scrapy-redis的分布式爬虫模板，在scrapy-redis自带的example的基础上进行修改，添加在实际爬取过程中大部分爬虫可能用到的功能，使的构建分布式爬虫更加的简单。
scrapy-redis: [https://github.com/darkrho/scrapy-redis](https://github.com/darkrho/scrapy-redis)

###安装`Redis`
####`Windows`
`Redis`官网没有`windows`的安装程序，但是微软的`MsOpenTech`团队维护了`Windows`的`Redis`，编译了可执行程序，需要的可以到[https://github.com/MSOpenTech/redis/releases](https://github.com/MSOpenTech/redis/releases)下载
####`Ubuntu`
```
$sudo apt-get install redis-server
```
####`Redis`图形化管理
下载地址：[https://github.com/cinience/RedisStudio/releases](https://github.com/cinience/RedisStudio/releases)

###安装`Scrapy-redis`
`scrapy-redis`GitHub地址：[https://github.com/darkrho/scrapy-redis](https://github.com/darkrho/scrapy-redis)

推荐使用`pip`安装
```
$pip install scrapy-redis
```

###使用`BSpider`
从`GitHub`克隆仓库，克隆成功即可得到一个可以运行的爬虫，该爬虫默认已经配置好了`Redis`,`worker`以及用户代理等功能
```
$ git clone https://github.com/KDF5000/RSpider.git
```
####配置`Scrapy-redis`
`Scrapy-redis`的所有配置到放在`setting.py`的特定位置，如下面所示，每个配置项代表什么意思注释已经详细的说明，不需要过多解释，如果不想使用`Scrapy-redis`将所有配置项注释掉即可

```
# 修改scrapy默认的调度器为scrapy重写的调度器 启动从reids缓存读取队列调度爬虫
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

# 调度状态持久化，不清理redis缓存，允许暂停/启动爬虫
SCHEDULER_PERSIST = True

# 请求调度使用优先队列（默认)
#SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'

# 请求调度使用FIFO队列
#SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderQueue'

# 请求调度使用LIFO队列
#SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderStack'

# 最大的空闲时间，避免分布式爬取得情况下爬虫被关闭
# 此设置只适用于SpiderQueue和SpiderStack
# 也是爬虫第一次启动时的等待时间（应为队列是空的）
#SCHEDULER_IDLE_BEFORE_CLOSE = 10

# 存储爬取到的item，一定要在所有的pipeline最后，即设定对应的数字大于其他pipeline
ITEM_PIPELINES = {
    'RSpider.pipelines.BaseSpiderPipeline': 256,
    'scrapy_redis.pipelines.RedisPipeline': 300
}

# 指定redis的地址和端口(可选，程序将使用默认的地址localhost:6379)
REDIS_HOST = 'localhost'
REDIS_PORT = 6378

# 声明redis的url地址（可选）
# 如果设置了这一项，则程序会有限采用此项设置，忽略REDIS_HOST 和 REDIS_PORT的设置
#REDIS_URL = 'redis://user:pass@hostname:9001'
```


####配置`graphite`
##### 安装`graphite`
目前`graphite`不支持`Windows`,所以使用`Windows`的用户要么在自己电脑搭个虚拟环境，要么在一台可以访问的`Linux`主机搭建该服务。如果有时间研究一下`Docker`自己写个镜像。
具体安装参考[Ubuntu 14.04 安装图形监控工具Graphite](http://kdf5000.github.io/2015/08/28/Ubuntu-14-04-%E5%AE%89%E8%A3%85%E5%9B%BE%E5%BD%A2%E7%9B%91%E6%8E%A7%E5%B7%A5%E5%85%B7Graphite/)

##### `Scrapy`配置`graphite`
该模板源码自定一个`scrapy`的[Stats Collection](http://doc.scrapy.org/en/latest/topics/stats.html),封装了`graphite client`使用[plaintext protocol](http://graphite.readthedocs.org/en/latest/feeding-carbon.html)发送数据到`graphite`所在服务器的`Carbon`,客户端的使用可以查看`statscol/graphite.py`文件

####无图无真相
![](http://7sbpmg.com1.z0.glb.clouddn.com/img_scrapy_graphite_cmd.png)

![](http://7sbpmg.com1.z0.glb.clouddn.com/img_scrapy_graphite.png)