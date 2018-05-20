# -*- mode: ruby -*-
# vi: set ft=ruby :
################################################################################
# JAVA 8, KIBANA
################################################################################

VAGRANTFILE_API_VERSION = '2'.freeze
Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.synced_folder "D:/Arquivos/devops/vagrant/kibana", "/home/vagrant/share", nfs:true
  config.vm.box = 'ubuntu/trusty64'

  config.vm.define :kibana01 do |kibana01_config|
    kibana01_config.vm.hostname = 'kibana01'
    kibana01_config.vm.network :private_network,
                         ip: '192.168.10.10'
    kibana01_config.vm.provision :shell, path: "boot.sh"
      config.vm.provider "virtualbox" do |v|
        v.memory = 2048
        v.cpus = 2
        v.name = "kibana01"
      end
    kibana01_config.vm.network "forwarded_port", guest: 9200, host: 9201 # ES
    kibana01_config.vm.network "forwarded_port", guest: 5601, host: 5602 # Kibana
    kibana01_config.vm.network "forwarded_port", guest: 8111, host: 8112 # HTTP server for test
    kibana01_config.vm.network "forwarded_port", guest: 5044, host: 5041 # logstash
  end
################################################################################
end
