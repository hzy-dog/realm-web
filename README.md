# Realm Web

该项目提供了一个网络界面，用于管理游戏流量的端口转发和其他网络配置。它支持 TCP 和 UDP 流量、TLS 配置，并包含登录保护机制。

## 特性

- **TCP/UDP 流量端口转发**
- **TLS 配置**
- **认证和登录保护**
- **支持 Docker 镜像**
- **带有 Web 界面的简单部署**

## 前提条件

要运行该项目，你需要：

- 一个 Linux 系统（推荐使用 x86 架构）
- Docker（可选，推荐使用 Docker 进行部署）
- Node.js（如果你选择手动部署）

## 安装

你可以通过以下两种方式安装和部署该项目：

### 方法 1：**使用 Docker 部署**

1. **安装 Docker**：如果没有安装 Docker，请按照 [官方 Docker 安装指南](https://docs.docker.com/get-docker/) 进行安装。
   
2. **克隆该仓库**：
   ```bash
   git clone https://github.com/hzy-dog/realm-web.git
   cd realm-web
构建并运行 Docker 容器：

bash
复制
编辑
docker build -t realm-web .
docker run -d -p 7655:7655 realm-web
访问 Web 界面：打开浏览器，访问 http://localhost:7655，开始配置端口转发。

方法 2：手动部署（快速部署）
克隆该仓库：

bash
复制
编辑
git clone https://github.com/hzy-dog/realm-web.git
cd realm-web
安装依赖：

确保你已安装 Node.js。如果没有安装，请参考 Node.js 安装指南。

安装所需的依赖：

bash
复制
编辑
npm install
启动 Web 服务器：

bash
复制
编辑
npm start
访问 Web 界面：打开浏览器，访问 http://localhost:7655，开始配置端口转发。

配置
1. 端口
Web 界面默认运行在 7655 端口。

2. TLS 配置
你可以在 config 文件中配置 TLS（SSL），通过提供证书和私钥的路径来启用加密通信。

3. 登录认证
在 config 文件中设置用户名和密码，以启用登录保护。

许可证
该项目采用 MIT 许可证，详细内容请参阅 LICENSE 文件。
