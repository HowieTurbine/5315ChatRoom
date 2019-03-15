5315ChatRoom
==
##任务清单:
###Server 端:

- 处理JSON报文
- 线程池
- 管理连接
- Redis处理未读完的数据

###Clint 端

- GUI:
- 发送接收处理
- 定期发送心跳包，说明自身的存在


##通信规范
- 注册报文(C->S)

        {
           "status":(error/ok)
           "content":{
            "name":(name),
            "time":(time)
           }
            "msg":{
            "code":(status code),
            "docs":(detail msg)
        }
- 心跳报文(C<->S)

        {
           "status":(error/ok)
           "content":{
            "name":(name),
            "time":(time)
           }
            "msg":{
            "code":(status code),
            "docs":(detail msg)
        }
        
- 通信报文(S->C)

        {
          "status":(error/ok),
          "content":{
            "from":(username),
            "to":(username),
            "time":(timestamp),
            "content":(content)
           }
            "msg":{
            "code":(status code),
            "docs":(detail msg)
            }
        }
        
- Status Code

        200: OK
        201: Register msg
        202: Communication msg
        
        500: User Not Exist
        501: Internal Logic Error
        502: Data Transfor Error
        
## Test Cases

## Demo

## Contributor
- Howie Zhao: 
- Ziqi Wang:
- Zekun Zhang:
 


