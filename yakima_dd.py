# coding = utf-8

import requests, time

def call(method, options={}, **kwargs):
    '''Фукнция вызова api ВК.'''
    options['access_token'] = token
    options['v'] = '5.81'
    options.update(kwargs)
    resp = requests.get('https://api.vk.com/method/'+method, params=options).json()
    if 'error' in resp:
        print('VKERROR: {error_code}: {error_msg}'.format(**resp['error']))
    return resp
def send_message(peer_id, textmessage='',photovar=''):
    '''Функция отправки сообщений.'''
    options = {
        'message' : textmessage,
        'peer_id' : peer_id,
    }
    if photovar != '':
        options['attachment'] = 'photo' + photovar
    call('messages.send', options)
    print('Отправлен {message} и {photo} к {peer_id}'.format(message = textmessage, photo = photovar, peer_id = peer_id))
def main(peer_id, timer, photo):
    file = open('dialog.txt', encoding='utf-8', newline='')
    timer = int(timer)
    while True:
        for line in file:
            time.sleep(timer)
            send_message(peer_id, line, photo)


if __name__ == '__main__':
    token = "123" #тут ваш токен вк
    i = int(input('Введите айди беседы, взять его можно из im?peers=c(айди без букв сука) ')) #пример 1
    peer_id = i + 2000000000
    timer = input('Введите задержку при постинге в секундах (минимальная задержка 5 секунд): ')
    photo = ('551462653_457244347')
    main(peer_id, timer, photo)