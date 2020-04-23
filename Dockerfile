FROM python:latest
RUN pip3 install RPi.bme280 -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip3 install requests -i https://pypi.tuna.tsinghua.edu.cn/simple