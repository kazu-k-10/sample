def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):

    # ここから記述
    
    first = 0
    last = len(sorted_array) - 1
    
    while first <= last:
        midindex = (first + last) // 2    #配列の真ん中のindex
        print("midindex=",midindex)
        midium = sorted_array[midindex]   # 真ん中の数を調べる
        print("midium=",midium)

        if target_number == midium:      #もし真ん中の数が目的の数と同じ場合
            print("a")
            return midium
        
        elif midium < target_number:     #もし真ん中の数が目的の数より小さい場合
            print("b")
            first = midindex + 1
            
        else:                            #もし真ん中の数が目的の数より小さい場合
            print("c")
            last = midindex -1
            
    # ここまで記述
    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()
