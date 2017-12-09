# hntworks

## これは何？

elgoogのコンテナ環境構築ファイル一式

## インストール方法

* cleanなubuntu-16.04を用意
* 初期セットアップを実施(docker,python3インストールなど)
```
$ wget https://github.com/k-shino/hntworks/raw/master/init.sh
$ chmod +x init.sh
$ ./init.sh
```
* ubuntu再起動
* このレポジトリをclone
```
$ git clone https://github.com/k-shino/hntworks
```
* docker-composeでbuild&起動
```
$ cd hntworks/
$ docker-compose build
$ docker-compose up -d
```
