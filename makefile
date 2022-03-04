.PHONY: build

build:
	trunk build && sed -r -i 's/<!--|-->//g' dist/index.html   

serve: 
	python serve.py