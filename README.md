

####  [Vue官网](https://vuejs.org/)

#### 终端

Linux和Mac上可以用自带的终端。
Windows上推荐用powershell或者cmd。Git Bash有些指令不兼容。

#### 安装Nodejs

[安装地址](https://nodejs.org/en/)

#### 安装@vue/cli

打开Git Bash，执行：

```
npm i -g @vue/cli
```


如果执行后面的操作有bug，可能是最新版有问题，可以尝试安装早期版本，比如：npm i -g @vue/cli@4

#### 启动vue自带的图形化项目管理界面

```
vue ui
```

常见问题1：Windows上运行vue，提示无法加载文件，表示用户权限不足。
解决方案：用管理员身份打开终端，输入set-ExecutionPolicy RemoteSigned，然后输入y

#### Vue所需依赖

- @popperjs/core
- bootstrap
- jquery

#### Vue所需插件

- router
- vuex