import os

import jieba
from wordcloud import WordCloud

# 字体路径
custom_font_path = r'/System/Library/Fonts/PingFang.ttc'

def word_cloud(filename):
    f = open(r'./input/' + filename, 'r', encoding='utf-8')
    t = f.read()
    t = t.replace('\n', '')
    f.close()

    # 停用词
    with open(r'./stop_words.txt', 'r') as file:
        custom_stopwords = file.read().split()

    words = jieba.lcut(t)
    words = [element for element in words if element not in custom_stopwords]
    txt = ' '.join(words)
    # print(txt+"\n")

    wc = WordCloud(
        font_path=custom_font_path,
        width=500, height=400,
        background_color='white',
        min_font_size=16,
        max_font_size=72,
        relative_scaling=0.5,
        max_words=100
    )

    wc.generate(txt)
    wc.to_file(r'./output/' + filename + '.png')


def main():
    for filename in os.listdir(r'./input'):
        if os.path.isfile(os.path.join(r'./input', filename)) and filename.endswith('.txt'):
            word_cloud(filename)


if __name__ == '__main__':
    main()
