# !pip install fastcore
# !pip install jp_pref
from jp_pref.prefecture import name2code


hokkaido = name2code(["北海道"])
tohoku = name2code(["青森県", "岩手県", "秋田県", "宮城県", "山形県", "福島県"])
kanto = name2code(["茨城県", "栃木県", "群馬県", "埼玉県", "千葉県", "東京都", "神奈川県"])
chubu = name2code(["新潟県", "富山県", "石川県", "福井県", "山梨県", "長野県", "岐阜県", "静岡県", "愛知県"])
kansai = name2code(["三重県", "滋賀県", "奈良県", "和歌山県", "京都府", "大阪府", "兵庫県"])
chugoku = name2code(["岡山県", "広島県", "鳥取県", "島根県", "山口県"])
shikoku = name2code(["香川県", "徳島県", "愛媛県", "高知県"])
kyushu = name2code(["福岡県", "佐賀県", "長崎県", "大分県", "熊本県", "宮崎県", "鹿児島県", "沖縄県"])

def pref2area(pref):
    try:
        pref = name2code(pref)
    except:
        print("都道府県名を入力してください")
        return

    if pref in hokkaido:
        return "北海道"
    elif pref in tohoku:
        return "東北"
    elif pref in kanto:
        return "関東"
    elif pref in chubu:
        return "中部"
    elif pref in kansai:
        return "関西"
    elif pref in chugoku:
        return "中国"
    elif pref in shikoku:
        return "四国"
    elif kyushu:
        return "九州"


if __name__ == "__main__":
    pref = str(input("出身は？　"))

    area = pref2area(pref=pref)

    print(f"あなたの出身地は{area}地方です．")
