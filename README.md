# fofaURLCollect
从FOFA指定关键字采集全中国范围的WEB服务器IP端口或域名地址，无需付费会员（具有时效性，后面如果没法用了，请自行下载源码更改，博主可能懒得个更新~）

脚本使用需要输入三个参数：-s/-o/-c,其中-s后跟FOFA搜索语法，-o后跟采集URL后要输出的文件名，-c后跟登录FOFA后的cookie

示例(搜索使用log4j2相关Web服务器)：

    python3 fofaAssetCollect.py -s=app=”log4j2” -o=”output.txt” -c=”这里写自己FOFA登录后的cookie”
    
搜索结果展示：
![image](https://user-images.githubusercontent.com/58912406/152275975-4e30ae13-4615-49c5-a866-b76f61408b57.png)
