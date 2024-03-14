# %引きの計算
per = int(input("値段はいくらですか?")) # %引きする値段の入力
per_closs = int(input("何%引きですか?"))# %引きする割合の入力
mult = 100 - per_closs
two = mult / 100
low = per * two
print(int(low))