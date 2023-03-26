def sort_data(data):
    """Сортировка словарей по дате"""
    items = []
    for item in data:
        if item.get('state') == 'EXECUTED':
            items.append(item)
    items.sort(key = lambda x: x.get('date'), reverse = True)
    return items
def format(item):
    '''Форматирование входящих данных'''
    str_date = date(item.get('date'))
    from_= hide(item.get('from'))
    to_ = hide(item.get('to'))
    description = item.get('description')
    amount = item.get('operationAmount').get('amount')
    currency = item.get('operationAmount').get('currency').get('name')
    if from_:
        from_ = from_ + ' -> '
    return f'{str_date} {description}\n{from_}{to_}\n{amount} {currency}'
def date(str_date):
    '''Форматирование даты в требуемый вид'''
    date = str_date[:10].split('-')
    return date[2] +'.'+ date[1]+'.'+date[0]
def hide(card):
    '''Скрытие номера карты и счета'''
    if not card:
        return ''
    card_data = card.split(' ')
    if card_data[0] == 'Счет':
        return card_data[0] + ' **' + card_data[1][-4:]
    card_number = card_data[-1][:4] + ' ' + card_data[-1][4:6] + '** **** ' + card_data[-1][-4:]
    return ' '.join(card_data[:-1]) + ' ' + card_number