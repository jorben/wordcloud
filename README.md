# wordcloud
简易的python生成词云工具

### 使用方法

1. 创建虚拟环境：
在项目根目录下，打开命令行，并执行以下命令来创建一个虚拟环境：

```shell
python -m venv .venv
```


2. 激活虚拟环境：
接着，在命令行中使用以下命令来激活虚拟环境：

- 在 macOS/Linux 系统中：
```shell
source .venv/bin/activate
```

- 在 Windows 系统中：
```shell
.venv\Scripts\activate
```

3. 安装项目依赖：
在虚拟环境激活状态下，运行以下命令来安装项目所需的依赖：
```shell
pip install -r requirements.txt
```

这将会根据requirements.txt文件中指定的依赖，安装相应的包。

4. 把需要生成词云的内容使用txt格式放到input文件夹下（注意保留.txt扩展名）


5. 运行项目：
```shell
python main.py
```
