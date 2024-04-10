# wordcloud
简易的python生成词云工具

### 使用方法

1. **创建虚拟环境**：
   在项目根目录下，打开命令行，并执行以下命令来创建一个虚拟环境：
   ```
   python -m venv .venv
   ```
   这将会在项目根目录下创建一个名为`.venv`的新虚拟环境。

1. **激活虚拟环境**：
   接着，在命令行中使用以下命令来激活虚拟环境：
   - 在 macOS/Linux 系统中：
     ```
     source .venv/bin/activate
     ```
   - 在 Windows 系统中：
     ```
     .venv\Scripts\activate
     ```

1. **安装项目依赖**：
   在虚拟环境激活状态下，运行以下命令来安装项目所需的依赖：
   ```
   pip install -r requirements.txt
   ```
   这将会根据`requirements.txt`文件中指定的依赖，安装相应的包。

1. **准备数据**
   把需要生成词云的文本内容以txt文件格式存放到input文件夹下（注意保留.txt扩展名）

1. **运行项目**：
   准备好需要生成词云的文本数据后，执行下方命令运行，将对input中每个数据文件生成一个词云图
   ```shell
   python main.py
   ```

1. **获取词云图**：
   当你完成项目的运行后，可以在output目录下获取词云图片：

### 修订停用词

停用词存放在项目的`stop_words.txt`文件中，多个停用词使用空格分隔，可以自行调节