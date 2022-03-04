.PHONY: build

build:
	trunk build --release && \
	mv dist/index*_bg.wasm dist/index_bg.wasm && \
	mv dist/index*.js dist/index.js && \
	sed -r -i 's/index-[a-z0-9]+\_bg.wasm/index_bg.wasm/g' dist/index.html && \
	sed -r -i 's/index-[a-z0-9]+\.js/index.js/g' dist/index.html \


serve: 
	python serve.py