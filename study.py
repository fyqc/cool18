import os
import requests
from bs4 import BeautifulSoup

# 2021年6月1日


def get_soup_from_webpage(url, header):
    response = requests.get(url, headers=header)
    if 'classbk' in url:
        response.encoding = 'gb2312'
    else:
        response.encoding = 'utf-8'
    content = response.text
    soup = BeautifulSoup(content, 'lxml')
    return soup


def find_title(soup):  # 寻找文章的标题
    title = soup.title.get_text()
    title = title.strip()
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
    return title


def file_name(title):
    return "".join([title, '.txt'])


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


def create_folder_as_per(foldername):
    if not os.path.exists(foldername):
        os.makedirs(foldername)
        print(f"建立文件夹{foldername}")
    else:
        print(f"{foldername}文件夹已经存在")


def rilla_save(path, para, url):
    paragraph_with_footer = para + '\n' + '\n' + '页面来源： ' + url
    with open(path, 'wt', encoding='utf-8') as f:
        f.write(paragraph_with_footer)


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
                giveup_path = "".join(
                    [folder, '\\', auto_rename_2[:-4], '_', giveup_name])
                rilla_save(giveup_path, para, url)
            else:
                print("算了，跳过不理")


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
        print(hyperlink) if test == 'on' else ''  # 测试用
        if not hyperlink.get('href'):  # 当href不存在的时候，跳过
            continue  # <a target="_blank"></a>
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
        # print(bytes)
        # bytes = reply.text.split('bytes')[0]
        # print(bytes)
        # bytes = bytes.split(' ')[-2][1:]
        # print(bytes)

        # 根据留言的bytes数来筛选真的补充帖子，bytes数小于600的一律不作数

        if int(bytes) and int(bytes) > 6000:
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
                top_soup = get_soup_from_webpage(article, header)
                # 【欲恋】（０１－６１）作者_ 爱夜夜夜夜
                top_title = find_title(top_soup)
                print(top_title)
                create_folder_as_per(top_title)
                postlist = hyperlink_extractor(article, header)
                for posturl in postlist:
                    soup = get_soup_from_webpage(posturl, header)
                    page_title = find_title(soup)
                    # 【欲恋】 (46-50)
                    print(page_title)
                    txt_name = file_name(page_title)
                    if 'classbk' in posturl:
                        paragraph = extract_classbk(soup)
                    else:
                        paragraph = extract_text(soup)
                    # 将正文保存为文本
                    rename_and_savetext(
                        top_title, txt_name, paragraph, posturl)
                    # 有的王八蛋特别变态，把文本隐藏在更深的二级章节里
                    secondary_list = hyperlink_extractor(posturl, header)
                    if secondary_list:
                        secondary_folder_path = "".join(
                            [top_title, '\\', page_title])
                        create_folder_as_per(secondary_folder_path)
                        print(secondary_folder_path)
                        for second_level in secondary_list:
                            if 'cool18' not in second_level:
                                continue
                            try:
                                second_soup = get_soup_from_webpage(
                                    second_level, header)
                                second_title = find_title(second_soup)
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


if __name__ == '__main__':
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46'}
    crawl(header)
