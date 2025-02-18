import json


def get_articles() -> dict:
    with open("articles.json", "r", encoding='utf-8') as json_f:
        text = json.load(json_f)
    return text


def save_article(name: str, text: str):
    with open("articles.json", "r", encoding="utf-8") as f:
        articles = json.load(f)
    articles[name] = text
    with open("articles.json", "w", encoding="utf-8") as f:
        json.dump(articles, f, ensure_ascii=False)



def delete_article(name: str):
    with open("articles.json", "r", encoding="utf-8") as f:
        articles = json.load(f)
    del articles[name]
    with open("articles.json", "w", encoding="utf-8") as f:
        json.dump(articles, f, ensure_ascii=False)


