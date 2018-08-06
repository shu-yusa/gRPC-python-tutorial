#!/bin/sh

# port 8500 for gRPC API
# port 8501 for RESTful API

saved_model=`pwd`/saved_model_twice_plus_three
model_name=twice_plus_three
docker run --rm --name tsf -p 8500:8500 -p 8501:8501 -v $saved_model:/models/$model_name -e MODEL_NAME=$model_name -t tensorflow/serving

