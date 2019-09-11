import os
import time
import requests

product_id = '4488439'
url_base = 'https://sclub.jd.com/comment/productPageComments.action?productId='
url_page_pattern = '&score=0&sortType=5&page='
url_tail = '&pageSize=10&isShadowSku=0&fold=1'

output_file_path = './%s_comment.jd' % product_id

data_expect_to_retrieve = 100
cool_down_time = 5  # in secs

# 请求头
headers = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/74.0.3729.169 Safari/537.36',
    'Referer': 'https://item.jd.com/100004325476.html',
    'Host': 'sclub.jd.com'
}


def get_comment(page_idx):
    # 请求
    url_builder = url_base + product_id + url_page_pattern + str(page_idx) + url_tail
    req = requests.get(url_builder, headers=headers)

    # 数据处理
    res = req.json()  # 转换成python对象
    comments = res['comments']

    total = []
    for comment in comments:
        comment_content = comment['content']
        format_string = comment_content.replace('\n', ';') + "\n"
        total.append(format_string)
    return total


if __name__ == '__main__':
    
    fh = open(output_file_path, "w", encoding='utf-8')

    iteration = int(data_expect_to_retrieve / 10)
    
    for idx in range(iteration):
        res = get_comment(idx)
        fh.writelines(res)
        fh.flush()
        time.sleep(cool_down_time)

    fh.close()