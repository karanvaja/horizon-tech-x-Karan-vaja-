from scapy.all import sniff, IP, TCP, UDP, Raw

def packet_callback(packet):
    
    if IP in packet:
        ip_layer = packet[IP]
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst
        proto = ip_layer.proto
        
        
        proto_name = "Other"
        if proto == 6:
            proto_name = "TCP"
        elif proto == 17:
            proto_name = "UDP"
        elif proto == 1:
            proto_name = "ICMP"

        print(f"\n[+] New Packet: {src_ip} -> {dst_ip} | Protocol: {proto_name}")

        
        if packet.haslayer(TCP):
            print(f"    TCP Port: {packet[TCP].sport} -> {packet[TCP].dport}")
        elif packet.haslayer(UDP):
            print(f"    UDP Port: {packet[UDP].sport} -> {packet[UDP].dport}")

        
        if packet.haslayer(Raw):
            payload = packet[Raw].load
            try:
                
                print(f"    Payload: {payload[:80].decode('utf-8', errors='ignore')}")
            except:
                print(f"    Payload (raw): {payload[:40]}")


print("Starting sniffer... Press Ctrl+C to stop.")
sniff(prn=packet_callback, store=0)