# cp generated/py/grpcspec/*.py pybrijgrpc/
cat <<EOF >pygrpcspec/__init__.py
from . import proto
__all__ = [
	'proto'
]
EOF
cat <<EOF >pygrpcspec/proto/__init__.py
from . import todo_pb2_grpc
from . import todo_pb2
__all__ = [
	'todo_pb2_grpc',
	'todo_pb2'
]
EOF