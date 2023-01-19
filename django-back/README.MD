# django-back


## 1. 后端部分运行

### 1.1 第一次部署
进入项目目录 
```bash
cd django-back
```

创建虚拟环境
```bash
python -m venv env
```

进入/激活 当前虚拟环境
```bash
env\scripts\activate # windows
source ./env/bin/activate # macos and linux
```

根据依赖列表安装
```bash
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```


### 1.2 运行项目

进入/激活 当前虚拟环境
```bash
env\scripts\activate # windows
source ./env/bin/activate # macos and linux
```

运行项目，并绑定到 8000端口（前端跨域代理也要绑定对应的端口）
```bash
python manage.py runserver 127.0.0.1:8000
```
