Vagrant.configure("2") do |config|
	config.ssh.insert_key = false
	config.vm.provider "virtualbox" do |virtualbox|
		virtualbox.memory = 2048
		virtualbox.cpus = 2
		virtualbox.gui = false
		virtualbox.name = "Kali"
	end
	config.vm.box = "kalilinux/rolling"
	config.vm.provision "shell", inline: "touch /home/vagrant/.hushlogin", run: "always"
	config.vm.synced_folder ".", "/home/vagrant/Documents/CTFs", create: true
end