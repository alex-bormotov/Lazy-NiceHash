# lazy-nicehash


> This bot does auto exchange BTC to XRP on NiceHash exchange once a day then sends a notification to Discord.


---

### Install on Ubuntu (Docker)

> sudo apt-get update

> sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common

> curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

> sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"

> sudo apt-get update

> sudo apt-get install docker.io git

> git clone https://github.com/alex-bormotov/

> cd lazy-nicehash

> cp config.json.sample config.json, and edit config.json

> sudo docker build -t lazy-nicehash .

> sudo docker lazy-nicehash axe-bot &
