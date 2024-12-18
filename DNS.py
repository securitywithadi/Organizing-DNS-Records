with open('packets.txt') as f:
    packets = f.readlines()

ip_sizes = {}
for packet in packets:
    src_ip, size = packet.strip().split(',')
    ip_sizes[src_ip] = ip_sizes.get(src_ip, 0) + int(size)

print(ip_sizes)
