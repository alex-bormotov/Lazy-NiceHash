# Lazy-NiceHash


> This bot does auto exchange BTC (that was mined) to XRP on NiceHash exchange once a day then sends a notification to Discord.


---

### Install on Ubuntu (Docker)

```bash
sudo apt-get update
```

```bash
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common
```

```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```

```bash
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
```

```bash
sudo apt-get update
```

```bash
sudo apt-get install docker.io git
```

```bash
git clone https://github.com/alex-bormotov/lazy-nicehash
```

```bash
cd lazy-nicehash
```

```bash
cp config.json.sample config.json
```

> edit config.json

```bash
sudo docker build -t lazy-nicehash .
```

```bash
sudo docker run lazy-nicehash &
```

### Update

```bash
cd lazy-nicehash
```

```bash
sudo docker ps
```

```bash
sudo docker stop CONTAINER ID
```

```bash
sudo docker rm CONTAINER ID
```

```bash
sudo docker rmi lazy-nicehash
```

```bash
git pull origin master
```

```bash
sudo docker build -t lazy-nicehash .
```

```bash
sudo docker run lazy-nicehash &
```

