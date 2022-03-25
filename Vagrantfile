Vagrant.configure("2") do |config|
	config.ssh.insert_key = false
	config.vm.provider "virtualbox" do |virtualbox|
		virtualbox.memory = 2048
		virtualbox.cpus = 2
		virtualbox.gui = false
		virtualbox.name = "Kali"
	end
	config.vm.box = "kalilinux/rolling"
	config.vm.provision "shell", inline: <<-SCRIPT
		cp -f /etc/apt/sources.list{,.bkup}
		cp -f /etc/apt/sources.list /tmp
		# https://mirror.aarnet.edu.au/pub/kali/kali
		sed -i 's$http://http.kali.org/kali$https://mirrors.ocf.berkeley.edu/kali/$' /tmp/sources.list
		cat /tmp/sources.list > /etc/apt/sources.list
	SCRIPT
	config.vm.provision "shell", inline: "touch /home/vagrant/.hushlogin", run: "always"
	config.vm.synced_folder ".", "/home/vagrant/Documents/CTFs", create: true
	config.vm.synced_folder "../ctfd_challenges", "/home/vagrant/Documents/ctfd_challenges", create: true
end
