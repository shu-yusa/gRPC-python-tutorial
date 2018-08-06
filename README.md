# TensorFlow Serving

## Setup

```bash
virtualenv env
source env/bin/activate
pip install tensorflow-serving-api
```

## Export model
To export, run
```bash
python twice_plus_three.py `version`
```

To check SavedModel, run
```bash
saved_model_cli show --dir ./saved_model_twice_plus_three/`version` --all
```

## Run TensorFlow Serving API
```bash
docker run --rm --name tsf -p 8500:8500 -p 8501:8501 -v ./saved_model_twice_plus_three:/models/twice_plus_three -e MODEL_NAME=twice_plus_three -t tensorflow/serving
```

## Call predict API
To call RESTful API from command line, run
```bash
curl -d '{"instances": [1.0, 2.0, 5.0]}' -X POST http://localhost:8501/v1/models/twice_plus_three:predict
```

To call gRPC API, run
```bash
python twice_plus_three_client.py
```

## References
* https://www.tensorflow.org/serving/docker
* https://grpc.io/docs/quickstart/python.html
* http://nlp-tech-blog.hatenablog.com/entry/2018/02/19/172104
