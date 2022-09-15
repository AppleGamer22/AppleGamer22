Vagrant.configure("2") do |config|
	if Vagrant.has_plugin?("vagrant-vbguest")
		config.ssh.insert_key = false
		config.ssh.forward_agent = true
	else
		config.ssh.username = "vagrant"
		config.ssh.password = "vagrant"
	end
	config.vm.provider "virtualbox" do |virtualbox|
		virtualbox.memory = 2048
		virtualbox.cpus = 2
		virtualbox.gui = false
		virtualbox.name = "Kali"
	end
	config.vm.box = "kalilinux/rolling"
	# mirror configuration
	config.vm.provision "shell", inline: <<-SCRIPT
		cp -f /etc/apt/sources.list{,.bkup}
		cp -f /etc/apt/sources.list /tmp
		# https://mirror.aarnet.edu.au/pub/kali/kali
		sed -i 's$http://http.kali.org/kali$https://mirrors.ocf.berkeley.edu/kali/$' /tmp/sources.list
		cat /tmp/sources.list > /etc/apt/sources.list
	SCRIPT
	# zsh configuration
	config.vm.provision "shell", inline: <<-SCRIPT
		touch /home/vagrant/.hushlogin
		sudo apt remove zsh-autosuggestions
	SCRIPT
		config.vm.synced_folder ".", "/home/vagrant/Documents/CTFs", create: true
	config.vm.synced_folder "../ctfd_challenges", "/home/vagrant/Documents/ctfd_challenges", create: true
end
