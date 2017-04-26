# coding: utf-8

def fcookie(raw_cookie):
    result = {}
    fcookie = ''.join(raw_cookie.split(' ')).split(';')
    for item in fcookie:
        cookie = item.split('=')
        result[cookie[0]] = cookie[1]
    return result
