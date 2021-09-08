from flask import Flask

app = Flask(__name__)

import grpc
import report_pb2
import report_pb2_grpc

def obj_to_dict(obj):
    return obj.__dict__

@app.route("/")
def hello_world():
    print("start service")

    try:
        channel = grpc.insecure_channel('localhost:3000')
        stub = report_pb2_grpc.ReportStub(channel)
        reportRequest = report_pb2.ReportRequest()
        reportResponse = stub.GetCovidDataForAllStates(reportRequest)

        for stateData in reportResponse:
            print(stateData)

        return str(reportResponse)

    except Exception as e:
        print(e)
        return e

    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    app.run()