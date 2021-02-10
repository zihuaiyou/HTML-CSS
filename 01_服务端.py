import socket

server = socket.socket()
server.bind(('127.0.0.1', 8080))
server.listen(5)
"""
b'GET / HTTP/1.1\r\n 请求首行
Host: 127.0.0.1:8080\r\n 请求头
Connection: keep-alive\r\n
Upgrade-Insecure-Requests: 1\r\n
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.56\r\n
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n
Sec-Fetch-Site: none\r\n
Sec-Fetch-Mode: navigate\r\n
Sec-Fetch-User: ?1\r\n
Sec-Fetch-Dest: document\r\n
Accept-Encoding: gzip, deflate, br\r\n
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6\r\n
\r\n
请求体
'"""

while True:
    conn, addr = server.accept()
    data = conn.recv(1024)
    print(data)
    # 构造出符合HTTP协议底层的数据
    conn.send(b'HTTP/1.1 200 0k\r\n\r\n')
    # conn.send(b'<h1>hello baby</h1>')
    with open('a.txt', 'rb') as f:
        conn.send(f.read())
    conn.close()


