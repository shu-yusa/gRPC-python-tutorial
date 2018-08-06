import grpc
import tensorflow as tf

from tensorflow.core.framework import types_pb2
from tensorflow_serving.apis import predict_pb2
from tensorflow_serving.apis import prediction_service_pb2

tf.app.flags.DEFINE_string('server', 'localhost:8500', 'PredictionService host:port')
FLAGS = tf.app.flags.FLAGS


def main():
    channel = grpc.insecure_channel(FLAGS.server)
    stub = prediction_service_pb2.PredictionServiceStub(channel)
    request = predict_pb2.PredictRequest()
    request.model_spec.name = 'twice_plus_three'
    # request.model_spec.signature_name = 'serving_default'

    request.inputs['x'].dtype = types_pb2.DT_FLOAT
    request.inputs['x'].float_val.append(2.0)

    result_future = stub.Predict.future(request, 5.0)
    result = result_future.result()
    print(result)

if __name__ == '__main__':
    main()
