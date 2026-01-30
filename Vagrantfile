# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  # Configuração Global para Libvirt (KVM)
  config.vm.provider :libvirt do |libvirt|
    libvirt.driver = "kvm"
    libvirt.memory = 4096 # 4GB RAM padrão
    libvirt.cpus = 2
  end

  # --- VM 1: Security Tools (SonarQube, Vault, DefectDojo) ---
  config.vm.define "security" do |sec|
    sec.vm.box = "generic/ubuntu2204" # Imagem leve e otimizada para KVM
    sec.vm.hostname = "security-server"
    
    # Rede Privada (IP Fixo para o Runner acessar)
    sec.vm.network "private_network", ip: "192.168.56.10"
    
    sec.vm.provider :libvirt do |v|
      v.memory = 6144 # 6GB (SonarQube + Java pesam)
      v.cpus = 2
    end

    # Instalação Básica do Docker (Shell Script)
    sec.vm.provision "shell", inline: <<-SHELL
      apt-get update
      apt-get install -y docker.io docker-compose
      usermod -aG docker vagrant
      # Habilita Docker Socket para acesso remoto (opcional, mas útil em labs)
      systemctl enable docker
      systemctl start docker
    SHELL
  end

  # --- VM 2: Production (Onde a App vai rodar) ---
  config.vm.define "production" do |prod|
    prod.vm.box = "generic/ubuntu2204"
    prod.vm.hostname = "prod-server"
    
    # Rede Privada
    prod.vm.network "private_network", ip: "192.168.56.20"

    prod.vm.provision "shell", inline: <<-SHELL
      apt-get update
      apt-get install -y docker.io
      usermod -aG docker vagrant
      systemctl enable docker
      systemctl start docker
    SHELL
  end
end