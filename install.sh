#!/bin/bash

echo "选择安装方式："
echo "1) 快速安装（本地 Node 环境）"
echo "2) Docker 安装（推荐）"
read -p "请输入选项 [1 或 2]: " choice

if [ "$choice" == "1" ]; then
  echo "正在进行快速安装..."
  sudo apt update
  sudo apt install -y nodejs npm git
  git clone https://github.com/hzy-dog/realm-web.git
  cd realm-web
  cd backend
  npm install
  nohup node index.js &
  echo "已启动后台服务，默认监听 7655 端口"

elif [ "$choice" == "2" ]; then
  echo "正在进行 Docker 安装..."
  sudo apt update
  sudo apt install -y docker.io git
  git clone https://github.com/hzy-dog/realm-web.git
  cd realm-web
  docker build -t realm-web .
  docker run -d -p 7655:7655 --name realm-web realm-web
  echo "Docker 部署完成，已在 7655 端口运行"

else
  echo "无效选项，请重新运行脚本并选择 1 或 2"
fi
