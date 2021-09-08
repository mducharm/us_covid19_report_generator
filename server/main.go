package main

import (
	"context"
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

type StateCovidData struct {
	state               string // "California",
	updated             uint   // 1631115135558,
	cases               uint   // 4442304,
	todayCases          uint   // 0,
	deaths              uint   // 66587,
	todayDeaths         uint   // 0,
	recovered           uint   // 2323894,
	active              uint   // 2051823,
	casesPerOneMillion  uint   // 112429,
	deathsPerOneMillion uint   // 1685,
	tests               uint   // 84736996,
	testsPerOneMillion  uint   // 2144577,
	population          uint   // 39512223
}

func (s *server) GetReportAsCSV(ctx context.Context, in *pb.ReportRequest) (*pb.ReportResponse, error) {

	resp, err := http.Get(url)
	if err != nil {
		return nil, err
	}

	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		return nil, err
	}

	sb := string(body)

	return &pb.ReportResponse{Name: sb}, nil
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
