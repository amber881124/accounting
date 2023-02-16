import os

products = [] 

if os.path.isfile('accounting.csv'):
    print('檔案存在')
    with open('accounting.csv', 'r', encoding = 'utf-8') as f:
        for line in f:
            name, price = line.strip().split(',')
            products.append([name,price])

with open('accounting.csv', 'w', encoding = 'utf-8') as f:
    while True:
        name = input('請輸入商品名稱： ')
        if  name == 'q':
            print('停止輸入')
            break 
        price = input('請輸入商品價格： ')
        price = int(price)
        products.append([name, price])
    print(products)
    for name, price in products:
        f.write(f'{name},{price}\n')
