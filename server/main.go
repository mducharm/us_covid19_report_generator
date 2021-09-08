package main

import (
	"encoding/json"
	"io/ioutil"
	"log"
	"net"
	"net/http"

	pb "us_covid19_report/server/report"

	"google.golang.org/grpc"
)

const (
	port = ":3000"
	url  = "https://disease.sh/v3/covid-19/states"
)

type server struct {
	pb.UnimplementedReportServer
}

func (s *server) GetCovidDataForAllStates(req *pb.ReportRequest, stream pb.Report_GetCovidDataForAllStatesServer) error {

	var stateData []*pb.StateCovidData

	resp, err := http.Get(url)
	if err != nil {
		return err
	}

	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		return err
	}

	if err := json.Unmarshal(body, &stateData); err != nil {
		return err
	}

	for _, data := range stateData {
		if err := stream.Send(data); err != nil {
			return err
		}
	}

	return nil
}

func main() {
	lis, err := net.Listen("tcp", port)
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	log.Printf("listening...")
	s := grpc.NewServer()
	pb.RegisterReportServer(s, &server{})
	if err := s.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}
