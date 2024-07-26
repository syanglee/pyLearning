# 创建Python 虚拟环境
> python3 -m venv ia_env
> python -m virtualenv ia_env

# 激活和使用虚拟环境(Linux)
> source ia_env/bin/activate

# 激活和使用虚拟环境(Windows)
# CMD 中可以使用 activate.bat 来激活环境变量
ia_env\Scripts\activate.bat
# Windows10 中 新发布Terminal 中需要使用 Activate.ps1 文件来激活
d:/MyCloud/MyAliCloud/Workspace/Python/myPy3L/ia_env/Scripts/Activate.ps1
.\Activate.ps1

"""
注意：
默认情况下在计算机上启动 Windows PowerShell 时，执行策略默认是 Restricted。
如果执行策略为 Restricted，系统不允许任何脚本运行。则必须将执行策略更改为 RemoteSigned 或 Unrestricted，
AllSigned 和 RemoteSigned 执行策略可防止 Windows PowerShell 运行没有数字签名的脚本。
查看计算机上的现用执行策略，打开 PowerShell 然后输入 `get-executionpolicy`
修改执行策略：以管理员身份打开PowerShell 输入 `set-executionpolicy remotesigned`
"""

pip -V
python -m pip install --upgrade pip
pip -V
# 安装paddlepaddle gpu 版本
pip install paddlepaddle-gpu -i https://mirror.baidu.com/pypi/simple
# 安装paddlepaddle cpu 版本
pip install paddlepaddle -i https://mirror.baidu.com/pypi/simple
# 安装PaddleOCR
pip install paddleocr

# 安装CV2（OpenCV），只用主模块
pip install opencv-python
pip install opencv-python -i https://pypi.tuna.tsinghua.edu.cn/simple
# 安装CV2（OpenCV），需要用主模块和contrib模块
pip install opencv-contrib-python

# 安装
pip install pillow
