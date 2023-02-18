import os

# 讀取檔案
def read_file(filename):
    products = [] 
    with open(filename, 'r', encoding = 'utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue
            name, price = line.strip().split(',')
            products.append([name,price])
    return products

# 讓使用者輸入
def user_input(products):
    while True:
        name = input('請輸入商品名稱： ')
        if  name == 'q':
            print('停止輸入')
            break 
        price = input('請輸入商品價格： ')
        price = int(price)
        products.append([name, price])
    print(products)
    return products

# 印出所有購買紀錄
def print_procucts(products):
    for name, price in products:
        print(f'{name}的價格為{price}')

#寫入檔案
def write_file(filename, products):
    with open('accounting.csv', 'w', encoding = 'utf-8') as f:
        f.write('商品,價格\n')
        for name, price in products:
            f.write(f'{name},{price}\n')

# 執行function
def main():
    filename = 'accounting.csv'
    # 檢查檔案在不在，之所以不用寫成func，是因為他很短，且只用一次
    if os.path.isfile(filename):
        print('檔案存在')
        products = read_file(filename) # prcducts是用來接return出來的東西(讀取已存在檔案內的products)
    else:
        print('檔案不存在')
    products = user_input(products) # prcducts是用來接return出來的東西(已加入新products)
    print_procucts(products)
    write_file(filename, products)

main()