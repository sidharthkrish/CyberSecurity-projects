package port

import (
	"net"
	"strconv"
	"time"
)

type ScanResult struct {
	Port  string
	State string
}

func ScanPort(protocol, hostname string, port int) ScanResult {
	result := ScanResult{Port: protocol + "/" + strconv.Itoa(port)}
	address := hostname + ":" + strconv.Itoa(port)
	conn, err := net.DialTimeout(protocol, address, 60*time.Second)

	if err != nil {
		result.State = "Closed"
		return result
	}
	defer conn.Close()

	result.State = "Open"
	return result
}

func InitialScan(hostname string) []ScanResult {
	var results []ScanResult
	var x ScanResult
	for i := 1; i <= 1024; i++ {
		x = ScanPort("tcp", hostname, i)
		if x.State == "open" {
			results = append(results, x)
		}

		x = ScanPort("udp", hostname, i)
		if x.State == "open" {
			results = append(results, x)
		}

	}
	return results

}
