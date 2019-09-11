import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt

file_to_process = "./4488439_comment.jd"
font_to_use = r"C:\Windows\Fonts\SIMHEI.TTF"
ignore_words = ["很", "非常", "京东", "JD", "jd", ".com"]

def main():

    fh = open(file_to_process, "r", encoding='utf-8')
    data_lines = fh.readlines()
    fh.close()

    words = ''
    for data in data_lines:
        words += ' '.join(jieba.cut(data))

    cloud = WordCloud(
        font_path=font_to_use,
        background_color="white",
        width=1000,
        height=800,
        stopwords=ignore_words
    ).generate(words)

    plt.imshow(cloud)
    plt.axis("off")
    plt.show()
    
main()
