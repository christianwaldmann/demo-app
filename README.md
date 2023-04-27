# demo-app

Demo application that returns the string _"demo-app is working"_ on GET-requests to the endpoint _/_.

### Build docker image

```zsh
docker build -t demo-app:latest .
```

### Run docker image

```zsh
docker run -p 8000:80 demo-app:latest
```

[localhost:8000](http://localhost:8000/) should now return _"demo-app is working"_.
