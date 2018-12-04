version := v0.0.1
dev:
	docker build -t flaskresty:$(version)-dev -f Dockerfile .
run:
	docker run -p 5000:5000 -v `pwd`:/app flaskresty:$(version)-dev uwsgi '/app/uwsgi/dev.ini'