servers_config = {
    'servers': [
      {
          'hostname': "net1",
          'ip': "192.168.11.11",
          'port_forwarding': [
              (22, 2011)
          ],
      }
      #{:hostname => "net2",:ip => "192.168.22.11" , :ssh_port => "2022"},
      #{:hostname => "net3",:ip => "192.168.33.11" , :ssh_port => "2033"}
    ]
}
