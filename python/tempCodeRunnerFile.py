for ip in ip_network(network, strict = False):
        print(ip)

        thread = Scanner(ip)
        thread.start()
        threads.append(thread)