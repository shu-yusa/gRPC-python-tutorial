# Tutorial for gRPC with python

## Setup

```bash
virtualenv env
source env/bin/activate
pip install protobuf
```

## Compile protocol buffers

```bash
protoc [-I=.] --python_out=. ./addressbook.proto
```
This will generates `addressbook_pb2.py`.

## Write and read address book

To write,
```bash
python write_message.py `addressbook`
```

To read,
```bash
python read_message.py `addressbook`
```


## Reference
* https://grpc.io/docs/tutorials/basic/python.html
