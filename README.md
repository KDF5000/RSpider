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


