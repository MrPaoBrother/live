# 基于hls的直播技术

## 环境
* win10
* vscode
* cmder
* python2.7
## 安装
* [安装flask](https://flask.palletsprojects.com/en/1.0.x/installation/?highlight=install)

```
$ pip install flask
```

## 运行
* 运行主要分为两部分
    * m3u8文件定时刷新脚本
    * 基于hls的播放服务
* 运行refresh_m3u8.py

```
$ python refresh_m3u8.py
```
* 运行server.py

```
$ python server.py
```

## demo展示
![image](live_hls/static/images/hls_demo.png)

## 参考
[1] [hls协议官网文档](https://developer.apple.com/streaming/)

[2] [ffmpeg使用手册](https://ffmpeg.org/ffmpeg-formats.html)

[3] [hls.js使用手册](https://video-dev.github.io/hls.js/stable/)