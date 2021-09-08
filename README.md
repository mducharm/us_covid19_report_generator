

```bash
# for Go:

protoc --go_out=plugins=grpc:. .\report.proto
```

```bash
# for Python:
```

```
protoc --go_out=. --go_opt=paths=source_relative --go-grpc_out=. --go-grpc_opt=paths=source_relative .\helloworld\helloworld.proto 


protoc --go_out=. --go_opt=paths=source_relative --grpc_python_out=. --grpc_python_out=paths=source_relative .\shared\covid19.proto 
```
```