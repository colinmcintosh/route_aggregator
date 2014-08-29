Name: Route Aggregator

Author: Colin McIntosh

Current Version: 0.1

Version Date: 08/28/2014

License: MIT


Description
---------------
	This tool takes an input file of static routes, combines routes into a
	shorter prefix lenth, if possible, and creates an output file with the
	resulting static routes.

	
Usage Guidelines
---------------
	The tool will aggregate contiguous static routes have the same next-hop
	and combine to form a supernet.
	The tool will read any lines in the input file that follow the format of:
		"ip route x.x.x.x/y z.z.z.z"
		OR
		"ip route x.x.x.x/y.y.y.y z.z.z.z"
		OR
		"ip route x.x.x.x y.y.y.y z.z.z.z"
	This means that the input file can be only a line-delimited listing of
	static routes or a running-config. The output file will only contain the
	resulting static routes.
	The tool will ONLY aggregate IPv4 routes.
	The tool will NOT aggregate routes with an interface destination.
	The tool will NOT preserve remarks.

	
Command Line Usage
---------------
	> python route_aggregator.py [input_file] [output_file]
	 
	input_file - (Optional) This is the path of the file that contains the
							static routes to be aggregated. [Default = in.txt]
							
	output_file - (Optional) This is the path of the file that will contain the
							 resulting static routes. [Default = out.txt]
							 

Changelog
---------------
	v0.1 - Initial build. Contains only basic functionality.
	
	
To-do
---------------
	-IPv6 support
	-Preserve in-line remarks
	-Support routes with destination interface
	-Full command-line support
	-Juniper static route support
	