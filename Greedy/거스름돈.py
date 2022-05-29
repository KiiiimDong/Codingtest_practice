# 거스름돈
n = 1460
answer = 0

coin_list = [500, 100, 50, 10]
for coin in coin_list:
    answer += n // coin # 500원 부터 10원까지  하나씩 몇번 지불할 수 있는지 세기.
    n %= coin # 지불하고 남은금액(나머지) n에 할당.
print(answer)
