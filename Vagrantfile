Vagrant.configure("2") do |config|
  # Ubuntu 16.04 with docker, docker-compose and docker-machine
  config.vm.box = "comiq/dockerbox"

  # Forward Django's port to vagrant machine
  config.vm.network "forwarded_port", guest: 8000, host: 8000
  # Copy everyting in project to /vagrant under vagrant machine
  config.vm.synced_folder ".", "/vagrant"

  # Configure virtual box
  config.vm.provider "virtualbox" do |vb|
    vb.name = 'imagestore'
  end
end
