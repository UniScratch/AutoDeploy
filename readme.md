一个用于自动化部署预览站的小工具  
## 安装
```
pip3 install -r requirements.txt
```
## 配置  
修改`config.py.example`文件并删除`.example`后缀  
修改 GitHub WebHook 配置  
| item | value |  
|-     |-      |
| Payload URL | http://ip:11460/webhook |
| Content type | application/json |
| Secret | 与`config.py`内`SECRET`一致 |
| Which events would you like to trigger this webhook? | Just the push event. |


## 启动
```bash
python3 app.py
```
