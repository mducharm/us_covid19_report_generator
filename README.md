## US COVID-19 Report Generation

Provides US COVID-19 data as a CSV. Uses a Go gRPC server with Python Flask client.

Powered by [Disease.sh](https://disease.sh/), which aggregates COVID-19 data from various worldometers.

Completed as a part of Waystar Day (September 2021).

### Running Locally

```bash
# server
go run .\server\main.go

# client
python app.py
```


### Generating gRPC code from report.proto

```bash
# for Go:

protoc --go_out=plugins=grpc:. .\report.proto
```

```bash
# for Python:
python -m grpc_tools.protoc -I . --python_out=client --grpc_python_out=client .\report.proto
```
