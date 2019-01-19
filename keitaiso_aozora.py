import matplotlib.pyplot as plt
from wordcloud import WordCloud
from bs4 import BeautifulSoup
import urllib.request
import MeCab as mc
import collections

#形態素解析
def mecab_analysis(text):
    t = mc.Tagger()
    result = t.parse(text)
    output = []
    for row in result.split("\n"):
        word = row.split("\t")[0]
        if word == "EOS":
            break
        else:
            word_type = row.split("\t")[1].split(",")[0]
            if word_type == "名詞":
                output.append(word)
    return output

#青空文庫のテキストを抽出
def get_text_of_aozora_bunko(url):

    soup = BeautifulSoup(urllib.request.urlopen(url).read(), "html.parser")
    main_text = soup.find("div", class_="main_text")
    text = main_text.text
    return text

# ワードクラウドを作成
def create_wordcloud(text):

    fpath = "foo"   #フォントの場所

    wordcloud = WordCloud(background_color="white",font_path=fpath, width=900, height=500, \
                          stopwords={}).generate(text)

    plt.figure(figsize=(15,12))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()

# csvファイルを作成
def create_csv(words):
    data = collections.Counter(wordlist)
    freq = data.most_common()
    with open("output.csv", "w") as f:
        for row in freq:
            print(*row, sep=",", file=f)


url = "sample.html"      #サンプル（青空文庫の作品のurl）
text = get_text_of_aozora_bunko(url)
wordlist = mecab_analysis(text)
create_csv(wordlist)
create_wordcloud(" ".join(wordlist))
