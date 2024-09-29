# rust-learn
## 環境構築
- Dockerを使う
```
$ cd rust-learn

# イメージビルド
$ docker image build -t rust:learn .

# コンテナ起動
# マウントするディレクトリ（source=.のところ）は動作させたいプロジェクトによって変える
$ docker container run --rm -it --mount type=bind,source=.,target=/root/workspace rust:learn bash
```
