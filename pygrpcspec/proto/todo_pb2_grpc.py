# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import todo_pb2 as proto_dot_todo__pb2


class TaskManagerStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetSummary = channel.unary_unary(
        '/gogrpcspec.TaskManager/GetSummary',
        request_serializer=proto_dot_todo__pb2.Employee.SerializeToString,
        response_deserializer=proto_dot_todo__pb2.SpecificSummary.FromString,
        )
    self.AddTask = channel.unary_unary(
        '/gogrpcspec.TaskManager/AddTask',
        request_serializer=proto_dot_todo__pb2.Task.SerializeToString,
        response_deserializer=proto_dot_todo__pb2.SpecificSummary.FromString,
        )
    self.AddTasks = channel.stream_unary(
        '/gogrpcspec.TaskManager/AddTasks',
        request_serializer=proto_dot_todo__pb2.Task.SerializeToString,
        response_deserializer=proto_dot_todo__pb2.Summary.FromString,
        )
    self.GetTasks = channel.unary_stream(
        '/gogrpcspec.TaskManager/GetTasks',
        request_serializer=proto_dot_todo__pb2.Employee.SerializeToString,
        response_deserializer=proto_dot_todo__pb2.Task.FromString,
        )
    self.ChangeToDone = channel.stream_stream(
        '/gogrpcspec.TaskManager/ChangeToDone',
        request_serializer=proto_dot_todo__pb2.Task.SerializeToString,
        response_deserializer=proto_dot_todo__pb2.SpecificSummary.FromString,
        )


class TaskManagerServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetSummary(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddTask(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddTasks(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetTasks(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ChangeToDone(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_TaskManagerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetSummary': grpc.unary_unary_rpc_method_handler(
          servicer.GetSummary,
          request_deserializer=proto_dot_todo__pb2.Employee.FromString,
          response_serializer=proto_dot_todo__pb2.SpecificSummary.SerializeToString,
      ),
      'AddTask': grpc.unary_unary_rpc_method_handler(
          servicer.AddTask,
          request_deserializer=proto_dot_todo__pb2.Task.FromString,
          response_serializer=proto_dot_todo__pb2.SpecificSummary.SerializeToString,
      ),
      'AddTasks': grpc.stream_unary_rpc_method_handler(
          servicer.AddTasks,
          request_deserializer=proto_dot_todo__pb2.Task.FromString,
          response_serializer=proto_dot_todo__pb2.Summary.SerializeToString,
      ),
      'GetTasks': grpc.unary_stream_rpc_method_handler(
          servicer.GetTasks,
          request_deserializer=proto_dot_todo__pb2.Employee.FromString,
          response_serializer=proto_dot_todo__pb2.Task.SerializeToString,
      ),
      'ChangeToDone': grpc.stream_stream_rpc_method_handler(
          servicer.ChangeToDone,
          request_deserializer=proto_dot_todo__pb2.Task.FromString,
          response_serializer=proto_dot_todo__pb2.SpecificSummary.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'gogrpcspec.TaskManager', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
