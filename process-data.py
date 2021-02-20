import re
from datetime import datetime

file = open('data.txt', 'r')
inp = file.read().splitlines()
inp = [x for x in inp if x != '']
file.close()


def clean_str(string):
    string = re.sub('<.*?>', '  ', string)
    string = re.sub(' &amp; ', ' & ', string)
    string = re.sub('\s{2,}', ';', string)
    string = re.sub(';+', '|', string)
    string = re.sub('^,', '', string)
    string = re.sub('Order Number,', '', string)
    string = re.sub('Total Amount,', '', string)
    string = re.sub('Items,', '', string)
    string = re.sub('Ordered on,', '', string)
    return string


class Order:
    CSV_HEADING = f'restaurant' \
        + f',location' \
        + f',city' \
        + f',delivered' \
        + f',order_no' \
        + f',amount' \
        + f',items' \
        + f',datetime'

    def __init__(self, str_inp):
        x = str_inp.split('|')[1:]
        self.restaurant = x[0]
        self.location = x[1].split(',')[0].strip()
        self.city = x[1].split(',')[-1].strip()
        self.delivered = x[2] == 'Delivered'
        self.order_no = x[4]
        self.amount = float(x[6][1:].replace(',', ''))
        self.items = x[8].strip().replace(',', ' +')
        self.order_datetime = datetime.strptime(
            x[10].replace(' at ', ' '), '%B %d, %Y %H:%M %p')

    def get_csv(self) -> str:
        return f'{self.restaurant}' \
            + f',{self.location}' \
            + f',{self.city}' \
            + f',{self.delivered}' \
            + f',{self.order_no}' \
            + f',{self.amount}' \
            + f',{self.items}' \
            + f',{self.order_datetime}'


p = [Order.CSV_HEADING]
for i in inp:
    x = Order(clean_str(i)).get_csv()
    p.append(x)

file = open('data.csv', 'w')
file.write("\n".join(p))
file.close()
