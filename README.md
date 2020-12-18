## setup

```sh
docker run -itd --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
virtualenv vnev
source venv/bin/activate
pip3 install -r requirements.txt
```

## run
```sh
./client.py & ./client.py & ./client.py &
./__init__.py
kill $(jobs -p)
```