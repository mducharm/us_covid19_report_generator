from flask import Flask, make_response, render_template
import io
import csv


app = Flask(__name__)

import grpc
import report_pb2
import report_pb2_grpc
from google.protobuf.json_format import MessageToDict

def obj_to_dict(obj):
    return obj.__dict__

@app.route("/")
def index():
    try:
        data = get_covid_data_by_state()
        return render_template("index.html", data=data)

    except Exception as e:
        return e

@app.route("/download")
def download():

    try:
        data = get_covid_data_by_state()
        csv_data = covid_data_as_csv(data)
        si = io.StringIO()
        csv_writer = csv.writer(si)
        csv_writer.writerows(csv_data)
        output = make_response(si.getvalue())
        output.headers["Content-Disposition"] = "attachment; filename=us_covid_data.csv"
        output.headers["Content-type"] = "text/csv"
        return output

    except Exception as e:
        return e

def get_covid_data_by_state():
    try:
        channel = grpc.insecure_channel('localhost:3000')
        stub = report_pb2_grpc.ReportStub(channel)
        reportRequest = report_pb2.ReportRequest()
        reportResponse = stub.GetCovidDataForAllStates(reportRequest)

        return [MessageToDict(r) for r in reportResponse]

    except Exception as e:
        return e

def covid_data_as_csv(state_data_as_dicts):
    headers = state_data_as_dicts[0].keys()
    data = [s.values() for s in state_data_as_dicts]
    data.insert(0, headers)

    return data

if __name__ == '__main__':
    app.run()