#!/bin/bash

echo "Realm Web 安装脚本"
echo "请选择安装方式："
echo "1. 快速安装（Node.js 环境）"
echo "2. Docker 安装"
read -p "请输入 1 或 2 进行选择: " choice

if [ "$choice" == "1" ]; then
    echo "开始快速安装..."
    sudo apt update
    sudo apt install -y nodejs npm git

    git clone https://github.com/hzy-dog/realm-web.git
    cd realm-web || exit

    npm install
    npm start &

    echo "安装完成，访问地址：http://localhost:7655"

elif [ "$choice" == "2" ]; then
    echo "开始 Docker 安装..."

    if ! command -v docker &>/dev/null; then
        echo "未检测到 Docker，正在安装..."
        sudo apt update
        sudo apt install -y docker.io
        sudo systemctl enable docker
        sudo systemctl start docker
    fi

    git clone https://github.com/hzy-dog/realm-web.git
    cd realm-web || exit

    docker build -t realm-web .
    docker run -d -p 7655:7655 realm-web

    echo "安装完成，访问地址：http://localhost:7655"

else
    echo "输入无效，请输入 1 或 2"
    exit 1
fi
