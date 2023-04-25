import requests,json,flask,configparser
server = flask.Flask(__name__)

con = configparser.ConfigParser()
con.read('config.ini', encoding='utf-8')


@server.route('/api/dingding', methods=['post'])

def dingding_hook():
    dingding = con.get('dingding','open_dingding')
    if dingding == '1':
        data = flask.request.get_json()
        dingding_url = con.get('dingding', 'dingding_url')
        print(dingding_url)
        headers = {"Content-Type": "application/json; charset=utf-8"}
        data = {
            "msgtype": "text",
            "text": {
                "content": "deploy：分支"+data['branch']+"正在构建部署，请前往jenkins查看：http://192.168.0.40:8080"
            }
        }
        res = requests.post(dingding_url, headers=headers, json=data)
        print(res)
    else:
        print(dingding)
    return json.dumps({"data":"OK"})
if __name__ == '__main__':
    server.run(
        host='0.0.0.0',
        port=8080,
    )