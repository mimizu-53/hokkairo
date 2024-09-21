import http.server
import ssl

# ホスト名とポートの設定
server_address = ('192.168.1.10', 8080)

# HTTPサーバーの作成
httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)

# SSLコンテキストの設定
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile='./server.pem')

# ソケットをSSLでラップする
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

print("Serving on localhost")
httpd.serve_forever()
