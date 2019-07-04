cat <<EOF >pygrpcspec/__init__.py
from . import proto
__all__ = [
	'proto'
]
EOF
pyfiles=($(ls pygrpcspec/proto | sed -e 's/\..*$//'| grep -v __init__))
rm -f pygrpcspec/proto/__init__.py
for i in "${pyfiles[@]}"
do
	echo "from . import $i" >> pygrpcspec/proto/__init__.py
done

echo "__all__ = [" >> pygrpcspec/proto/__init__.py
for i in "${pyfiles[@]}"
do
	echo "    '$i'," >> pygrpcspec/proto/__init__.py
done
echo "]" >> pygrpcspec/proto/__init__.py
