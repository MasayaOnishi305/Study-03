import pandas as pd
import eel

### デスクトップアプリ作成課題
def kimetsu_search(word,csv_file,add_flg):
    # 検索対象取得
    df=pd.read_csv(f"./{csv_file}.csv")
    source=list(df["name"])

    # 検索
    if word in source:
        answer = f"『{word}』はあります"
    
    else:
        answer = f"『{word}』はありません"      
        # 追加
        #add_flg=input("追加登録しますか？(0:しない 1:する)　＞＞　")
        if add_flg=="1":
            source.append(word)
            print(f"{source}.csvに{word}を追加登録します")
            # CSV書き込み
            df=pd.DataFrame(source,columns=["name"])
            df.to_csv(f"./{csv_file}.csv",encoding="utf_8-sig")
            answer = f"{answer}\r\n{source}"

    print(answer)
    return(answer)

