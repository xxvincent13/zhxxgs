import time
import sys,json
import stomp

def send_queue_out(body):
	conn = stomp.Connection10([('120.27.41.142',61613)])  
	conn.start()
	conn.connect()
	conn.send(body=body, destination='/queue/queue_out')
	conn.disconnect()

#s={"uid":"hnxzgs-performance","safe":"0","sid":"1452590031812_hnxzgs-performance","pwd":"85401632","text":{"content":"【绩效管理】你有1条新的绩效任务。"},"msgtype":"text","touser":"xzxgb","totag":"","agentid":12,"toparty":""} 
s={
   "touser": "xzxhg",
   "toparty": "",
   "totag": "",
   "msgtype": "news",
   "agentid": 0,
   "news": {
       "articles":[
           {
               "title": "CONC",
               "description": "原油指数",
               "url": "http://hqgjqhpic.eastmoney.com/EM_Futures2010PictureProducter/Index.aspx?imagetype=Kxl&id=CONC0&Formula=RSI&UnitWidth=6&type=D",
               "picurl": "http://hqgjqhpic.eastmoney.com/EM_Futures2010PictureProducter/Index.aspx?imagetype=Kxl&id=CONC0&Formula=RSI&UnitWidth=6&type=D"
           },
           {
               "title": "GLNC",
               "description": "美黄金",
               "url": "http://hqgjqhpic.eastmoney.com/EM_Futures2010PictureProducter/Index.aspx?imagetype=Kxl&id=GLNC0&Formula=RSI&UnitWidth=6&type=D",
               "picurl": "http://hqgjqhpic.eastmoney.com/EM_Futures2010PictureProducter/Index.aspx?imagetype=Kxl&id=GLNC0&Formula=RSI&UnitWidth=6&type=D"
           },
           {
               "title": "AGM",
               "description": "沪银主力",
               "url": "http://hqgnqhpic.eastmoney.com/EM_Futures2010PictureProducter/Index.aspx?ImageType=KXL&ID=agm1&EF=&Formula=RSI&UnitWidth=6&type=D",
               "picurl": "http://hqgnqhpic.eastmoney.com/EM_Futures2010PictureProducter/Index.aspx?ImageType=KXL&ID=agm1&EF=&Formula=RSI&UnitWidth=6&type=D"
           },
           {
               "title": "CUM",
               "description": "沪铜主力",
               "url": "http://hqgnqhpic.eastmoney.com/EM_Futures2010PictureProducter/Index.aspx?ImageType=KXL&ID=cum1&EF=&Formula=RSI&UnitWidth=6&type=D",
               "picurl": "http://hqgnqhpic.eastmoney.com/EM_Futures2010PictureProducter/Index.aspx?ImageType=KXL&ID=cum1&EF=&Formula=RSI&UnitWidth=6&type=D"
           } ,
           {
               "title": "DINI",
               "description": "美元指数 ",
               "url": "http://hqgjqhpic.eastmoney.com/EM_Futures2010PictureProducter/Picture/DINI0KD.png",
               "picurl": "http://hqgjqhpic.eastmoney.com/EM_Futures2010PictureProducter/Picture/DINI0KD.png"
           },
           {
               "title": "资金流入流出 ",
               "description": "资金流入流出 ",
               "url": "http://cmsjs.eastmoney.com/data/zjlximg/zjlx_ls_min.png",
               "picurl": "http://cmsjs.eastmoney.com/data/zjlximg/zjlx_ls_min.png"
           },
           {
               "title": "上证指数",
               "description": "上证指数",
               "url": "http://hqpiczs.dfcfw.com/em_quote2010pictureproducter/picture/0000011rsindex.png?r=1479824315340",
               "picurl": "http://hqpiczs.dfcfw.com/em_quote2010pictureproducter/picture/0000011rsindex.png?r=1479824315340"
           },

       ]
   }
}
data=json.dumps(s,ensure_ascii=False)
#print(data)

send_queue_out(data)
