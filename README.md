# Realm Web 面板

一个基于 Web 的可视化管理面板，专为 [zhboner/realm](https://github.com/zhboner/realm) 端口转发工具设计，支持 TCP / UDP 转发规则的可视化配置、TLS 设置、认证登录管理，适合用于游戏流量中转、内网穿透等场景。

## ✨ 项目特性

- 🌐 Web 浏览器图形界面
- 📦 支持 TCP / UDP 中转配置
- 🔐 支持 TLS 开关与证书路径配置
- 👤 登录认证保护（支持用户名密码修改）
- 📁 可视化添加 / 修改 / 删除转发规则
- 🐳 支持 Docker 镜像部署
- 📌 后端基于 JSON 文件存储配置（无需数据库）

---

## 🚀 一键安装方式

你可以使用以下命令在 Linux 服务器上快速安装该面板：

```bash
bash <(curl -sL https://raw.githubusercontent.com/hzy-dog/realm-web/main/install.sh)
```

脚本将提示你选择安装方式：

- `1`: 快速安装（Node.js 环境部署，适合本地或开发）
- `2`: Docker 安装（推荐，隔离、轻量）

---

## 📦 Docker 手动部署方式

若你熟悉 Docker，也可以手动构建和运行：

```bash
git clone https://github.com/hzy-dog/realm-web.git
cd realm-web
docker build -t realm-web .
docker run -d -p 7655:7655 realm-web
```

---

## 📂 项目结构说明

```
realm-web/
├── backend/               # 后端接口服务 (Express)
│   ├── routes/            # 路由：规则配置、认证管理
│   └── config.json        # 转发规则与用户认证存储文件
├── frontend/              # 前端界面 (Vue 或 React)
│   └── ...
├── install.sh             # 一键安装脚本
├── Dockerfile             # Docker 镜像构建文件
└── README.md              # 本文档
```

---

## 🛡 默认访问

- 面板地址: [http://localhost:7655](http://localhost:7655)
- 默认登录用户/密码：
  - 用户名: `admin`
  - 密码: `admin`

进入后可在面板中更改登录认证信息、证书路径及规则配置。

---

## 📘 相关项目

- 🔗 [zhboner/realm](https://github.com/zhboner/realm)：高性能端口转发工具，本面板为其提供前端管理支持。

---

## 📄 License

MIT License. 本项目仅用于学习与研究用途，请勿用于非法用途。
