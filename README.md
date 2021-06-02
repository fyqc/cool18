# 记一个Python爬虫的诞生全过程

## 写在前面

从去年疫情开始，在家闲着没事做，捣鼓Python以来，不知不觉已经一年了。

一开始学Python的诉求很简单，是为了下载Dgtle上的高清图片，用了很多的下载软件，哪怕像Firefox中的插件DownThemAll！这样优秀的作品，也是需要我手动保存一个下载列表，还要用替换的功能把链接中的缩略图的参数去除，再导回下载器才可以得到一个高清的图片。

而且还需要我再手动操作，把每一个作者的id单独记下来，效率很低，每周都要花好多时间来做这件事情。

计算机程序的意义就在于可以把人类从这样枯燥而重复的单调工作中解脱出来，加上IT界开放的资料汗牛充栋，真想学的话，网络上处处是资源。

花了点时间，很快就入门，又接连写了好几个程序提高了自己的知识水平。

我当然不能说我已经对Python掌握到了一个什么高度，但是就目前而言，它已经能够实现我心中的想法，对于不靠它吃饭的我来说，这就已经足够了。

虽然有很多人对Python嗤之以鼻，嫌它速度慢，效率低什么的，可能是我小时候苦日子过惯了，一直用的都是老掉牙的机器，对慢吞吞地反应速度已经习惯了。

当我的Python代码在我的计算机上运行起来的时候，它所呈现的速度是让我感到很惊喜的，我觉得现阶段，我思考的速度还远远不能跟不上它运行的速度，至于那一点点性能损失，反正NASA又不需要靠我的代码去实现登月，不在意啦。

这一次写就的爬虫，是我一段时间以来所学会的各种技术的综合演练，个人对结果比较满意。

也写下来，一方面满足自己人菜瘾大的创作欲望，另一方面也为有缘看到本文的朋友们当一个参考。

### 爬虫是什么

我本人非常讨厌一切虫子，但是爬虫又不是真的虫，只是一种计算机代码，用于从网上爬去数据而已。考虑到水平能力有限，里面一定充满了各种各样的Bug，那从这个意义上来考虑，倒也有些贴切。

这一次想要写爬虫的动机是出于看到[留园网](https://www.cool18.com)的[禁忌书屋](https://www.cool18.com/bbs4/index.php?app=forum&act=gold)版块里有许多~~让人看了欲罢不能的~~少儿不宜的读本。

每次抱着手机躺在床上刷，排版和广告都很令人头疼，网页上各种加载的css和图片也是手机电量的一个负担。因此，把它们保存成为txt格式，再慢慢看，成了一个最佳选择。

但是面对这么多的文本，每一个都打开一个一个手动保存，既费时费力，还很容易出错。

这种枯燥、繁复的工作，交给程序去做就好啦。

所以，这一次，我要写的代码，就是用Python来批量下载／保存*禁忌书屋*中的所有读本，并以读本的名字作为文件夹，里面的每一个单独的帖子都以该帖子的名字作为文本文件的文件名保存在该文件夹内，文本文件的编码格式选用UTF-8，以确保对移动设备的支持。

### 万事开头难

假设本文的阅读者已经对Python有了一定程度的了解，对PC的操作以及对互联网的使用都有一定的基础。

我所使用的Python是3.8.10 64-bit的版本，
编辑器是Visual Studio Code （版本 1.56.2），安装了Python（版本 2021.5.842923320）和Pylance （版本 2021.5.4） 插件，使用Windows 7 Pro 64-bit。

代码的编写规范遵循PEP8的指导，参照了Google的相关代码[编写指南](https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_style_rules/)。

虽然我是一个业余的计算机爱好者，但是我想业余并不代表胡来，还是在力所能及的范围内应该把事情做到位，做得尽可能正确。

考虑到文本文件本来也没有多大的体积，不像图片下载起来很慢，就没有上多线程来提高下载的效率了。一个一个的搞，其实也是一个乐趣，不然满屏幕的信息，根本来不及看，很容易头晕。

一秒钟跳个两三行的指令，我觉得已经是极限了，我的人脑的处理速度就这么快，还是想看着Powershell的命令进展，好知道自己的程序运行的情况。

### 关于收费

感觉互联网上有一股很浮躁的氛围，许多人稍微会一点点东西就急不可耐开始收费，要求扫码，要求打赏。

人家情色小说的作者尚且用爱发电，给我们贡献了这么多文学的经典，我不过是站在巨人们的肩膀上，做了点力所能及的微小贡献，实在是无颜把我的作品拿出来找人要钱。

当然有的伸手党从我这里免费拿去，再转载拿去收费，这样的行为我也无暇去一一追讨，只能说做人的境界不一样，人生的追求不一样，自私的人总是有的，作为总理的忠实信徒，我还是相信一个开放的互联网会让所有人受益，相信**天下为公**的。

看到本文的诸君，可以大大方方把本文拿去转载，不用来通知我一声，我所写的代码，也尽可以拿去用。~~被警察叔叔抓了别把我供出来就行~~。

---

## 正式开始

### 文件头

首先，在VS Code中创建一个py文件，这里我给它起名为`study.py`。

我不是很喜欢建立一堆文件，还是喜欢把所有的东西都放在一个页面里。反正整个程序也没有超过500行，来回多划拉几次，有需要的时候分左右两个屏对比前后来看看也就够了。

面对一个全新的空白的py文件，第一件事，来创建一个注释，加上今天的日期：

```python
# 2021年6月1日
```

然后开始导入运行需要的库：

因为是爬虫，这里用了两个大名鼎鼎的Python的库，一个叫做[Requests](https://docs.python-requests.org/en/master/)，一个叫做[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.html)。

又因为我们要操作并保存文本文件，建立文件夹，所以还需要导入Python自带的os库。

注意，有很多文章与教程只说用BeautifulSoup就好，但是BeautifulSoup推荐使用的`lxml`解析器也是需要[另外安装](https://lxml.de/)的。

按照惯例，把库放在整个文件最开始的地方。

```python
import os
import requests
from bs4 import BeautifulSoup

# 2021年6月1日
```

有的教程说python文件的开头要放一个#shebang，也就是下面这个东西：

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
```

这个东西的作用是让Python解析器知道你的文件的编码是UTF-8，不过我看了Python的官方文档，这东西在Python 2 的年代很有用，如今在Python 3 的时代，已经是默认为UTF-8，所以这两行不再需要了。

因为IT技术变化日新月异，许多时候你找到的教程一看创作时间在好几年之前，你复制下来他的代码，运行了一下发现根本跑不通，那并不完全是因为作者水平不济，有可能就是时代变了，当时工作的代码所依赖的环境变化了，所需要爬取的网站也改版了，所以那一段代码如今已经不能工作了。

想要确认是不是UTF-8很简单，在VS Code的右下角可以看到当前的编码，如果是UTF-8就说明该文档是UTF-8编码。

### 开始第一个函数

第一个函数`get_soup_from_webpage(url, header)`的作用是把一个网页从html格式变成BeautifulSoup的soup格式，方便后续从里面解析出我们需要的东西，包括正文的字符串，以及超链接。

```python
def get_soup_from_webpage(url, header):
    response = requests.get(url, headers=header)
    if 'classbk' in url:
        response.encoding = 'gb2312'
    else:
        response.encoding = 'utf-8'
    content = response.text
    soup = BeautifulSoup(content, 'lxml')
    return soup
```

这里的`url`是需要解析的网页的地址，类似于`https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.html`。因此需要有http或者https来开头，以html结尾。

同时，作为函数的参数，它必须是一个字符串，所以传入的时候要加上单引号或者双引号，使它成为字符串。

`header`是http传输协议的字头，为了欺骗网站，将我们的爬虫程序伪装成一个浏览器。对于大度的留园网而言，它对于字头还是睁一只眼闭一只眼的，因此我们的爬虫爬取它的信息还是比较容易，无愧于一个优秀海外中文网站的楷模。

`header`的获取可以在浏览器的开发者工具中找到，网上有很多的教程，随便搜搜都有，这里我用我的FireFox中所提供的：

```python
if __name__ == '__main__':
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46'}
```

对于初学者而言，很多人不明白这个

```python
if __name__ == '__main__':
```

到底是干嘛用的。

坦率讲，我也不明白，有的文章中说它的作用是保证你的代码在被别的py文件引用的时候（比如需要这个py文件中的函数），不会自动执行你的主程序。

这么说当然有一定的道理，我只是根据实践，大致理解为它类似 C语言中的main()函数，给你的代码提供一个开始的接口。告诉程序，以上都是我定义好的函数，从这一行开始，我要开始调用了。

把这一段放在代码的最下面，因为它上面是函数的定义，它下面是函数的调用。代码从这里开始执行，遇到调用函数的时候就回到上面去查找。

```python
if 'classbk' in url:
    response.encoding = 'gb2312'
else:
    response.encoding = 'utf-8'
```

这一段是因为网站的历史变迁缘故，在某一年之前的网页，它们的编码并不是默认的UTF-8，而是GB2312。

如果统一以UTF-8来解码，就会得到一个全是乱码的结果，后面的所有分析都无从谈起。

好在那样的网页，就目前来看，都有一个统一的特征，即url中包含关键字`classbk`，所以写了一个判断语句，根据需要来调用不同的解码规范。

---

### 第二个函数

接下来，开始写第二个函数`main_page_url_generator(test='off')`。

```python
def main_page_url_generator(test='off'):
    '''
    翻页系统，生成留园主页第一页到第十八页的地址
    '''
    article_page_url = []
    main_page = 'https://www.cool18.com/bbs4/index.php?app=forum&act=gold'  # 禁忌书屋首页
    article_page_url.append(main_page)
    for page in range(2, 19):
        newpage = "".join([main_page, '&p=', str(page)])  # 第2页到第18页的地址
        if test == 'on':
            print(newpage)  # 测试用
        article_page_url.append(newpage)
    return article_page_url
```

顾名思义，这个函数的作用是生成首页的url，并以列表的形式返回这18个url。

具体说来是什么意思呢？

禁忌书屋的第1页的地址是`https://www.cool18.com/bbs4/index.php?app=forum&act=gold`

第2页的地址是`https://www.cool18.com/bbs4/index.php?app=forum&act=gold&p=2`

第3页的地址是`https://www.cool18.com/bbs4/index.php?app=forum&act=gold&p=3`

通过幼儿园数学找规律的知识，不难发现，第2页就是在第1页的基础上多了后面的`&p=2`而已。

推而广之，第n页就是在第1页的url后面加上`&p=n`。
当然，虽然作者众多，文库里面的书也着实很多，但是山高也有边，水长也有源，每页200篇书目，一共18页就到头了。所以最后一页是`&p=18`

我们不是“万字”寓言中那个小孩，应该不会有人会把每一个url都列出来这么傻，我们只要写一个循环，让它自动生成<u>包含2到18的url列表</u>就好了。

无数Python的基础教程都会讲到一个生成1到18的数字的函数，叫做`range`，它的用法是前面是闭区间，后面是开区间。也就是说我们的`range(2, 19)`实际上是生成一个开始包含2，结尾不包含19的全自然数的数列。

代码中用到了`join`函数来拼接字符串。

```python
"".join([main_page, '&p=', str(page)])
```

对于字符串的拼接，一定要先使用`str()`把page得到的自然数从`int`类型转换成`str`类型。不然就会报错，告诉你不能把`str`和`int`拼接。

使用`join`而不是使用简单的一个`+`来拼接，而不是连接字符串的好处在于，这个代码即使被运行在其它的操作系统下，也可以最大程度地保证执行的可靠性。尤其是在拼接路径的时候，更是如此。

有些朋友注意到我在函数的参数那里放了一个默认值为off的test做为函数的参数，在函数内部还放了这样一段代码。

```python
if test == 'on':
    print(newpage)  # 测试用
```

这个东西的由来是在一开始摸索的时候，需要时时使用`print`来验证得到的结果。就像是工地上的脚手架，虽然楼盖好了，理论上就不再需要脚手架了，但是留着它作为一个接口，当程序运行的结果与我预期不一致的时候，比如报错。

我就想要知道到底哪里不对，如果再回到源代码中一行行去插入`print`，显得很慢。在排故结束之后，又很容易忘记把插入的`print`再注释掉或者删掉。

加入这样一个参数之后，利用`test='on'`作为一个调试的开关，就不用反反复复去注释代码中的`print`来显示每一步都得到了什么结果，当不需要`print`的时候，在调用函数的时候直接去掉函数的`test`参数，函数的默认值参数`test='off'`，这时候`print`的条件不满足，就不执行这些`print`的命令了。

---

### 第三个函数

接下来写第三个函数，`get_articles(url, header, test='off')`

```python
def get_articles(url, header, test='off'):
    '''
    拿到所有的文章的列表

    返回包含200篇文章的列表
    '''
    article_list = []
    if test == 'on':
        print("拿到所有的文章的列表")  # 测试用
    soup = get_soup_from_webpage(url, header)
    soup.table.decompose()  # 留园首页
    soup.table.decompose()  # 类别 都市
    table = soup.find('table')
    if test == 'on':
        print(table)  # 测试用
    for a in table.find_all('a'):
        href = a.get('href')
        if test == 'on':
            print(href)  # 测试用
        href = href.replace('&amp;', '&')
        if 'http' not in href:
            url_with_https = "".join(
                ['https://www.cool18.com/bbs4/', href])
            article_list.append(url_with_https)
        else:
            article_list.append(href)
    return article_list
```

如函数文档的说明所言，它的功能就是从首页上获取那200篇文章，每一个文章的页面的地址，并返回包含这200个url的列表。

`soup.table.decompose()`的函数的作用是把soup对象中所有的table的块按从上到下的顺序，抛弃掉，减小后面分析的时候的系统压力与负担。

这里介绍一下html的小知识，html中所有的元素都是以块的形式呈现的，比如一个html页面会放好几个`<table></table>`，里面放一堆导航条，比如在第一个里面塞上“首页”“漫画”“赛事”之类的东西，第二个`<table></table>`里面放些“点赞”“投币”之类的东西，第三个第四个第五个依次排列在网页上。

具体到留园的禁忌书屋，一共也就大概5个table，我需要的这200篇文章在第三个table块中，所以把前两个抛掉就行了。理论上你当然可以写一个循环来让这个代码更优雅，但是我看了一下页面，因此就让它抛了两次，留下了第三个。

你问我为什么后面的`<table></table>`我们不去管它？

因为接下来我们使用了`soup.find('table')`，这里的`find`和`find_all`的区别在于前者找到第一个就停下来，后面会继续找下去，直到找到所有的`'table'`标签为止。

请听题，已知有不少于五个table的块，我们需要的table块是第三个，然后我们删了俩，又使用了只找一次就不再找的`find`函数，那我们找到的到底是第几个table块呢？

答案显然就是第三个，也就是我们所需要的那一个。

```python
for a in table.find_all('a'):
    href = a.get('href')
    if test == 'on':
        print(href)  # 测试用
    href = href.replace('&amp;', '&')
    if 'http' not in href:
        url_with_https = "".join(
            ['https://www.cool18.com/bbs4/', href])
        article_list.append(url_with_https)
    else:
        article_list.append(href)
```

到了这一步，我们已经定位并拿到了所需要的这一个table的标签里面的所有内容，接着使用代码把里面的所有超链接的部分提取出来。

众所周知，留园家的超链接长这样：

`<a href='https://www.cool18.com/bbs4/index.php?app=forum&act=threadview&tid=14135342'>第一章</a>`

上述命令就是把所有的a标签，也就是超链接提取出来，再从提取出来的包含所有超链接（a标签）的列表中，做一个循环，依次提取href属性的内容。

由于html中，`&`并不合法，所以bs4会使用`'&amp;'`作为转义字符，如果我们直接把它输入到url中，就会导致出现解析的错误，所以使用`replace`函数把它替换（还原）会原本的样子。

下面那段是因为部分页面提取出来的时候长下面这样：

`index.php?app=forum&amp;act=threadview&amp;tid=14135342`

通过对比，发现少了前缀：`https://www.cool18.com/bbs4/`。

聪明的同学说，得之矣，用`join`函数把它拼接起来就好啦。

可是，问题又来了，某些页面是完整的，你这样不分青红皂白就拼接，就会出现很搞笑的情况：

`https://www.cool18.com/bbs4/https://www.cool18.com/bbs4/index.php?app=forum&amp;act=threadview&amp;tid=14135342`

到时候等待你的就是一个残酷的报错。

解决方案：我是一个业余爱好者，业余的人路子野，简单粗暴，判断http在不在里面，如果解析出来的url里面有`http`在，就不加前缀，`http`不在其中说明没有前半段，就调用`join`把前缀给加上去。

这里还有一个坑，部分同学说，那我用`https`作为判断不是更好吗？

理想是美好的，现实是残酷的，有时候解析出来的是`http不加s`后面跟着一长串，`http`跟`https`比，不过是安全性差了点，但它当然也是一个合法的url。这里如果以`https`作为关键词，代码在碰到`http`的时候就会认为没有前缀，于是再加上一个前缀，你就有了两个前缀，报错收场。

把url添加到列表的时候，记得加了前缀的，和原生的不需要加前缀的url，它们的变量名是不一样的，别添加错了。

---

### 第四个函数

接下来写一个函数`find_title(soup)`来提取页面的标题，以soup作为输入的参数。

所以它是用上面的解析出来的soup输入，从里面筛找，返回符合要求的标题（title）。这个标题等会儿就用来命名我们的文件夹和文本文件。

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

许多人说你这里搞这么多`replace`干嘛，那是因为总有些不走寻常路的作者天马行空，在网页的标题里弄一堆非法字符，如果不加以筛选，就直接用来创建文件夹，就会出错。

文件名中有一堆字符是不可以用的，把它们统统替换成下划线。此外每一个文章标题里都跟着` - cool18.com 书库`和` - cool18.com`，像小广告一样，很烦，把它们用不存在的“空”给替换掉，也就是删除掉。

如果不这样竖着排列，要用一字长蛇阵，也就是所谓的chain，看起来非常长，显得不美观，也不方便注释。

`strip`用来去除头尾的空格

最后那几个是最坑的，谁能想到居然茫茫文海中有人在标题里插了一个制表符`\t`，结果制表符当然从肉眼上看和空格也差不多，但是并不能当做文件名，就报错。真是令人大跌眼镜。

PS：

如果说插入制表符`\t`还能够原谅，那在标题里插入换行符`\r`和`\n`的，简直是泯灭人性。可是文章看多了，这样的奇事总是有，只好加以针对处理之。

有人会问，为什么要把`strip()`放在最后呢？

那是因为我们要os库的新建文件夹是以我们传入的`title`作为参数，如果`title`的末尾有空格，比如`《金庸列女传》全集 `（注意最后有一个空格）和`《金庸列女传》全集` （最后没有空格）在`os.path.exist()`中是被对待为等同的。

但是当你到了后面文本保存的那一刻，`《金庸列女传》全集 \金庸列女传.txt`和`《金庸列女传》全集\金庸列女传.txt`是完全不同的路径，在写入文本文件的时候就会产生路径不存在的报错。

因此在替换完所有的非法字符之后再在最后一步进行删除左右的空格的操作，是有必要的。

有时候，网页会被跳转，比如原帖被删除了，这种时候，`soup`虽然可以得到，但是从`soup`中什么都解析不出来，只能返回一个空值`None`，如果我们继续使用`strip()`函数，就会报错。从一个不存在的对象中，当然也无法继续后续的诸多操作，因此要及时放弃，中断循环。

所以先判断有没有合法的返回值，如果没有，就返回`None`，在后续的代码中，如果拿到`None`，就说明网页这里被跳转了，就触发中断循环的操作，避免后续的错误。

---

### 第五个函数

接下来这个函数的作用就是把title后面加个`.txt`，简单易懂。

```python
def file_name(title):
    return "".join([title, '.txt'])
```

---

### 第六个和第七个函数

接下来是文章分析器的函数`extract_text(soup)`和`extract_classbk(soup)`，用来提取正文。

之所以写了两个函数是对应新版与旧版的网页，它们的结构不同。

这个没有什么特别省事的方法，只能没完没了一点一点对照html的源码，一点点地调试，看看出来的是什么。

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

有关BeautifulSoup（以下简称bs4）的用法，官网有很详细的说明，CSDN上也有一些教程，主要的几个用法就是从HTML的标签中提取出我们需要的信息，不管是字符串还是a标签（超链接）的属性（也就是链接），都可以轻松使用bs4来提取，并保存到列表，为后续的去重做铺垫。

`input()`函数在这里起到的作用是提供一个暂停的机会，等待键盘的响应。如果只是放一个print在这里，等错误产生的时候，你可能完全没有注意到，就一闪而过，被后续的信息给淹没，完全没有注意到它。

---

### 第八个函数

创建`create_folder_as_per(foldername)`函数用来建立文件夹。

为了实现代码功能的构想，需要输入一个文件夹的名字，得到一个文件夹。

出于~~省事~~迁移方便的目的，选择在`study.py`所在的文件夹建立新的文件夹。

用`if not os.path.exists(foldername)`来判断文件夹是否已经存在，如果存在就打印一条提示语句，不存在的情况下才建立文件夹，避免浪费和重复。

```python
def create_folder_as_per(foldername):
    if not os.path.exists(foldername):
        os.makedirs(foldername)
        print(f"建立文件夹{foldername}")
    else:
        print(f"{foldername}文件夹已经存在")
```

---

### 第九个函数

有时候看文章看到结局，发现文章不全，里面充斥着乱码，或者干脆打开发现是一个空文件，这时候往往陷入自我怀疑：

是不是我的代码写得不对，文章没抓取完全，还是我的解析器哪里出了问题，乱码是从哪冒出来的？

究竟是我的问题，还是手机端的txt阅读器的问题？

这时候，如果在文章的末尾加一个出处，附上这个页面从哪个网址扒下来的，可就太有用处了。

所以创造函数`rilla_save(path, para, url)`来文本的末尾实现添加出处，并将**规定的文本**写入**规定的路径、规定的文件名**的txt文件中的功能。

```python
def rilla_save(path, para, url):
    paragraph_with_footer = para + '\n' + '\n' + '页面来源： ' + url
    with open(path, 'wt', encoding='utf-8') as f:
        f.write(paragraph_with_footer)
```

函数参数`path`，`para`，`url`的意义分别是：

`path`是要保存的文本文件的绝对路径

`para`是paragraph的缩写，意为段落，当然就是从上面解析出来的正文段落

`url`是要附加的页面地址。

用连接符号`+`把它们连在一起就好了，当然也可以用join，我懒了……

里面的两个`'\n'`的作用是插入两个“换行”，如果没有换行，直接紧跟在正文的文本后面，一来不容易看到；二来也没有层次感，破坏了看文的好心情。

这样任何一个txt文件打开，拉到最后，就能看到文章来源，如果有疑问，在怀疑自己之前，先去网页上看一眼，就会发现原来网站上原文就是一堆乱码，就是空白页，就是写到一半没有然后了。

宽恕自己，善莫大焉。

再用`with`语句，以UTF-8的编码创建并写入文本文件。打开模式选择`'wt'`，是`write text`的缩写，它是覆盖型的，这里是创建新文件，所以无所谓覆盖。

使用`with`语句好处多多，首先是能够确保打开的文本文件会被正确的关闭，有些老掉牙的教程会教你用`.open()`、`.write()`和`.close()`来处理文本文件的写入，太麻烦。

时代进步了，咱们也要与时俱进啊～

至于函数名中的rilla表示什么？那是我的英文名ヽ(*ﾟдﾟ)ノｶｲﾊﾞｰ

---

### 第十个函数

接下来这个函数`rename_and_savetext(folder, txt_name, para, url)`是整个代码中最有含金量之一的部分。

```python
def rename_and_savetext(folder, txt_name, para, url):
    '''
    以页面的标题作为文件夹的名字，把所有的txt保存在这个文件夹内
    '''
    txt_path = "".join([folder, '\\', txt_name])
    if not os.path.exists(txt_path):
        rilla_save(txt_path, para, url)
    else:
        print(f"啊哦，想要下载的文件 {txt_path} 已经有了，加_2处理之")
        auto_rename_2 = txt_path[:-4] + '_2' + '.txt'
        if not os.path.exists(auto_rename_2):
            print(f"新文件将被命名为{auto_rename_2}")
            rilla_save(auto_rename_2, para, url)
        else:
            print(
                f"啊哦，想要下载的文件 {auto_rename_2} 已经有了（已经试过重命名了），要怎么办呢？")
            overwrite_or_not = input(
                "覆盖/用url后几位数字来重命名/跳过？ （y/r/其它任意键）")
            if overwrite_or_not.lower() == 'y':
                rilla_save(auto_rename_2, para, url)
            elif overwrite_or_not.lower() == 'r':
                print(f"见鬼了，这个文件名居然也存在？算了，用url来命名吧。")
                giveup_name = url.split('tid=')[-1] + '.txt'
                giveup_path = "".join([auto_rename_2[:-4], '_', giveup_name])
                rilla_save(giveup_path, para, url)
            else:
                print("算了，跳过不理")
```

函数很长，看起来有点头晕，所以我们分段讲解。

首先是参数，其实参数一般都是先写完函数，看看缺什么，往里填什么。

四个参数`(folder, txt_name, para, url)`里面：

`folder`自然就是文件夹的名字

`txt_name`是文本文件的名字，也就是那个网页的标题

`para`是正文内容

`url`是网页所在的地址

```python
    txt_path = "".join([folder, '\\', txt_name])
    if not os.path.exists(txt_path):
        rilla_save(txt_path, para, url)
    else:
        print(f"啊哦，想要下载的文件 {txt_path} 已经有了，加_2处理之")
        auto_rename_2 = txt_path[:-4] + '_2' + '.txt'
        if not os.path.exists(auto_rename_2):
            print(f"新文件将被命名为{auto_rename_2}")
            rilla_save(auto_rename_2, para, url)
```

在我的构想中，一个小说应该是放在同一个文件夹里面。
比如著名的《金鳞岂是池中物》，就是一个文章，正文所在全是链接，点进去一个章下面居然又在回帖区充满了各种链接。

我们固然要谴责这种套娃的恶劣行径，另一方面也不能束手无策，还是要运用智慧加以解决之。

首先还是用`join`函数来拼接文件夹和文本文件的文件名，形成一个完整的`路径`。

如果**没有重名**，直接给`路径`，和`正文的内容`，还有`文章的地址（url）`调用上一步创建的`rilla_save()函数`就直接保存了。

然后考虑到帖子有时候有重名的时候，尤其是某个作者会写上百章的长篇小说，写到后面他也想不起来这是第几章，就会出现两个788章，却没有789章这种事。

其实这有时候也不能怪发帖者，情色小说嘛，很多电子情色小说最早起源于上古时代的元元图书馆，经过这么多年的转载、转载、转载，早就被水印、回复可见等等篡改地面目全非，全本本来就很难得，更多的已经散佚了。能有些热心人士靠着热情服务社区，给大家提供自己搜集来的各种版本，本来就不应加以苛责才是。

其实我说了这么多，就是想说，有相当数量的文章都不是作者亲自发布，而是时隔多年后由一个不相干的人来转载。那转载的人一天要转载那么多文章，错漏在所难免。

当然，我们宁可错杀三千，不开放过一个。与其粗暴选择覆盖，不如重命名，比如加一个_2在后面。

同时，在遇到这样的情况时，因为特别常见，如果每次都停下来，很耽误时间，不妨让程序自动处理。当_2也重复的时候，再来询问该如何处理之。

这里注意到用了切片的方式来处理字符串，把原先路径中的`'.txt'`去掉。

有人想说为啥不能用`-`来做这件事，像下面这样呢？

`auto_rename_2 = txt_path - '.txt' + '_2' + '.txt'`
想法是好想法，可是Python中只有`+`作为连接符，并不是想当然把`-`当做删减的符号。

可惜了，只能曲线救国啦。当然，用`replace`也是可以的，毕竟除了格式名，不太可能会有`'.txt'`出现在文件名和其它位置。

```python
        else:
            print(
                f"啊哦，想要下载的文件 {auto_rename_2} 已经有了（已经试过重命名了），要怎么办呢？")
            overwrite_or_not = input(
                "覆盖/用url后几位数字来重命名/跳过？ （y/r/其它任意键）")
            if overwrite_or_not.lower() == 'y':
                rilla_save(auto_rename_2, para, url)
            elif overwrite_or_not.lower() == 'r':
                print(f"见鬼了，这个文件名居然也存在？算了，用url来命名吧。")
                giveup_name = url.split('tid=')[-1] + '.txt'
                giveup_path = "".join([auto_rename_2[:-4], '_', giveup_name])
                rilla_save(giveup_path, para, url)
            else:
                print("算了，跳过不理")
```

`if`，`elif`，`else`结构在这里非常容易理解，一个不行就找另一个，总有一个适合它。

最后为了防止无限套娃，出现`_2_2_2_2`这种长的离谱的后缀，应考虑用不同的规则来命名文件。

通常说来，帖子的id应该是唯一的，也就是`tid＝`后面那一串数字。这里使用`split('tid=')[-1]`函数加切片，以`tid＝`为界，选择后面的数字提取出来，加上`.txt`。

再把前面的文件名后面去掉`.txt`，拼上`下划线`和刚刚的这个数字，放在上面的那串字符串的前面。就构成了一个新的字符串。

至于菜单选择，`overwrite_or_not.lower() == 'r'`，这里用了`.lower()`函数，反正输入的是一个ascii字符，直接用它就可以保证你不管是按下的是<kbd>R</kbd>还是<kbd>r</kbd>，都可以得到妥善的处理。

这样万一你的键盘不小心锁定了大写，你以为按下的<kbd>r</kbd>，实际上是<kbd>R</kbd>，代码也会把<kbd>R</kbd>当做<kbd>r</kbd>，不会产生不想要的误操作了。

---

### 第十一个函数

接下来就到了提取页面的超链接的部分了。

留园的小说最大的困扰就是页面到处有链接，正文有，底部也有。

而且很容易就错过，错过了就会导致保存的章节不全，你也不知道是作者没写完，是散佚了，还是你没有爬取完全。

所以为了避免看得正爽的时候戛然而止的扫兴，有必要开发一个功能强大的“超链接提取器”——

`hyperlink_extractor(url, header, test='off')`

参数十分简单，通常来说，越简单，越可靠不是嘛。

```python
def hyperlink_extractor(url, header, test='off'):
    '''
    用于提取一个单独页面中正文和底部的所有链接

    并返回一个包含url的列表
    '''
    if test == 'on':
        print("提取一个单独页面中正文和底部的所有链接")  # 测试用
    url = url.replace('amp;', '').replace('http:', 'https:')
    if test == 'on':
        print(url)  # 测试用
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
        print(hyperlink) if test == 'on' else ''  # 测试用
        href = hyperlink.get('href').replace(
            '&amp;', '').replace('http:', 'https:')
        if 'http' not in href:
            realurl = "".join(['https://www.cool18.com/bbs4/', href])
            postlist.append(realurl)
        else:
            postlist.append(href)

    if test == 'on':
        print('='*30)  # 测试用

    # 底部链接列表
    li = soup.find_all('li')
    for reply in li:
        bytes = reply.text.split(' bytes)')[0]
        bytes = bytes.split(' (')[-1]

        # 根据留言的bytes数来筛选真的补充帖子，bytes数小于600的一律不作数
        if bytes.isdecimal() and int(bytes) > 6000:
            print(reply) if test == 'on' else ''  # 测试用
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

    # return postlist
    if test == 'on':
        print('='*30)  # 测试用
    if test == 'on':
        print(postlist)  # 测试用
    # 对列表去重并保留原顺序
    only_postlist = []
    [only_postlist.append(i) for i in postlist if not i in only_postlist]

    return only_postlist
```

依旧是分段解读

```python
    if test == 'on':
        print("提取一个单独页面中正文和底部的所有链接")  # 测试用
    url = url.replace('amp;', '').replace('http:', 'https:')
    if test == 'on':
        print(url)  # 测试用
```

上面这一段的作用基本上之前的函数中都出现过，很容易理解的。

```python
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

页面有时候很纷杂，我们并不需要花里胡哨的JavaScript的脚本代码来拖后腿，找到对应的javaScript关键词标签，也就是`<script>`，用bs4的`decompose()`函数来抛弃掉。

与之前的抛弃`<table>`函数不一样的地方，在于这里用了循环，务求一网打尽。

```python

    postlist = []

    # 获取正文里面的链接
    para = soup.find('pre')
    a_para = para.find_all('a')
    for hyperlink in a_para:
        if not hyperlink.get('href'):  # 当href不存在的时候，跳过
            continue  # <a target="_blank"></a>
        print(hyperlink) if test == 'on' else ''  # 测试用
        href = hyperlink.get('href').replace(
            '&amp;', '').replace('http:', 'https:')
        if 'http' not in href:
            realurl = "".join(['https://www.cool18.com/bbs4/', href])
            postlist.append(realurl)
        else:
            postlist.append(href)
```

依这里的注释所说，首先去获取正文里面的链接。

留园文章的正文都在`<pre>`标签里面，获取起来不费吹灰之力。

接下来获取超链接的a标签，拿到之后，依旧是清洗数据格式，确保是正确合法的带有https的url格式。

你可能会好奇，为啥好端端要加一个判断，`if not hyperlink.get('href'):`

那是因为总有各种意外没完没了的出现啊：

比如某一个大神在文章中非要插一个图片。你插就插吧，还非要插一个外链的图片，那也罢了，可是这个外链还挂了，以至于被网站替换成了一个空链接，成了下面这样：

`<a target="_blank"></a>`

于是我们可爱的代码在执行到`href = hyperlink.get('href')`这一步的时候就毫不意外的挂了。

当`href`不存在的时候，上述的命令返回的就是一个`None`，`None`在Python中等价于`False`，所以`if not hyperlink.get('href'):`的意思在`hyperlink.get('href'):`返回了`None`的那一刻，就成了`if not False:`

`if not False:`是`if`和`not False`的合体。

`不假`就是`真`，`真`就满足`if`，就跳过<u>这个a标签</u>，去找下一个，也就是<u>包含href属性的那个a标签</u>。

多么有趣的Python编程啊！

深吸一口气，继续往下看

```python
    if test == 'on':
        print('='*30)  # 测试用

    # 底部链接列表
    li = soup.find_all('li')
    for reply in li:
        bytes = reply.text.split(' bytes)')[0]
        bytes = bytes.split(' (')[-1]

        # 根据留言的bytes数来筛选真的补充帖子，bytes数小于600的一律不作数
        if bytes.isdecimal() and int(bytes) > 6000:
            print(reply) if test == 'on' else ''  # 测试用
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

上面这一段，我自己是感到比较满意的。

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

那这种时候，无限加关键词，岂不是成了和谐词系统，我又不想开发一个“墙”。

仔细观察，发现通常有料的那个链接，Bytes数比较大，可见Bytes数越大，内容越多，是文章的概率就越大。经过反复测试与比较，感觉6000是一个比较合适的阈（yù）值。

```python
    for reply in li:
        bytes = reply.text.split(' bytes)')[0]
        bytes = bytes.split(' (')[-1]
        if bytes.isdecimal() and int(bytes) > 6000:
```

这里使用了`.isdecimal()`函数来确保拿到的bytes它是个数字。

为什么要强调这一点呢？因为有个别网页，里面它的链接并不在整个页面的底部，而是在正文的下方，所以也没有`bytes`这种东西。

Python中的变量只是一个名字，不是说你叫它`bytes`（变量名）它就真的是`bytes`（字面意思），完全有可能用`左括号`切片切出来的是一个字符串，如果直接用`int()`转换，那就报错了。

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
    # return postlist
    if test == 'on':
        print('='*30)  # 测试用
    if test == 'on':
        print(postlist)  # 测试用
    # 对列表去重并保留原顺序
    only_postlist = []
    [only_postlist.append(i) for i in postlist if not i in only_postlist]

    return only_postlist
```

最后到了要添加到列表的环节，添加之前先去重。不然有的文章正文和底部的链接都指向同一个章节，我们岂不是要白白下两次？

当然有人说可以用`list(set(list()))`的骚操作，利用set集合的无重复元素的特性来去重。但是那样一来，顺序就乱掉了。

对于这样一个动辄80篇帖子起步的网站，如果我们的列表顺序乱了，那么在报错的时候，就很难判断到底是哪一个帖子产生了错误。

如果是按顺序来，那么查找的时候就方便多了。

有鉴于此，用了这样一个稍显复杂，但是的确管用的方法来去重，保证了原有的顺序，生活又有了希望，不是吗。

---

### 最后一个函数

千呼万唤，我们终于来到了这总装的最后一步：

把上述介绍的所有的函数一层一层的套在一起，就有了以下的这个总装函数。

```python
def crawl(header, test='off'):
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
                if test == 'on':
                    print('='*30)  # 测试用
                    print(f"{article}")
                    print('='*30)  # 测试用
                top_soup = get_soup_from_webpage(article, header)
                top_title = find_title(top_soup)
                if top_title == None:
                    print("文章已经被删掉了，跳转去了主页")
                    break  # 文章已经被删掉了，跳转去了主页
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
                    soup = get_soup_from_webpage(posturl, header)
                    page_title = find_title(soup)
                    if page_title == None:
                        print("文章已经被删掉了，跳转去了主页")
                        break  # 文章已经被删掉了，跳转去了主页
                    print(page_title)
                    if test == 'on':
                        print(posturl)  # 测试用
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

                    # 有的王八蛋特别变态，把文本隐藏在更深的章节里
                    secondary_list = hyperlink_extractor(posturl, header)
                    if secondary_list:
                        secondary_folder_path = "".join(
                            [top_title, '\\', page_title])
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
                                    break  # 文章已经被删掉了，跳转去了主页
                                print(second_title)
                                if test == 'on':
                                    print(second_level)  # 测试用
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

对于这个函数的理解，需要正确掌握Python的函数中的形参和实参的概念。

虽然很多教材说的云里雾里，说白了就是形参就是形式上的参数，放在那个位置就是占一个地儿，名字不重要，位置很重要。当然你的名字对上了，位置也就不重要。

所以如下的函数里面的`pos1`和`pos2`只是占一个位置，你自己记得哪个是哪个，用的时候完全可以放不同的东西进去。

当然，变量的类型很重要，是`str`还是`int`要搞清楚，不然就会出错。

```python
def functional(pos1, pos2):
    return pos1 + pos2
```

此外还用到了一个很好用的结构，try……except……，不知道try里面的代码是否work的时候，先try它一下，有问题就退出来执行except里面的部分，所以我用它来做了一个提取错误链接的保存功能：

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

虽然我们已经考虑的很合理了，但是在实际运行过程中，一定会遇到各种事先所想象不到的困难，如果每次出错都要停下来排故，那就太痛苦了。

所以设立了一个“错题本”，遇到错误就把发生错误的文本的地址记下来，存到文本文件里去，等之后再翻出来一一解决。

这样就可以极大地提升工作的效率。

对于整个函数来说，虽然看起来很长很吓人，但是都是一点点往里面填充细节，而且很多错误是一开始未曾想到，在运行中一点点发现，再回过头来增补的。

整个函数的架构可以分解成以下这个样子：

```python
def crawl(header, test='off'):
    failed_log_list = []  # 新建一个错题本的列表
    article_page_url = main_page_url_generator()  # 用页面生成器拿到每一个主页的地址
    for each_page in article_page_url:
        # 根据每一个主页，依次获得每个主页上那200个文章的地址
        article_list = get_articles(each_page, header)
        for article in article_list:
            try:
                见代码块A讲解
                保存article的正文
                提取article的链接，存入post列表

                for posturl in postlist:
                    见代码块B讲解
                    保存二级链接网页的正文
                    提取二级网页里面附带的链接（如果有），存入secondary_list列表

                    if secondary_list:
                        见代码块C讲解
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

两个值得一讲的段落：

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

这一小段实际上是两个部分，先用`extract_classbk(top_soup)`和`extract_text(top_soup)`提取正文`para`，再用`postlist = hyperlink_extractor(article, header)`来提取<u>该正文所在页面上的链接列表</u>

下面用`if len(para) >= 1000 or postlist:`来判断正文是不是足够长（因为有些页面上，只有短短的两句毫无信息量的废话）或者有**有价值的**链接。两个条件只要满足任何一个，就调用`create_folder_as_per(top_title)`函数来新建一个文件夹。
并在这个文件夹里面调用用于保存的`rename_and_savetext()函数`执行保存操作。

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
        break  # 文章已经被删掉了，跳转去了主页
    print(page_title)
    if test == 'on':
        print(posturl)  # 测试用
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

用threadview做关键词基本上就能把非留园的帖子都过滤去除掉了，还是比较好用的。

剩下的代码部分就和代码块A里面的基本上一样，重复了一遍相同的流程罢了。唯一的区别是不再需要判断正文是否存在，也不需要再建立新的文件夹，省事省心。

#### 代码块C

原谅我有点烦躁，毕竟真的遇到那样令人抓狂的作者也是很头疼的，好好的页面他不用，非要在跟帖区贴链接，链接打开又是链接……

要是写的特别长篇大论倒也罢了，一共就2000来字，还要分八章，分布在那么多页面里……

莫非文章都是坐在马桶上写的么……

```python
# 有的王八蛋特别变态，把文本隐藏在更深的章节里
secondary_list = hyperlink_extractor(posturl, header)
if secondary_list:
    secondary_folder_path = "".join(
        [top_title, '\\', page_title])
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
                break  # 文章已经被删掉了，跳转去了主页
            print(second_title)
            if test == 'on':
                print(second_level)  # 测试用
            second_txt_name = file_name(second_title)
            body_text = extract_text(second_soup)
            if body_text:
                rename_and_savetext(
                    secondary_folder_path, second_txt_name, body_text, second_level)
        except:
            print("算了，跳过不理")
```

因为是链接的链接的文章，所以还是要再在主文件夹里创建一个子文件夹，把那八章的txt文件一股脑放进新的子文件夹中。

为什么要这样呢？

原因很简单，因为会把文章写到这一层的作者，在给文章的页面起标题的时候通常都是简单粗暴毫无逻辑缺乏美感。

平平无奇的“第一节”三个字，他可以从上一级文章的“第1章”一直用到“第88章”。

如果我们不为每一个“第X章”建立一个单独的子文件夹，那么这88个“第一节.txt”就会一个覆盖一个。你爬了半天，打开一看只有最后一章的第一节保存了下来，之前爬取的文件都被覆盖了。

就算我们用了重命名的高端算法，让这88个txt并存，也会有88个包含“第一节”的文件名的txt在文件夹里，你也根本搞不清这么多的“第一节”分别是哪一章的“第一节”。

创建子文件夹其实就是在原来的路径上去掉最后的`.txt`再继续加个`反斜杠\`再加`.txt`就是新的路径了，看起来复杂，实际上跟重命名文件的套路一脉相承。

最后要说明的是，为什么我们的传入参数的变量名变来变去，一会儿是`title`，一会儿是`top_tile`一会儿是`second_title`呢？

这就是本节开篇说的，要搞明白形参与实参的意义了，因为Python的变量虽然是私有，并非全局变量，但是在同一个函数中，变量名在这个函数的作用域里是全局的。

在上一个循环和下一个循环中，虽然函数调用的是同一个，但是函数的参数实际上是完全不同的，第一级的文章的链接和第三级的当然不应该混用，不然就会出现各种匪夷所思的结果。

举个例子，如果把`喊(爸爸)`当做一个函数，`你爸爸喊的(爸爸)`跟`你喊的(爸爸)`必然不是同一个人，这里`(爸爸)`就是形参，`被喊的“爸爸”`是实参。

---

### 还没完，别忘了最后一步

千辛万苦，整个代码到了可以运行的时候啦。

```python
if __name__ == '__main__':
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46'}
    crawl(header)
```

还记得我们写第一个函数的时候，把header放在了代码开始执行的地方吗？

记得回到这里，把我们刚刚总装的函数放在这里，让函数可以从这里开始运行。

将`study.py`拷贝到一个清爽的空文件夹里，然后打开你的CMD或者Powershell，执行这个文件，看着字符在屏幕上跳动，你的txt文件哗啦啦地在硬盘里生成吧。

---

## 后记

整个代码写了好几个晚上，实际运行超过六个小时，扒拉下来3.36 GB的txt文件。

一共得到了70,346个文件，6,316个文件夹。

据统计，在txt中差不多每1GB可以保存五亿汉字，那么估算了一下，留园上的精品情色小说的总字数高达15亿汉字。

朋友们，大部头的《红楼梦》也只有70几万字而已。

可见生理欲望是人类文明发展的源源不断的动力啊。

但是我发现，下载了如此浩瀚的小说，可能我这一辈子也看不完其中的百分之一吧。

网民们的创作力是无穷的，而我的精力是有限的，呜呼哀哉！

真的想再活五百年啊～～

PS：

当然，这15亿汉字的小说里面有很多是重复的，毕竟我们采用的爬取方法并没有对帖子进行去重处理，而且有时候同一个小说会被来回引用转载，十万字的小说可以以不同的名字转载保存在网站的不同位置，轻而易举产生二百万字以上的空间，但是看来看去都是同一篇小说。

而且有些小说创作年代实在太过久远，不同的人通过不同的途径保存下来的章节出入很大，加上无数论坛、网站兴衰更迭，无数伸手党与搬运工转载就没转全，再加上敏感词和谐系统的出现，大量的删节与散佚。无数缺乏耐心与敬业精神的作者弃坑，断更，冒名顶替者续写，改写，替换主人公的姓名，拼接不同文章里的情节，换个名字把转载当原创，李鬼冒充李逵的现象比比皆是。

诞生只有不到二十年的华语情色小说尚且有如此大的分野，先秦时代的文学作品能流传到今天，也实属不易。

---

## 感谢

感谢所有为中文情色小说奉献过创意与想法的每一个人，感谢留园的版主: 小脸猫 青青的世界 。

大家都是一个个的普通人，既非圣贤，七情六欲只要在法律允许的边界之内，在幻想与现实中，找到一个平衡点，也是人生乐趣的一部分啊。
