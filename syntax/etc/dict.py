data = ["BTC", "BTC", "XRP", "ETH", "ETH", "ETH"]

case = set(data)


for k in set(data) :
    count = data.count(k)


    answer = (k, count)

    print(f"{answer}, count : { answer[1]}")

    