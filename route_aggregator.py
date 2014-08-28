import re, itertools
from ipaddress import ip_network


IP_ROUTE_REGEX = "^ip route (\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})(/\d{1,2}| \d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}) (\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}).*$"


def aggregate_routes(in_path, out_path):
    routes = _parse_routes(in_path)
    for dest, networks in dict(routes).items():
        routes[dest] = _aggregate_networks(networks)
    with open(out_path, "w") as out_file:
        out_file.write(_create_routes(routes))
    return


def _parse_routes(in_path):
    routes = {}
    with open(in_path) as in_file:
        for line in in_file:
            line = line.strip()
            match = re.match(IP_ROUTE_REGEX, line)
            if not match:
                continue
            network = (match.group(1)+match.group(2)).replace(" ", "/")
            try:
                routes[match.group(3)]
            except KeyError:
                routes[match.group(3)] = []
            routes[match.group(3)].append(network)
    return routes


def _aggregate_networks(networks):
    while True:
        combined = False
        for n1, n2 in itertools.combinations(networks, 2):
            n1o = ip_network(n1)
            n2o = ip_network(n2)
            if n1o.supernet() == n2o.supernet():
                combined = True
                networks.remove(n1)
                networks.remove(n2)
                networks.append(n1o.supernet().with_prefixlen)
                break
        if not combined: break
    return networks


def _create_routes(routes):
    output = ""
    for dest, networks in routes.items():
        for network in networks:
            output = output + ("ip route %s %s\n" % (network, dest))
    return output


if __name__ == "__main__":
    aggregate_routes("in.txt", "out.txt")
