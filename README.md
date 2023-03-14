<h1 align="center">nonebot-plugin-unoconv 🔧</h1></br>

<p align="center">基于unoconv的文件转换插件</p></br>


## 安装
### 方法一 使用nb-cli
```
nb plugin install nonebot_plugin_unoconv
```

### 方法二 使用pip
```
# pip 下载包
pip install nonebot_plugin_unoconv


# 配置 pyproject.toml

plugins = [
    ...,
    "nonebot_plugin_unoconv",
    ]

```

## 使用方法
**支持私聊与群聊**  
**下载与转换的文件在操作成功后会删除**
### 步骤
1. `文件转换` +  `要转换的类型`  
2. 发送文件  


| ![image](https://github.com/Zeta-qixi/nonebot-plugin-unoconv/blob/master/image/demo1.png) | ![image](https://github.com/Zeta-qixi/nonebot-plugin-unoconv/blob/master/image/demo2.jpg) |
|:--:|:--:|


## 类型支持
目前插件支持的  
输入:  `docx`, `doc`, `odt`  
输出:  `pdf`, `html`, `doc`  

其他查看 http://dag.wiee.rs/home-made/unoconv/   
需要其他格式可以尝试:
`强制文件转换` +  `要转换的类型`  


## 其他
⚠️ 目前只支持linux服务器 (没有win..)