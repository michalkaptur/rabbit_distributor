## setup

```sh
docker run -itd --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
virtualenv vnev
source venv/bin/activate
pip3 install -r requirements.txt
```

## run
```sh
./worker.py & ./worker.py & ./worker.py &
./rabbit_distr.py
kill $(jobs -p)
```