# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import imagedata_pb2 as imagedata__pb2


class PredictorStub(object):
  """python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. imagedata.proto

  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetPrediction = channel.unary_unary(
        '/Predictor/GetPrediction',
        request_serializer=imagedata__pb2.ImageData.SerializeToString,
        response_deserializer=imagedata__pb2.PredictionClass.FromString,
        )


class PredictorServicer(object):
  """python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. imagedata.proto

  """

  def GetPrediction(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_PredictorServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetPrediction': grpc.unary_unary_rpc_method_handler(
          servicer.GetPrediction,
          request_deserializer=imagedata__pb2.ImageData.FromString,
          response_serializer=imagedata__pb2.PredictionClass.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Predictor', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
