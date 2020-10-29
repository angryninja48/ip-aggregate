from netaddr import IPNetwork, cidr_merge


def read_file(file_name):
    """
    Loops through a file of IP addresses and appends a /32 host route
    """
    ips = []
    with open('ipaddresses.txt', 'r') as file:
        for line in file:
            cidr = line[:-1] + '/32'
            ips.append(cidr)
    return ips

def aggregate(list_of_cidrs):
    """
	Given a list of CIDR's aggregate the list to a summarised subnet
	"""
    # Create new list with IPNetwork objects
    networks = []
    for network in list_of_cidrs:
        networks.append(IPNetwork(network))

    # Merge new list and return summarised networks
    networks = cidr_merge(networks)
    return networks

def main():
    file = 'ipaddresses.txt'

    list_of_cidrs = read_file(file)
    sumarised_networks = aggregate(list_of_cidrs)
    if sumarised_networks: 
        print('.' * 3)
        print('Aggregated IPv4 networks:')
        for network in sumarised_networks:
            print(network)
        print('.' * 3)

if __name__ == "__main__":
    main()