import os
import requests
from bs4 import BeautifulSoup
from typing import Optional

# 2022年10月30日

HEADER = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0)'
    ' Gecko/20100101 Firefox/106.0',
}

SAVE_DIRECTORY = r'D:\Rilla\cool18'


def get_soup_from_webpage(url: str, header: dict) -> BeautifulSoup:
    response = requests.get(url, headers=header, timeout=15)
    if 'classbk' in url:
        response.encoding = 'gb2312'
    else:
        response.encoding = 'utf-8'
    content = response.text
    soup = BeautifulSoup(content, 'lxml')
    return soup


def main_page_url_generator() -> str:
    '''
    翻页系统，生成留园主页第1页到第23页的地址
    '''
    article_page_url = []
    main_page = 'https://www.cool18.com/bbs4/index.php?app=forum&act=gold'  # 禁忌书屋首页
    article_page_url.append(main_page)
    for page in range(2, 24):
        newpage = "".join([main_page, '&p=', str(page)])  # 第2页到第23页的地址
        article_page_url.append(newpage)
    return article_page_url


def get_articles(url: str, header: dict) -> list:
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


def find_title(soup: BeautifulSoup) -> Optional[str]:  # 寻找文章的标题
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


def file_name(title: str) -> str:
    return "".join([title, '.txt'])


def extract_text(soup: BeautifulSoup) -> str:
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


def extract_classbk(soup: BeautifulSoup) -> str:
    try:
        pre = soup.get_text()
        raw_words = pre.replace('www.6park.com', '').replace('6park.com', '')
        return raw_words
    except:
        input("啊哦，好像有点不对劲，检查一下代码吧。按任意键继续")


def create_folder_as_per(foldername: str):
    if not os.path.exists(foldername):
        os.makedirs(foldername)
        print(f"建立文件夹{foldername}")
    else:
        print(f"{foldername}文件夹已经存在")


def rilla_save(path: str, para: str, url: str):
    paragraph_with_footer = para + '\n' + '\n' + '页面来源： ' + url
    with open(path, 'wt', encoding='utf-8') as f:
        f.write(paragraph_with_footer)


def rename_and_savetext(folder: str, txt_name: str, para: str, url: str):
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


def hyperlink_extractor(url: str, header: dict) -> list:
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


def crawl(header: dict):
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


if __name__ == '__main__':
    os.chdir(SAVE_DIRECTORY)
    crawl(HEADER)
