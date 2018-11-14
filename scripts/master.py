import os
import random
l=os.listdir('../tool/patches')

List=[]
for patch in l:
    if patch.startswith('PatchSimGen'):
        List.append(patch)
#print(List)
random.shuffle(List)

from http.server import HTTPServer, BaseHTTPRequestHandler 
import threading

i=0
mutex = threading.Lock()
class TestHTTPHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        global i
        global List
        self.protocal_version = 'HTTP/1.1' 
        self.send_response(200) 
        self.send_header("Welcome", "Contect") 
        self.end_headers()
        mutex.acquire()
        if i==len(List):
            res='-1'
        else:
            res=str(List[i])
            i+=1
        mutex.release()
        self.wfile.write(res.encode(encoding="utf-8"))
def start_server(port):
        http_server = HTTPServer(('', int(port)), TestHTTPHandler)
        http_server.serve_forever() 

start_server(8000)
