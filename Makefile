
init:
	git config core.hooksPath .githooks

generate:
	rm -rf gogrpcspec/*
	docker run --rm -v ${CURDIR}:${CURDIR} -w ${CURDIR} \
	znly/protoc \
	--go_out=plugins=grpc:. \
	${CURDIR}/proto/*.proto \
	--proto_path=${CURDIR}
	mv proto/*.go gogrpcspec

	rm -rf pygrpcspec/*
	docker run --rm -v ${CURDIR}:${CURDIR} -w ${CURDIR} \
	znly/protoc \
	--plugin=protoc-gen-grpc=/usr/bin/grpc_python_plugin \
	--python_out=./pygrpcspec \
	--grpc_out=./pygrpcspec \
	${CURDIR}/proto/*.proto \
	--proto_path=${CURDIR}
	sh genpyinit.sh
	docker run --rm -v ${CURDIR}:${CURDIR} -w ${CURDIR}/pygrpcspec/proto \
	frolvlad/alpine-bash \
	bash -c "sed -i -E 's/^from proto import/from . import/g' *.py"
