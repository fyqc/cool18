# 从零开始，对本代码从头到尾完整细致的梳理与说明 暨 记述作为初学者在Python学习实践中遇到的匪夷所思的奇怪困扰与和层出不穷的错误绞尽脑汁进行排故的奇妙经历

## 新修订的说明

差不多一年半以前，那时候新冠疫情还在全世界蔓延，我也还赋闲在家，Python在互联网上的热潮还未消退，到处都是《学Python，找高薪工作》之类的文章和视频。因为确实有很多的时间，就捣鼓了一点代码，搞了几个晚上，爬取到了不少《留园》上的小说，所以有感而发，写了第一版的说明。

没有做任何的宣传，却得到了一些陌生网友的认可与鼓励，还有朋友提出来代码中存在的问题，实在是不胜欢喜。

而十几个月过去，世界也发生了很大的变化，我本人又回到了忙碌的工作中，空闲时间的大幅减少，以及兴趣的转移，让我对这个一年半之前的项目没有再过问过。

虽然在这段时间里，我的技术有了一点点的进步，也跟着好几本书和一些网络上的教程后面学到了不少新的知识，也纠正了不少我以前的错误认知，觉得是时候再对这个代码做一些修订与改正，提高一下运行的效率。

加上好久没有上《留园》，说不定他们也改版了，前一版的代码还能不能正常运行也实在是要打一个问号，就趁着靠近年末暂时安稳无事，抓紧时间写一个新修版的攻略好了。

### 和之前版本的异同

之前使用的Python版本是3.8.10，这一次使用了Python 3.10.8 64-bit版本，编辑器也来到了Visual Studio Code （版本1.72.2），安装了如下插件：Python（v2022.16.0）， Pylance（v2022.10.10），操作系统使用了Windows 11 Pro 22H2。

虽然看起来与前一版有了很大的版本差异，但是用到的依赖库基本上还是原来那些，函数看起来也没有什么变化，所以按讲在之前的平台上也能够运行的很好。

---

## 引子

开始学Python的动机很简单——就是为了下载 [数字尾巴](https://www.dgtle.com) 上的高清图片。尝试用了很多的下载软件，哪怕像Firefox中DownThemAll！这样优秀的插件，也需要我先手动保存一个包含了所有图片地址的下载列表，再用记事本打开。用替换功能把链接中缩略图的参数去除掉，以得到高清的原图地址，再导回下载器才可以批量下载到高清的原图片。

而在Firefox版本升级的过程中因为抛弃了Legacy模式，对插件引入了新的限制而让DownThemAll！插件的作者愤怒地表示再也不要给Firefox开发新插件了，让我一度很惶恐，以为再也下不到图片了。

当然他后来还是开发了新版本的DownThemAll！，虽然比以前变得难用的了，可也实在是让人很汗颜。

费尽千辛万苦下载完图片之后，还要归类整理，需要我手动操作，把每一个作者的id单独记下来建立一个文件夹，再把图片全选，剪切粘贴到它们所属的文件夹里面去。效率很低，还很容易出错，那时候我每周都要花好多时间来做这件事情。

计算机的伟大就在于它可以把人类从这样枯燥而重复的单调工作中解脱出来，IT界又有着伟大的开放传统，从业人员既谦卑又博学，互联网上的资料汗牛充栋，只要真心想学，网络上处处都是资源。

因为本身就对计算机比较感兴趣，又花了点时间，很快就入门，接连写了好几个程序，感觉自己的知识水平也在蹭蹭地上升。

诚然，学然后知不足，越是学习，就越觉得，对于Python，我其实还只是一个门外汉，它里面有太多的精髓令人望而兴叹，真正能够精通怕不知是何年何月。好在就当下而言，用它能够实现我的诉求，对于不靠它吃饭的我来说，就已经足够了。

虽然网上有很多人嘲笑Python的速度慢，说什么C++比它快200倍什么的，许是因为我爸爸没有钱，家里用的都是丐版配置的机器，对于计算机一向运行起来慢慢吞吞这种事，我已经习惯了。

当Python代码在我的计算机上运行起来的时候，一行行的字符刷的一闪而过，这速度已经快得让我受宠若惊了，快得让我眼花缭乱，感觉我思考的速度还远远不能跟上它运行的速度。至于说Python比其它语言慢什么的，反正NASA又不需要靠我的代码去登月，我们就只是爬小说而已，早一点晚一点没什么大不了啦。

这一次写的攻略，是我一段时间以来所学会的各种技术的综合演练，把它写下来，一方面满足自己人菜瘾大的创作欲望，另一方面也为有缘看到本文的朋友们当一个参考。倘若真的有人从中间得到帮助，少走一些弯路或者得到一些启发，那真的是一件非常开心的事情。

---

### 本代码的诉求

看到 [留园网](https://www.cool18.com) 的 [禁忌书屋](https://www.cool18.com/bbs4/index.php?app=forum&act=gold) 版块里有许多 ~~让人看了欲罢不能的~~ 少儿不宜的读本。

每次举着手机躺在床上刷，排版和广告都很令人头疼，本来因为人手不大胳膊也没什么力气才特意买的小屏手机，重量轻了但是显示面积也小，就这样还要被网页上各种加载的广告和图片占掉一大截空间。闪来闪去的广告一不留神手滑点到了会影响阅读的流畅不说，也很影响手机的续航。插着充电线躺着床上，翻身都不自由，手机还会发烫。因此，就有了把它们保存成为txt格式，再引入手机，用专业的看书软件打开慢慢看的想法。

如果只是一部短篇小文，那么用电脑浏览器打开，复制保存到记事本中尚还能够接受，可如果想要把一部八十几章，每章都分成好几百个单独网页的长篇连载都打开，一个一个手动保存，既费时费力，还很容易出错。要是看到一半，发现章节顺序出错，或者情节不连贯，那真是扫兴极了。

这种枯燥、繁复的工作，就交给我们的Python程序去做就好啦。

这一次的代码，就是要用Python来批量保存*禁忌书屋*中的所有小说读本，并以<u>读本的名字</u>作为 `文件夹` ，里面的每一个单独的帖子都以<u>该帖子的名字</u>作为 `文本文件的文件名` 保存在该文件夹内，文本文件的编码格式选用UTF-8，以尽量保证兼容性，减少出现乱码的可能。

---

### 约定

假定本文的阅读者熟悉计算机操作及互联网概念，且有一定的Python基础。

代码的编写规范遵循PEP8的指导，参照了 [Google的相关代码编写指南](https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_style_rules/) 。

虽然是一个业余的计算机爱好者，但业余并不等于胡来，还是要在力所能及的范围内把事情做到位，做得尽可能正确。

考虑到文本文件本来也没有多大的体积，不像图片下载起来很慢，就没有上多线程来提高下载的效率了。一方面降低复杂度，二来也减少对《留园》服务器的压力。章节一个一个的拉取，一秒钟跳个两三行的指令，我觉得已经是极限了。满屏幕的信息，倘若滚动地太快就根本来不及看，很容易头晕。

人脑的处理速度就这么快，代码试运行的时候得看着Powershell的输出，以便知晓自己程序的运行情况，万一不对好及时中断。

---

### 关于本代码的版权

感觉简体中文互联网这些年蔓延了一股很浮躁的氛围，许多人的视频和文章稍微放一点点东西出来就急不可耐地开始收费，要求扫码，要求打赏。

这一点不得不佩服人家情色小说的作者，大部分人无私奉献，用爱发电，给我们贡献了这么多文学的经典，而我不过是站在巨人们的肩膀上，只做了点微小的贡献，加上我也完全不靠这个养活自己，所以尽管本代码采用了GPL-3.0的版权声明，但是看到本文的诸君，尽可以大大方方地把本文拿去转载，在本代码的基础上进行二次开发，不用特意跑来通知我一声。不仅是我这个仓库里的代码，其它仓库里凡是我所写的代码，也尽可以拿去用。

当然免不了有些朋友从我这里免费获得之后，再向别人兜售获利，我无暇也无意去一一追讨，只能说做人境界不一样，人生追求不一样，自私的人总是有的，作为前总理的忠实信徒，我还是相信一个开放的互联网会让所有人受益，相信**天下为公**的。

---

## 正式开始

说了半天，让我们进入正轨，开始展示代码。

### 文件头

首先，在VS Code中创建一个py文件，为了和第一版代码相区分，这里我给它起名为 `study2.py` 。

相较于建立一堆文件，然后把函数来回互相引用，我还是喜欢把所有的函数都放在一个文件里，这样文件夹显得清爽一些，反正整个程序也没有超过1000行，来回多划拉几次，有需要的时候分左右两个屏对比前后来看看也就够了。

面对一个全新的空白的py文件，第一件事，让我们来创建一个注释，加上今天的日期：

```python
# 2022年10月30日
```

这样做，是为了实现简单的版本管理，假设你也像我一样有不止一台计算机，那么从一台计算机复制到另一台计算机上去执行的时候，有时候会临时修改代码，那么每次修改之后如果及时更新这里的日期，那么两台计算机上的Python代码文件里的日期就会不一样，从而得知哪一个是较新的版本。

接下来开始引入运行时所依赖的库：

因为是网络爬虫，需要与《留园》的服务器建立链接，并解析它家的静态HTML页面数据。

所以这里用了两个大名鼎鼎的Python库，一个叫做 [Requests](https://docs.python-requests.org/en/master/) ，一个叫做 [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.html) 。

二者都可以通过pip来安装，Windows下是执行下述命令：

```cmd
pip install requests
```

```cmd
pip install beautifulsoup4
```

又因为我们要操作并保存文本文件，建立文件夹，所以还需要导入Python自带的os库。

注意，有很多文章与教程只说用BeautifulSoup就好，但是BeautifulSoup推荐使用的 `lxml` 解析器也是需要 [单独安装](https://lxml.de/) 的。

```cmd
pip install lxml
```

按照惯例，把库放在整个文件最开始的地方。

```python
import os
import requests
from bs4 import BeautifulSoup
```

有些稍微过时的教程说Python文件的开头应该放一个叫做#shebang的东东，如下所示：

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
```

这个东西的作用是让Python解析器知道你的文件的编码是UTF-8，从而避免对中文的显示产生乱码。不过我看了一下Python的官方文档，和一些新一点的教程，大家表示这东西在Python 2的年代曾经很有用，如今在Python 3的时代，因为解析器已经是默认文件编码是UTF-8，所以这两行不再需要了。

IT技术变化日新月异，许多时候你找到的教程一看创作时间在好几年之前，你复制下来他的代码，运行了一下发现根本跑不通，那并不完全是因为作者水平不济，很有可能只是时代变了，当时工作的代码所依赖的环境变化了，所需要爬取的网站也改版了，所以那一段代码如今已经不能正常工作了。

想要确认是不是UTF-8很简单，在VS Code的右下角可以看到当前的编码，如果写着 `UTF-8` 那就说明该文档是UTF-8编码。

### 声明常量

这是一个我在学习C语言的时候学到的好习惯，即把那些不会变的常量先声明在最前面，这样修改的时候就很方便，一目了然。比如先指定文档保存的路径，这样无论把这个代码复制到哪个目录去执行，输出的路径都不会改变了。要不然总是默认在Python文件所在的目录下产生大量的文件，清理起来也很麻烦的。

```python
HEADER = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0)'
    ' Gecko/20100101 Firefox/106.0',
}

SAVE_DIRECTORY = r'D:\Rilla\cool18'
```

上述先定义了 `请求头（HEADER）` ，这是HTTP传输协议的请求头，为了欺骗网站，将我们的爬虫程序伪装成一个浏览器。

对于大度的《留园》而言，它对于请求头还是睁一只眼闭一只眼的，因此我们的爬虫爬取它的信息还是比较容易，无愧于一个优秀海外中文网站的楷模。

 `HEADER` 的获取可以在浏览器的开发者工具中找到，也可以在网上搜。这里我用我的FireFox中所提供的。有的朋友的Header会和我的不一样，长度会长于我这个，当Header的原值特别长的时候，为了显示效果，可以如本例所示，在中间做一个截断。Python会对字典中两个相邻的字符串做自动拼接，所以只要保证上一行与下一行都有各自的引号，且第二行开始的位置与第一行相同，是不会影响到字符串的效用的。

接着定义了 `文件的储存目录（SAVE_DIRECTORY）` ，这样是为了将来如果有需要，可以随时方便地修改为其它的中意的目录，待会儿我们爬取到的文章就会在该路径下源源不断地生成。

### 第一个函数与程序入口:

```python
def get_soup_from_webpage(url, header):
    response = requests.get(url, headers=header, timeout=15)
    if 'classbk' in url:
        response.encoding = 'gb2312'
    else:
        response.encoding = 'utf-8'
    content = response.text
    soup = BeautifulSoup(content, 'lxml')
    return soup
```

第一个函数 `get_soup_from_webpage(url, header)` 的作用是从一个指定的网页URL中返回BeautifulSoup格式，方便后续从里面解析出我们需要的东西，包括网页的标题，正文的字符串，以及超链接等等。

这里的 `url` 是需要解析的网页的地址，类似于 `https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.html` 。通常以http或者https来开头，以html结尾。

同时，作为函数的参数，它必须是一个字符串，所以传入的时候要加上单引号或者双引号。

```python
if 'classbk' in url:
    response.encoding = 'gb2312'
else:
    response.encoding = 'utf-8'
```

这一段是因为网站的历史变迁缘故，在某一年之前的网页，它们的编码并不是默认的UTF-8，而是GB2312。

如果统一以UTF-8来解码，就会得到一个全是乱码的结果，后面的所有分析都无从谈起。

好在以GB2312编码的网页，数量稀少，而且就目前来看，URL中都包含有关键字 `classbk` ，所以写了一个判断语句，根据需要来调用不同编码来解码。

最后加上一个 `timeout` 参数，设定为15秒钟，如果因为网络不通畅的关系导致获取失败，及时中断，不要吊死在这。

---

### 第二个函数

```python
def main_page_url_generator():
    '''
    翻页系统，生成留园主页第一页到第十八页的地址
    '''
    article_page_url = []
    main_page = 'https://www.cool18.com/bbs4/index.php?app=forum&act=gold'  # 禁忌书屋首页
    article_page_url.append(main_page)
    for page in range(2, 19):
        newpage = "".join([main_page, '&p=', str(page)])  # 第2页到第23页的地址
        article_page_url.append(newpage)
    return article_page_url
```

顾名思义，第二个函数 `main_page_url_generator()` 的作用是生成首页的url，并以列表的形式返回这23个url，也就是返回包含了23页中每一个页面中200个帖子地址的列表。

具体说来是什么意思呢？

禁忌书屋的第1页的地址是`https://www.cool18.com/bbs4/index.php?app=forum&act=gold`

第2页的地址是`https://www.cool18.com/bbs4/index.php?app=forum&act=gold&p=2`

第3页的地址是`https://www.cool18.com/bbs4/index.php?app=forum&act=gold&p=3`

通过幼儿园数学找规律的知识，不难发现，第2页就是在第1页的基础上多了后面的 `&p=2` 而已。

推而广之，第n页就是在第1页的url后面加上 `&p=n` 。

当然，虽然作者众多，文库里面的书也着实很多，但是山高也有边，水长也有源，每页200篇书目，到今天为止，一共23页也就到头了。所以最后一页是 `&p=23` 。

我们不是“万字”寓言中那个小孩，应该不会有人会把每一个url都列出来这么傻，我们只要写一个循环，让它自动生成<u>包含2到23的url列表</u>就好了。

Python的基础教程提到过，想要生成1到23的数字，有一个叫做 `range` 的函数，它的用法是前面是闭区间，后面是开区间。也就是说我们的 `range(2, 24)` 实际上是生成一个开始包含2，结尾不包含24（也就是以23结尾）的全自然数的数列。

代码中用到了 `join` 函数来拼接字符串。

```python
"".join([main_page, '&p=', str(page)])
```

对于字符串的拼接，一定要确保拼接的都是字符串，即先使用 `str()` 把page得到的自然数从 `int` 类型转换成 `str` 类型。不然就会报错，告诉你不能把 `str` 和 `int` 拼接。

使用 `join` 而不是使用简单的一个 `+` 来连接字符串的好处在于，这个代码即使被运行在其它的操作系统下，也可以最大程度地保证执行的可靠性。

尤其是在拼接路径的时候，要使用 `os.path.join` 函数来避免非Windows系统对文件夹的报错：

> [macOS 文件夾錯誤 #1| popoko1379 opened this issue on Aug 23](https://github.com/fyqc/cool18/issues/1)

---

### 第三个函数

```python
def get_articles(url, header):
    '''
    拿到所有的文章的列表

    返回包含200篇文章的列表
    '''
    article_list = []
    soup = get_soup_from_webpage(url, header)
    # <ul id="thread_list">
    tag_ul = soup.find('ul', id="thread_list")
    for a in tag_ul.find_all('a'):
        href = a.get('href')
        href = href.replace('&amp;', '&')
        if 'http' not in href:
            url_with_https = "".join(
                ['https://www.cool18.com/bbs4/', href])
            article_list.append(url_with_https)
        else:
            article_list.append(href)
    return article_list
```

接下来写第三个函数， `get_articles(url, header)` 。

如函数文档的说明所言，它的功能就是从首页上获取那200篇文章中每一个文章的页面地址，并返回包含这200个url的列表。

这里介绍一下html的小知识，html中所有的元素都是以块的形式呈现的，比如一个html页面会放一个叫做 `<body>` 的块，下面有好几个 `<table></table>` ，里面可以放一堆导航条，比如在第一个里面塞上“首页”“漫画”“赛事”之类的东西，第二个 `<table></table>` 里面放些“点赞”“投币”之类的东西，第三个第四个第五个依次排列在网页上……

由于分析了网页的源代码，发现所有的文章的列表都在 `<ul id="thread_list">` 子节点下，所以用 `tag_ul = soup.find('ul', id="thread_list")` 在soup对象中把相应的HTML标签提取出来。

```python
for a in tag_ul.find_all('a'):
    href = a.get('href')
    href = href.replace('&amp;', '&')
    if 'http' not in href:
        url_with_https = "".join(
            ['https://www.cool18.com/bbs4/', href])
        article_list.append(url_with_https)
    else:
        article_list.append(href)
return article_list
```

到了这一步，我们已经定位并拿到了所需要的这一个 `ul` 的标签里面的所有内容，接着使用代码把里面的所有超链接的部分提取出来。

众所周知，留园家的超链接长这样：

`<a href='https://www.cool18.com/bbs4/index.php?app=forum&act=threadview&tid=14135342'>第一章</a>`

因为具体的文章的地址是通过超链接标签 `<a>` 的形式外链的，所以接下来我们使用了 `soup.find_all` 来把所有的a标签，也就是超链接提取出来，再从提取出来的包含所有超链接（a标签）的列表中，做一个循环，用 `.get` 方法依次提取href属性的内容。

由于html中， `&` 并不合法，所以bs4会使用 `'&amp;'` 作为转义字符，如果我们直接把它输入到url中，就会导致出现解析错误，所以使用 `replace` 函数把它替换（还原）回原本的样子。

下面那段是因为部分页面提取出来的时候长下面这样：

`index.php?app=forum&amp;act=threadview&amp;tid=14135342`

通过与浏览器地址栏的对比，发现少了前缀： `https://www.cool18.com/bbs4/` 。

聪明的同学说，得之矣，用 `join` 函数把它拼接起来就好啦。

没错，可是，问题又来了，《留园》的某些页面是带有完整的前缀的，倘若你这样不分青红皂白就拼接，就会出现如下所示很搞笑的情况：

`https://www.cool18.com/bbs4/https://www.cool18.com/bbs4/index.php?app=forum&amp;act=threadview&amp;tid=14135342`

到时候等待你的就是一个残酷的报错。

解决方案：我是一个业余爱好者，爱好者也不懂技术，采用的方法简单粗暴：判断http在不在里面，如果解析出来的url里面有 `http` 在，就不加前缀；如果 `http` 不在其中，就说明没有前半段，就调用 `join` 把前缀给加上去。

这里还有一个坑，有同学说，那我用 `https` 作为判断不是更好吗？

理想是美好的，现实是残酷的，有时候解析出来的是 `http不加s` 后面跟着一长串， `http` 跟 `https` 比，不过是安全性差了点，但它当然也是一个合法的url。这里如果以 `https` 作为关键词，代码在碰到 `http` 的时候就会认为没有前缀，于是再加上一个前缀，你就有了两个前缀，仍然以报错收场。

把url添加到列表的时候，为了区分加了前缀的，和原生的不需要加前缀的url，它们的变量名是不一样的，注意不要添加错了。

---

### 第四个函数

```python
def find_title(soup):  # 寻找文章的标题
    title_may_none = soup.title
    if title_may_none:
        title = title_may_none.get_text()
        title = title.replace(' - cool18.com 书库', '')
        title = title.replace(' - cool18.com', '')
        title = title.replace('\\', '_')
        title = title.replace('/', '_')
        title = title.replace(':', '_')
        title = title.replace('*', '_')
        title = title.replace('?', '_')
        title = title.replace('"', '_')
        title = title.replace('<', '_')
        title = title.replace('>', '_')
        title = title.replace('|', '_')
        title = title.replace('\t', '_')
        title = title.replace('\r', '_')
        title = title.replace('\n', '_')
        title = title.strip()
        return title
    else:
        return None
```

接下来写一个函数 `find_title(soup)` 来提取页面的标题，以 `soup` 作为输入的参数。

所以它是用上面第一个函数的解析出来的soup作为参数输入，从里面筛找，返回符合要求的 `标题（title）` 。这个标题等会儿就用来命名我们的 <u>文件夹和文本文件</u> 。

许多人说你这里搞这么多 `replace` 干嘛，那是因为总有些不走寻常路的作者天马行空，在网页的标题里弄一堆非法字符，如果不加以筛选，就直接用来创建文件夹，就会出错。

计算机的操作系统限制了文件名中有一堆字符是不可以用的，需要把它们统统删除掉或者替换成下划线。此外每一个文章标题里都跟着 ` - cool18.com 书库` 和 ` - cool18.com` ，像小广告一样很烦，把它们用不存在的“空”给替换掉，也就是删除掉。

如果不这样竖着排列，要用一字长蛇阵，也就是所谓的chain，看起来非常长，显得不美观，不方便注释，也不方便后续删改。

最后那几个是最坑的，谁能想到茫茫文海中居然有人在标题里插了一个制表符 `\t` ，结果制表符当然从肉眼上看和空格也差不多，但是并不能当做文件名，就会报错。真是令人大跌眼镜。

PS：

如果说插入制表符 `\t` 还能够原谅，那在标题里插入换行符 `\r` 和 `\n` 的，简直是泯灭人性。可是文章看多了，这样的奇事总是有，只好加以针对处理之。

用 `strip` 来去除头尾的空格，有同学要问，你为什么要把 `strip()` 放在最后呢？

那是因为我们要os库的新建文件夹是以我们传入的 `title` 作为参数，如果 `title` 的末尾有空格，比如 `《金庸列女传》全集 ` （注意最后有一个空格）和 `《金庸列女传》全集` （最后没有空格）在 `os.path.exist()` 中是被对待为等同的。

但是当你到了后面文本保存的那一刻， `《金庸列女传》全集 \金庸列女传.txt` 和 `《金庸列女传》全集\金庸列女传.txt` 是完全不同的路径，在写入文本文件的时候就会产生路径不存在的报错。

因此在替换完所有的非法字符之后再在最后一步进行删除左右的空格的操作，是很有必要的。

有时候，网页会被跳转，比如原帖被删除了，这种时候， `soup` 虽然可以得到，但是从 `soup` 中什么都解析不出来，只能返回一个空值 `None` ，如果我们继续使用 `strip()` 函数，就会报错。从一个不存在的对象中，当然也无法继续后续的诸多操作，因此要及时放弃，中断循环。

所以先判断有没有合法的返回值，如果没有，就返回 `None` ，在后续的代码中，如果拿到 `None` ，就说明网页这里被跳转了，就可以及早触发中断循环的操作，避免后续的错误。

---

### 第五个函数

```python
def file_name(title):
    return "".join([title, '.txt'])
```

接下来这个函数的作用就是在title后面加个 `.txt` ，简单易懂。

---

### 第六个和第七个函数

```python
def extract_text(soup):
    try:
        pre = soup.find_all('pre')
        for word in pre:
            raw_words = word.get_text()
            raw_wo_cool18 = raw_words.replace(
                '　　', '\n').replace('cool18.com', '').replace('www.6park.com', '')
            raw_wo_blank = raw_wo_cool18.replace('', '\n').replace(' ', '')
            paragraph = raw_wo_blank.strip()
            return paragraph
    except:
        input("啊哦，好像有点不对劲，检查一下代码吧。按任意键继续")


def extract_classbk(soup):
    try:
        pre = soup.get_text()
        raw_words = pre.replace('www.6park.com', '').replace('6park.com', '')
        return raw_words
    except:
        input("啊哦，好像有点不对劲，检查一下代码吧。按任意键继续")
```

接下来是文章分析器的函数 `extract_text(soup)` 和 `extract_classbk(soup)` ，用来提取正文。

之所以写了两个函数是对应新版与旧版的网页，它们的结构不同。

这个没有什么特别省事的方法，只能没完没了一点一点对照html的源码，一点点地调试，看看出来的是什么。

有关BeautifulSoup（以下简称bs4）的用法，官网有很详细的说明，CSDN上也有一些教程，主要的几个用法就是从HTML的标签中提取出我们需要的信息，不管是字符串还是a标签（超链接）的属性（也就是链接），都可以轻松使用bs4来提取，并保存到列表，为后续的去重做铺垫。

 `input()` 函数在这里起到的作用是提供一个暂停的机会，等待键盘的响应。如果只是放一个print在这里，等错误产生的时候，你可能完全没有注意到，就一闪而过，被后续的信息给淹没，完全没有注意到它。

---

### 第八个函数

```python
def create_folder_as_per(foldername):
    if not os.path.exists(foldername):
        os.makedirs(foldername)
        print(f"建立文件夹{foldername}")
    else:
        print(f"{foldername}文件夹已经存在")
```

创建 `create_folder_as_per(foldername)` 函数用来建立文件夹。

为了实现代码功能的构想，需要输入一个文件夹的名字，得到一个文件夹。

出于~~省事~~迁移方便的目的，选择在 `study2.py` 所指定文件夹，也就是开头 `SAVE_DIRECTORY` 处建立新的子文件夹。

用 `if not os.path.exists(foldername)` 来判断文件夹是否已经存在，如果存在就打印一条提示语句，不存在的情况下才建立文件夹，避免浪费和重复。

---

### 第九个函数

有时候看文章看到结局，发现文章不全，里面充斥着乱码，或者干脆打开发现是一个空文件，这时候往往陷入自我怀疑：

是不是我的代码写得不对，文章没抓取完全，还是我的阅读器没有设置好编码，究竟是哪里出了问题，乱码是从哪冒出来的？

这时候，如果在文章的末尾加上一个出处，记录下这个页面是从哪个网址扒下来的，那可就太有用处了。

所以创造函数 `rilla_save(path, para, url)` 来在文本的末尾实现添加出处，并将**规定的文本**写入**规定的路径、规定的文件名**的txt文件中的功能。

```python
def rilla_save(path, para, url):
    paragraph_with_footer = "".join([para, '\n', '\n', '页面来源： ', url])
    with open(path, 'wt', encoding='utf-8') as f:
        f.write(paragraph_with_footer)
```

函数参数 `path` ， `para` ， `url` 的意义分别是：

 `path` 是要保存的文本文件的绝对路径

 `para` 是paragraph的缩写，意为段落，当然就是从上面解析出来的正文段落

 `url` 是要附加的页面地址。

用 `join` 函数把它们连在一起就好了。

里面的两个 `'\n'` 的作用是插入两个 `“换行”` ，如果没有换行，直接紧跟在正文的文本后面，一来不容易看到；二来也没有层次感，破坏了看文的好心情。

这样任何一个txt文件打开，拉到最后，就能看到文章来源，如果有疑问，在怀疑自己之前，先去网页上看一眼。看了之后就会发现，啊，原来网站上原文就是一堆乱码，就是空白页，就是写到一半没有然后了。

宽恕自己，善莫大焉。

再用 `with` 语句，以UTF-8的编码创建并写入文本文件。打开模式选择 `'wt'` ，是 `write text` 的缩写，它是覆盖型的，这里是创建新文件，所以无所谓覆盖。

使用 `with` 语句好处多多，首先是能够确保打开的文本文件会被正确的关闭，有些老掉牙的教程会教你用 `.open()` 、 `.write()` 和 `.close()` 来处理文本文件的写入，那种写法已经过时了，2022年，时代进步了，咱们也要与时俱进啊～

至于函数名中的Rilla，ヽ(*ﾟдﾟ)ノｶｲﾊﾞｰ

---

### 第十个函数

```python
def rename_and_savetext(folder, txt_name, para, url):
    '''
    以页面的标题作为文件夹的名字，把所有的txt保存在这个文件夹内
    '''
    txt_path = os.path.join(folder, txt_name)
    if not os.path.exists(txt_path):
        rilla_save(txt_path, para, url)
    else:
        print(f"啊哦，想要下载的文件 {txt_path} 已经有了，加个_2")
        auto_rename_2 = txt_path[:-4] + '_2' + '.txt'
        if not os.path.exists(auto_rename_2):
            print(f"新文件将被命名为{auto_rename_2}")
            rilla_save(auto_rename_2, para, url)
        else:
            print(
                f"啊哦，想要下载的文件 {auto_rename_2} 已经有了，算了，用url来命名吧。")
            giveup_name = url.split('tid=')[-1] + '.txt'
            giveup_path = "".join([auto_rename_2[:-4], '_', giveup_name])
            rilla_save(giveup_path, para, url)
```

接下来放大招啦！这个函数 `rename_and_savetext(folder, txt_name, para, url)` 是整个代码中最有技术含量的部分，纵使时隔一年半，看起来依然陶醉不已，觉得自己真是好厉害的说。

函数很长，看起来有点头晕，所以我们分段讲解。

首先是参数，其实参数一般都是先写完函数，看看缺什么，往里填什么。

四个参数 `(folder, txt_name, para, url)` 里面：

 `folder` 自然就是文件夹的名字

 `txt_name` 是文本文件的名字，也就是那个网页的标题

 `para` 是正文内容

 `url` 是网页所在的地址

```python
txt_path = os.path.join(folder, txt_name)
if not os.path.exists(txt_path):
    rilla_save(txt_path, para, url)
else:
    print(f"啊哦，想要下载的文件 {txt_path} 已经有了，加个_2")
    auto_rename_2 = txt_path[:-4] + '_2' + '.txt'
    if not os.path.exists(auto_rename_2):
        print(f"新文件将被命名为{auto_rename_2}")
        rilla_save(auto_rename_2, para, url)
```

在我的构想中，一个小说应该是放在同一个文件夹里面。
比如著名的《金鳞岂是池中物》，就是一个文章，正文所在全是链接，点进去一个章下面居然又在回帖区充满了各种链接。

我们固然要谴责这种套娃的恶劣行径，另一方面也不能束手无策，还是要运用智慧加以解决之。

首先用改良过的 `os.path.join` 函数来拼接文件夹和文本文件的文件名，形成一个完整的 `路径` 。

如果**没有重名**，直接给 `路径` ，和 `正文的内容` ，还有 `文章的地址（url）` 调用上一步创建的 `rilla_save()函数` 就直接保存了。

然后考虑到帖子有时候有重名的时候，尤其是某个作者会写上百章的长篇小说，写到后面他也想不起来这是第几章，就会出现两个788章，却没有789章这种事。

其实这有时候也不能怪发帖者，情色小说嘛，很多电子情色小说最早起源于上古时代的元元图书馆，经过这么多年的转载、转载、转载，早就被水印、回复可见等等篡改地面目全非，全本本来就很难得，更多的已经散佚了。能有些热心人士靠着热情服务社区，给大家提供自己搜集来的各种版本，本来就不应加以苛责才是。

其实我说了这么多，就是想说，有相当数量的文章都不是作者亲自发布，而是时隔多年后由一个不相干的人来转载。那转载的人一天要转载那么多文章，错漏在所难免。

当然，我们“宁可放过三千，不可错杀一个”。与其粗暴选择覆盖，不如重命名，比如加一个_2在后面。

同时，在遇到这样的情况时，因为特别常见，如果每次都报错，停下来人工处理，就很耽误时间，不妨让程序自动处理。

这里注意到用了切片的方式来处理字符串，把原先路径中处于最后的四个字符，也就是 `'.txt'` 去掉。

有人想说为啥不能用 `-` 来做这件事，像下面这样呢？

 `auto_rename_2 = txt_path - '.txt' + '_2' + '.txt'` 

想法是好想法，可是Python中只有 `+` 作为连接符，并没有把 `-` 当做删减的符号。

可惜了，只能曲线救国啦。当然，用`replace`也是可以的，毕竟除了格式名，不太可能会有`'.txt'`出现在文件名和其它位置。

```python
else:
    print(f"啊哦，想要下载的文件 {txt_path} 已经有了，加个_2")
    auto_rename_2 = txt_path[:-4] + '_2' + '.txt'
    if not os.path.exists(auto_rename_2):
        print(f"新文件将被命名为{auto_rename_2}")
        rilla_save(auto_rename_2, para, url)
    else:
        print(
            f"啊哦，想要下载的文件 {auto_rename_2} 已经有了，算了，用url来命名吧。")
        giveup_name = url.split('tid=')[-1] + '.txt'
        giveup_path = "".join([auto_rename_2[:-4], '_', giveup_name])
        rilla_save(giveup_path, para, url)
```

 `if`，`else` 的结构在这里非常容易理解，一个不行就找另一个，总有一个适合它。

当_2也重复的时候，为了防止无限套娃，出现`_2_2_2_2`这种长的离谱的后缀，应考虑用不同的规则来命名文件。

通常说来，帖子的id应该是唯一的，也就是`tid＝`后面那一串数字。这里使用`split('tid=')[-1]`函数加切片，以`tid＝`为界，选择后面的数字提取出来，加上`.txt`。

再把前面的文件名后面去掉`.txt`，拼上`下划线`和刚刚的这个数字，放在上面的那串字符串的前面。就构成了一个新的字符串，也就是用帖子的id来作为文件名。

---

### 第十一个函数

接下来就到了提取页面的超链接的部分了。

留园的小说最大的困扰就是页面到处有链接，正文有，底部也有。

而且很容易就错过，错过了就会导致保存的章节不全，你也不知道是作者没写完，是散佚了，还是你没有爬取完全。

所以为了避免看得正爽的时候戛然而止的扫兴，有必要开发一个功能强大的“超链接提取器”——

`hyperlink_extractor(url, header)`

参数十分简单，通常来说，越简单，就越可靠。

```python
def hyperlink_extractor(url, header):
    '''
    用于提取一个单独页面中正文和底部的所有链接

    并返回一个包含url的列表
    '''
    url = url.replace('amp;', '').replace('http:', 'https:')
    soup = get_soup_from_webpage(url, header)

    # 清理版面上不需要的部分，只留下正文与底部链接列表
    for script in soup("script"):
        script.decompose()
    for img in soup("img"):
        img.decompose()
    for noscript in soup("noscript"):
        noscript.decompose()
    for div in soup("div"):
        div.decompose()

    postlist = []

    # 获取正文里面的链接
    para = soup.find('pre')
    a_para = para.find_all('a')
    for hyperlink in a_para:
        if not hyperlink.get('href'):  # 当href不存在的时候，跳过
            continue  # <a target="_blank"></a>

        href = hyperlink.get('href').replace(
            '&amp;', '').replace('http:', 'https:')
        if 'http' not in href:
            realurl = "".join(['https://www.cool18.com/bbs4/', href])
            postlist.append(realurl)
        else:
            postlist.append(href)

    # 底部链接列表
    li = soup.find_all('li')
    for reply in li:
        bytes = reply.text.split(' bytes)')[0]
        bytes = bytes.split(' (')[-1]

        # 根据留言的bytes数来筛选真的补充帖子，bytes数小于600的一律不作数
        if bytes.isdecimal() and int(bytes) > 6000:
            reply = reply.find('a')  # 只选择第一个a标签获取其中的链接
            reply = reply.get('href')
            reply = reply.replace('http:', 'https:')
            reply = reply.replace('&amp;', '&')  # 似乎Beautifulsoup会自动把&amp;转换为?

            # 对于不完整的url，也就是前面没有http的时候：
            # index.php?app=forum&amp;act=threadview&amp;tid=14180619
            if 'http' not in reply:
                url_with_https = "".join(
                    ['https://www.cool18.com/bbs4/', reply])
                postlist.append(url_with_https)
            else:
                postlist.append(reply)

    # 对列表去重并保留原顺序
    only_postlist = []
    [only_postlist.append(i) for i in postlist if not i in only_postlist]

    return only_postlist
```

依旧是分段解读

```python
url = url.replace('amp;', '').replace('http:', 'https:')
soup = get_soup_from_webpage(url, header)

# 清理版面上不需要的部分，只留下正文与底部链接列表
for script in soup("script"):
    script.decompose()
for img in soup("img"):
    img.decompose()
for noscript in soup("noscript"):
    noscript.decompose()
for div in soup("div"):
    div.decompose()
```

页面有时候很纷杂，为了提高检索速度，我们并不需要花里胡哨的JavaScript的脚本代码来拖后腿，找到对应的javaScript关键词标签，也就是 `<script>` ，用bs4的 `decompose()` 函数来抛弃掉。

这里用上了循环，务求一网打尽。

```python
postlist = []

# 获取正文里面的链接
para = soup.find('pre')
a_para = para.find_all('a')
for hyperlink in a_para:
    if not hyperlink.get('href'):  # 当href不存在的时候，跳过
        continue  # <a target="_blank"></a>

    href = hyperlink.get('href').replace(
        '&amp;', '').replace('http:', 'https:')
    if 'http' not in href:
        realurl = "".join(['https://www.cool18.com/bbs4/', href])
        postlist.append(realurl)
    else:
        postlist.append(href)
```

依这里的注释所说，首先去获取正文里面的链接。

留园文章的正文都在 `<pre>` 标签里面，获取起来不费吹灰之力。

接下来获取超链接的 `<a>` 标签，拿到之后，依旧是清洗数据格式，确保是正确合法的带有https的url格式。

你可能会好奇，为啥好端端要加一个判断， `if not hyperlink.get('href'):` 

那是因为总有各种意外没完没了的出现啊：

比如某一个大神在文章中非要插一个图片。你插就插吧，还非要插一个外链的图片，那也罢了，可是这个外链还挂了，以至于被网站替换成了一个空链接，成了下面这样：

`<a target="_blank"></a>`

于是我们可爱的代码在执行到 `href = hyperlink.get('href')` 这一步的时候就毫不意外的挂了。

当 `href` 不存在的时候，上述的命令返回的就是一个 `None` ， `None` 在Python中等价于 `False` ，所以 `if not hyperlink.get('href'):` 的意思在 `hyperlink.get('href'):` 返回了 `None` 的那一刻，就成了 `if not False:` ， `if not False:` 是 `if` 和 `not False` 的合体。

 `不假` 就是 `真` ， `真` 就满足 `if` ，就跳过 <u>这个a标签</u> ，去找下一个，也就是 <u>包含href属性的那个a标签</u> 。

多么有趣的Python编程啊！

深吸一口气，继续往下看

```python
# 底部链接列表
li = soup.find_all('li')
for reply in li:
    bytes = reply.text.split(' bytes)')[0]
    bytes = bytes.split(' (')[-1]

    # 根据留言的bytes数来筛选真的补充帖子，bytes数小于600的一律不作数
    if bytes.isdecimal() and int(bytes) > 6000:
        reply = reply.find('a')  # 只选择第一个a标签获取其中的链接
        reply = reply.get('href')
        reply = reply.replace('http:', 'https:')
        reply = reply.replace('&amp;', '&')  # 似乎Beautifulsoup会自动把&amp;转换为?

        # 对于不完整的url，也就是前面没有http的时候：
        # index.php?app=forum&amp;act=threadview&amp;tid=14180619
        if 'http' not in reply:
            url_with_https = "".join(
                ['https://www.cool18.com/bbs4/', reply])
            postlist.append(url_with_https)
        else:
            postlist.append(reply)
```

上面这一段，我自己是感到比较得意的。

首先，留园的普通文章的跟贴区长这样：

```txt
++++++++该贴评分完成！ - 小脸猫 (179 bytes) 05/23/13

借帖求书《悖伦的娇妻们》完整版或最新章节！ - arcmod (2 bytes) 05/20/13

    记错了，以为书屋有的。新章节没有，TJ状态…… - 小脸猫 (2 bytes) 05/20/13
        可书屋里没有啊！我以前有收录的…… - arcmod (75 bytes) 05/21/13
            再收录吧 - 小脸猫 (2 bytes) 05/21/13
                我就是想再收录呀，可惜书屋找不到啊！ - arcmod (2 bytes) 05/21/13

程程爱吃橙子对此贴投票评分，给 affa19 加3银元奖励！！ (无内容) - 程程爱吃橙子 (0 bytes) 04/11/16

【降头师】第十七集［河图实体］ - xlm (133751 bytes) 05/20/13

    降头师18有人发么？17以后是不是就断更了？ (无内容) - isdemon (0 bytes) 08/16/19

【降头师】第十六集［河图实体］ - xlm (137201 bytes) 05/20/13

【降头师】第十五集［河图实体］ - xlm (138845 bytes) 05/20/13
```

这里面大部分是~~毫无意义的~~没什么用的跟帖。如果每一个都保存打开，就太浪费了。

需要先筛选一下。

继续努力观察，发现一般说来，带有文字“（无内容）”的，和“XXX对此贴投票评分，给 XXX 加X银元奖励”的，都可以过滤掉。

但是有的朋友就不按套路出牌，非要点评一个“ding ding ding”或者“好文”来显示一下存在感。

那这种时候，要是继续无限地添加关键词，岂不是成了又一个“墙”。

通过仔细观察，发现通常有料的那个链接，Bytes数比较大，可见Bytes数越大，内容越多，是文章的概率就越大。经过反复测试与比较，感觉6000是一个比较合适的阈（yù）值。

```python
for reply in li:
    bytes = reply.text.split(' bytes)')[0]
    bytes = bytes.split(' (')[-1]
    if bytes.isdecimal() and int(bytes) > 6000:
```

这里使用了 `.isdecimal()` 函数来确保拿到的bytes它是个数字。

为什么要强调这一点呢？因为有个别网页，里面它的链接并不在整个页面的底部，而是在正文的下方，所以也没有 `bytes` 这种东西。

Python中的变量只是一个名字，不是说你叫它 `bytes` （变量名）它就真的是 `bytes` （字面意思），完全有可能用 `左括号` 切片切出来的是一个字符串，如果直接用 `int()` 转换，那就报错了。

所以要先用`.isdecimal()`函数来判断一下，判断结果是个数字的话，虽然也不能百分百确定就是`bytes`，但是起码比不是数字的可能性要高多了。

接下来照旧是切片，替换清洗格式，返回列表了事。

PS：

关于Bytes的切片那里，曾经我觉得这么分布是最合理的：

```python
bytes = reply.text.split('bytes')[0]
bytes = bytes.split(' ')[-2][1:]
```
毕竟这样符合人类的认知与哲学，只要看看哪个留言的bytes数大于6000就应该是有点东西在正文里就好了嘛。

直到我遇到了以下这个奇葩：

> 我知道,但不足1万bytes还是有可能不评分...这条是通的~~ - affa19 (2 bytes) 03/30/13

哎，头疼……

```python
# 对列表去重并保留原顺序
only_postlist = []
[only_postlist.append(i) for i in postlist if not i in only_postlist]

return only_postlist
```

最后到了要添加到列表的环节，添加之前先去重。不然有的文章正文和底部的链接都指向同一个章节，我们岂不是要白白下两次？

当然有人说可以用 `list(set(list()))` 的骚操作，利用set集合无重复元素的特性来去重。但是那样一来，顺序就乱掉了。

对于这样一个动辄80篇帖子起步的网站，如果我们的列表顺序乱了，那么在报错的时候，就很难判断到底是哪一个帖子产生了错误。

如果是按顺序来，那么查找的时候就方便多了。

有鉴于此，用了这样一个稍显复杂，但是的确管用的方法来去重，保证了原有的顺序，生活顿时又有了希望。

---

### 最后一个函数

千呼万唤，我们终于来到了这总装的最后一步：

把上述介绍的所有的函数一层一层的组装在一起，注意缩进，就有了以下的这个主函数。

```python
def crawl(header):
    failed_log_list = []
    # 生成主页地址
    article_page_url = main_page_url_generator()
    # https://www.cool18.com/bbs4/index.php?app=forum&act=gold&p=2
    for each_page in article_page_url:
        # 根据每一个主页，依次获得每个主页上那200个文章的地址
        article_list = get_articles(each_page, header)
        # https://www.cool18.com/bbs4/index.php?app=forum&act=threadview&tid=14135342
        # 【欲恋】（０１－６１）作者: 爱夜夜夜夜
        for article in article_list:
            try:
                # 每个文章动用文章链接提取器来提取章节地址
                try:
                    top_soup = get_soup_from_webpage(article, header)
                except:
                    top_soup = get_soup_from_webpage(article, header)
                top_title = find_title(top_soup)
                if top_title == None:
                    print("文章已经被删掉了，跳转去了主页")
                    break
                print(top_title)
                if 'classbk' in article:
                    para = extract_classbk(top_soup)
                else:
                    para = extract_text(top_soup)
                postlist = hyperlink_extractor(article, header)
                if para:
                    if len(para) >= 1000 or postlist:
                        create_folder_as_per(top_title)
                        rename_and_savetext(
                            top_title, top_title + '.txt', para, article)
                else:
                    print("空空如也，不值得保存，跳过。")
                    break

                for posturl in postlist:
                    if 'threadview' not in posturl:
                        continue
                    try:
                        soup = get_soup_from_webpage(posturl, header)
                    except:
                        soup = get_soup_from_webpage(posturl, header)
                    page_title = find_title(soup)
                    if page_title == None:
                        print("文章已经被删掉了，跳转去了主页")
                        break
                    print(page_title)
                    txt_name = file_name(page_title)
                    if 'classbk' in posturl:
                        paragraph = extract_classbk(soup)
                    else:
                        paragraph = extract_text(soup)

                    if paragraph:
                        # 将正文保存为文本
                        rename_and_savetext(
                            top_title, txt_name, paragraph, posturl)
                    else:
                        print("空空如也，跳过。")
                        break

                    # 针对把文本隐藏在更深的章节里的情况
                    secondary_list = hyperlink_extractor(posturl, header)
                    if secondary_list:
                        secondary_folder_path = os.path.join(
                            top_title, page_title)
                        create_folder_as_per(secondary_folder_path)
                        print(secondary_folder_path)
                        for second_level in secondary_list:
                            if 'threadview' not in second_level:
                                continue
                            if second_level in article_list:  # 不重复下载
                                continue
                            try:
                                try:
                                    second_soup = get_soup_from_webpage(
                                        second_level, header)
                                except:
                                    second_soup = get_soup_from_webpage(
                                        second_level, header)
                                second_title = find_title(second_soup)
                                if second_title == None:
                                    print("文章已经被删掉了，跳转去了主页")
                                    break
                                print(second_title)
                                second_txt_name = file_name(second_title)
                                body_text = extract_text(second_soup)
                                if body_text:
                                    rename_and_savetext(
                                        secondary_folder_path, second_txt_name, body_text, second_level)
                            except:
                                print("算了，跳过不理")
            except:
                print(f"{article}挂了，先记下来，回头再算账")
                failed_log_list.append(article)
                for line in failed_log_list:
                    with open('try_later.txt', 'a', encoding='utf-8') as fd:
                        fd.write(line + '\n')
```

对于这一个函数的理解，首先需要正确掌握Python的函数中的形参和实参的概念。

这里要提到中英文的差异，在英文中，Parameter和Argument是两个不同的东西，中文里面统一翻译成「参数」，其实两个有些许差异，很多教材说的云里雾里，把它们分别翻译为了「形参」和「实参」，说白了形参就是形式上的参数，也叫位置参数，放在那个位置就是占一个地儿，名字不重要，位置很重要。但是Python里也有例外，就是在名字对上了的情况下，位置也就不再需要一一对应了。

举个例子，如果把 `喊(爸爸)` 当做一个函数， `你妈妈喊的(爸爸)` 是你外公，而 `你喊的(爸爸)` 是你爹，那这两个通常情况下不应该是同一个人。这里括号内的 `(爸爸)` 就是形参； `被喊的“爸爸”` 具体是谁，要结合输入的参数来判断，所以是实参。

所以如下的函数里面的`pos1`和`pos2`只是占一个位置，你自己要清楚记得哪个是哪个，用的时候完全可以放不同的东西进去。

当然，变量的类型很重要，是`str`还是`int`要搞清楚，不然就会出错。

```python
def functional(pos1, pos2):
    return pos1 + pos2
```

此外还用到了一个很好用的结构： `try……except……` ，在不知道 `try` 里面的代码是否正常运行的的时候，先try它一下，没有问题就正常执行，有问题就退出来执行except里面的部分，而不是简单的报错程序崩掉。

利用这个特性，对每一次获取soup的请求都在第一次请求失败之后做第二次尝试，可以有效减少因为网络不通畅而造成的爬取失败。

此外，我们可以用这个结构来实现一个提取错误链接的保存功能：

```python
failed_log_list ＝ []
try:
    略
except:
    print(f"{article}挂了，先记下来，回头再算账")
    failed_log_list.append(article)
    for line in failed_log_list:
        with open('try_later.txt', 'a', encoding='utf-8') as fd:
            fd.write(line + '\n')
```

虽然我们已经考虑的很合理了，但是在实际运行过程中，一定会遇到各种事先所想象不到的困难，比如上文中列举的各种匪夷所思的情况，什么文件名包含非法字符啦，网页明明在列表中但是已经被删了导致返回错误啦，还有个别作者和用户不按套路出牌之类的……如果每次出错都要停下来排故再重新启动一遍我们的代码，一来耽误时间二来也没完没了被打断，实在是很痛苦。

所以考虑到这样的情况，就模仿小学时候的经验，设立了一个“错题本”，遇到错误就把发生错误的文本的地址记下来，存到文本文件里去，等代码运行结束之后再翻出来逐一单独解决。

对于整个函数来说，虽然看起来很长很吓人，但是都是一点点往里面填充细节，而且很多错误是一开始未曾想考虑到，在运行中一点点发现，再回过头来增补的。

整个函数的架构可以分解成以下这个样子：

```python
def crawl(header):
    failed_log_list = []  # 新建一个错题本的列表
    article_page_url = main_page_url_generator()  # 用页面生成器拿到每一个主页的地址
    for each_page in article_page_url:
        # 根据每一个主页，依次获得每个主页上那200个文章的地址
        article_list = get_articles(each_page, header)
        for article in article_list:
            try:
                # 见代码块A讲解
                保存article的正文
                提取article的链接，存入post列表

                for posturl in postlist:
                    # 见代码块B讲解
                    保存二级链接网页的正文
                    提取二级网页里面附带的链接（如果有），存入secondary_list列表

                    if secondary_list:
                        # 见代码块C讲解
                        保存二级链接网页的二级链接的网页的正文……
                        基本上也没有再链的部分了，到这里差不多就可以了。
            except:
                把错题本里面的链接保存到错题的文本文件中
```

#### 代码块A

作为第一级文章，它是所有下面的二级网页的起点。里面有时候会在正文中和正文下方的跟帖区插入大量的其它章节的链接。

但是呢，因为帖子的历史很长，加上各个作者的习惯不一样，有的人正文什么也不写，但是会在跟帖那里留下一些链接。

有的人把链接放在正文里，有的短篇太短，正文就都有了，没有链接。

这些都还好，建个文件夹，有正文保存正文，没有就下载链接的文章放在这个文件夹里就行。但是，有的文章是空的。

你问我为什么是空的，天知道，也许是被删贴了，也许是作者故意而为之，总之就是空的。还有被重定向的，在这种情况下，如果我们也不分青红皂白就建一个文件夹，那就显得比较不明智了。回头看着空空的文件夹往往会怀疑人生，以为自己的代码没有工作。

所以先加一个判断，看看文章里面有没有料，如果发现有比较长的正文，或者有bytes数比较大的链接，说明这个文章有继续发掘保存的价值，再建立文件夹比较好。

```python
# 每个文章动用文章链接提取器来提取章节地址
top_soup = get_soup_from_webpage(article, header)
top_title = find_title(top_soup)
if top_title == None:  
    print("文章已经被删掉了，跳转去了主页")
    break  
print(top_title)

if 'classbk' in article:
    para = extract_classbk(top_soup)
else:
    para = extract_text(top_soup)

postlist = hyperlink_extractor(article, header)

if para:
    if len(para) >= 1000 or postlist:
        create_folder_as_per(top_title)
        rename_and_savetext(
            top_title, top_title + '.txt', para, article)
else:
    print("空空如也，不值得保存，跳过。")
    break

```

上述代码中挑两个值得一讲的段落进行分析：

```python
if top_title == None:  
    print("文章已经被删掉了，跳转去了主页")
    break  
```

这里就是上面文中提到的，当soup返回来的结果什么都没解析到的时候，通常意味着文章已经走入了历史，所以及时中断循环，止损，既可以挽救青春也可以避免报错。

```python
if 'classbk' in article:
    para = extract_classbk(top_soup)
else:
    para = extract_text(top_soup)

postlist = hyperlink_extractor(article, header)

if para:
    if len(para) >= 1000 or postlist:
        create_folder_as_per(top_title)
        rename_and_savetext(
            top_title, top_title + '.txt', para, article)
```

这一小段实际上是两个部分，先用 `extract_classbk(top_soup)` 和 `extract_text(top_soup)` 提取正文 `para` ，再用 `postlist = hyperlink_extractor(article, header)` 来提取 <u>该正文所在页面上的链接列表</u> 。

下面用 `if len(para) >= 1000 or postlist:` 来判断正文是不是足够长（因为有些页面上，只有短短的两句毫无信息量的废话）或者有**有价值的**链接。两个条件只要满足任何一个，就调用 `create_folder_as_per(top_title)` 函数来新建一个文件夹。
并在这个文件夹里面调用用于保存的 `rename_and_savetext()函数` 执行保存操作。

#### 代码块B

来到二级链接的网页，大部分文章在这里都是某一个大标题下面的小章节，比如第10到第15章这样。

```python
for posturl in postlist:
    if 'threadview' not in posturl:
        continue
    soup = get_soup_from_webpage(posturl, header)
    page_title = find_title(soup)
    if page_title == None:
        print("文章已经被删掉了，跳转去了主页")
        break
    print(page_title)
    txt_name = file_name(page_title)
    if 'classbk' in posturl:
        paragraph = extract_classbk(soup)
    else:
        paragraph = extract_text(soup)

    if paragraph:
        # 将正文保存为文本
        rename_and_savetext(
            top_title, txt_name, paragraph, posturl)
    else:
        print("空空如也，跳过。")
        break
```

有个别时候，我们写的链接提取器会判断失误，把一些奇怪的图床上的图片的链接也拉了进来。所以要在这里进行过滤。

有朋友会说那为什么不从列表中甄别剔除，非要等到用的时候再抓过来一个个看呢？

那是因为从一个列表中循环每一个元素，判断该元素是否包含特定的关键词的操作相对比较繁琐。步骤越多，出错的可能性越高。所以还是简单点的好。

用 `threadview` 做关键词基本上就能把非留园的帖子都过滤去除掉了，还是比较好用的。

剩下的代码部分就和代码块A里面的基本上一样，重复了一遍相同的流程罢了。唯一的区别是不再需要判断正文是否存在，也不需要再建立新的文件夹，省事省心。

#### 代码块C

阿弥陀佛，不知道你们有没有遇到过这种令人抓狂的作者：好好的页面他不用，非要在跟帖区贴链接，链接打开又是链接……

要是写的特别长篇大论倒也罢了，一共就2000来字，还要分八章，分布在那么多页面里……

莫非丫的文章都是坐在马桶上写的么🤷‍♀️

```python
# 针对把文本隐藏在更深的章节里的情况
secondary_list = hyperlink_extractor(posturl, header)
if secondary_list:
    secondary_folder_path = os.path.join(
        top_title, page_title)
    create_folder_as_per(secondary_folder_path)
    print(secondary_folder_path)
    for second_level in secondary_list:
        if 'threadview' not in second_level:
            continue
        try:
            second_soup = get_soup_from_webpage(
                second_level, header)
            second_title = find_title(second_soup)
            if second_title == None:
                print("文章已经被删掉了，跳转去了主页")
                break
            print(second_title)
            second_txt_name = file_name(second_title)
            body_text = extract_text(second_soup)
            if body_text:
                rename_and_savetext(
                    secondary_folder_path, second_txt_name, body_text, second_level)
        except:
            print("算了，跳过不理")
```

因为是链接的链接的文章，所以还是要再在主文件夹里创建一个子文件夹，把那八章的txt文件一股脑放进新的子文件夹中。

为什么要这样子做呢？

原因很简单，因为会把文章写到这一层的作者，在给文章的页面起标题的时候通常都简单粗暴，毫无逻辑，缺乏美感。

平平无奇的“第一节”三个字，他可以从上一级文章的“第1章”一直用到“第88章”。

如果我们不为每一个“第X章”建立一个单独的子文件夹，那么这88个“第一节.txt”就会一个覆盖一个。你爬了半天，打开一看只有最后一章的第一节保存了下来，之前爬取的文件都被覆盖了。

就算我们用了重命名的高端算法，让这88个txt并存，也会有88个包含“第一节”的文件名的txt在文件夹里，你也根本搞不清这么多的“第一节”分别是哪一章的“第一节”。

创建子文件夹其实就是在原来的路径上用 `os.path.join` 函数继续加一层新的子文件夹的名字就好了，具体的实现交给函数去做就行。

最后要说明的是，为什么我们的传入参数的变量名变来变去，一会儿是 `title` ，一会儿是 `top_tile` 一会儿是 `second_title` 呢？

这就是本节开篇说的，要搞明白形参与实参的意义了，因为Python的变量虽然是私有，并非全局变量，但是在同一个函数中，变量名在这个函数的作用域里是全局的。

在上一个循环和下一个循环中，虽然函数调用的是同一个，但是函数的参数实际上是完全不同的，第一级的文章的链接和第三级的当然不应该混用，不然就会出现各种匪夷所思的结果。

---

### 还没完，别忘了最后一步

千辛万苦，整个代码到了可以运行的时候啦~

```python
if __name__ == '__main__':
    os.chdir(SAVE_DIRECTORY)
    crawl(HEADER)
```

对于初学者而言，很多人不明白这个 `if __name__ == '__main__':` 到底是干嘛用的。

坦率讲，一年半以前的我也不明白，看到大家都这么用我也这么用，照葫芦画瓢代码能跑就行。当然经过这么长时间的学习，现在的我已经懂了：

它的作用是避免代码在模块被导入后执行。假设你的代码在被别的py文件引用的时候（例如在其它的py文件import该py文件），如果不加这一段，那么你的代码会不分青红皂白直接运行，而加了这一段之后，在引用的时候就不会自动执行你放在这一行之后的代码块。

把这一段放在代码的最下面，因为它上面是函数的定义，它下面是函数的调用。代码从这里之后开始执行，遇到调用函数的时候就回到上面去查找。

用 `os.chdir` 函数把Python的执行目录切换到你要保存文本文件的路径去，这样待会儿爬取下来的文章就会哗啦啦在那个路径下生成。

最后把HEADER放进我们刚刚总装的函数，让主函数可以从这里开始运行。

打开你的CMD或者Powershell，执行这个 `study2.py` ，就可以看到字符在屏幕上跳动，你的txt文件哗啦啦地在硬盘里生成啦。

～～花びらをまく～～

---

## 后记

整个代码写了好几个晚上，实际运行超过十个小时，扒拉下来7 GB多的txt文件。

一共得到了110,346个文件，8,316个文件夹。

据统计，在txt中差不多每1GB可以保存五亿汉字，那么据此估算，留园上的精品情色小说的总字数高达35亿汉字（非精品应该更多）。

朋友们，古典名著《红楼梦》也只有70几万字而已。

可见生理欲望是人类文明发展的源源不断的动力啊。

下载了如此浩瀚的小说，可能我这一辈子也看不完其中的百分之一吧。

网民们的创作力是无穷的，而我的精力是有限的，呜呼哀哉！

真的想再活五百年啊～～

PS：

当然，这35亿汉字的小说里面有很多是重复的，毕竟我们采用的爬取方法并没有对帖子进行去重处理，之所以不去重的原因在于有时候同一个小说会被来回引用转载，十万字的小说可以以不同的名字转载保存在网站的不同位置，轻而易举产生二百万字以上的空间，但是看来看去都是同一篇小说。但是同一篇小说还有什么重排版、重置版、精修版、续写版……你也搞不清到底哪个才是真的原著，哪个是从别的地方搞过来的拼接版，所以干脆统统拉下来，大家自己鉴别。

而且有些小说创作年代实在太过久远，不同的人通过不同的途径保存下来的章节出入很大，加上无数论坛、网站兴衰更迭，导致无数伸手党与搬运工转载就没转全，再加上敏感词和谐系统的出现，大量的删节与散佚。无数缺乏耐心与敬业精神的作者弃坑，断更，冒名顶替者续写，改写，替换主人公的姓名，拼接不同文章里的情节，换个名字把转载当原创，李鬼冒充李逵的现象比比皆是。

诞生只有不到二十年的华语情色小说尚且有如此大的分野，先秦时代的文学作品能流传到今天，实属不易。

PS2：

鉴于重复率实在是太高了，还是补了一个新的Python文件用来去重，请有需要的朋友自己运行`duplicate_remove.py` ，在去重之前有约11万个文件，去重之后只剩下74,791个有效文件，略小于4 GB。

当然，这个数字依然很庞大，我不可能看得完，也不打算看完，偶尔挑几本过过瘾就好了。

人生短暂，多陪陪家人。世界很大很精彩，多出门走走，成为更好的自己。

---

## 感谢

感谢所有为中文情色小说奉献过创意与想法的每一个人，感谢留园的版主: 小脸猫 青青的世界 。

大家都是一个个的普通人，既非圣贤，七情六欲只要在法律允许的边界之内，在幻想与现实中，找到一个平衡点，也是人生乐趣的一部分啊。

祝大家生活愉快，有缘再聚。
