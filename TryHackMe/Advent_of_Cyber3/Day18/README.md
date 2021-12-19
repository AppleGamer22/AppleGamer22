# TryHackMe [Advent of Cyber 3](https://tryhackme.com/room/adventofcyber3) Day 18
### References
* Hammond, J. (2021). TryHackMe! Advent of Cyber - Day 18 [YouTube Video]. In YouTube. https://youtu.be/jpRTzb1eZQ4
* The AWS CLI and `curl` were installed in my Kali Linux environment by running `sudo apt install awscli curl`.
* Set-up Docker on Kali Linux:
```bash
$ vagrant ssh
$ sudo apt install docker.io
$ sudo usermod -aG docker $USER
$ logout
$ vagrant ssh
```

## What command will list container images stored in your local container registry?
**Answer**: `docker images`
## What command will allow you to save a Docker image as a `tar` archive?
**Answer**: `docker save`
## What is the name of the file (including file extension) for the configuration, repository tags, and layer hash values stored in a container image?
1. Save the Docker image contents to the local file system:
```bash
$ docker save -o aoc3.tar public.ecr.aws/h0w1j9u3/grinch-aoc
$ tar -xf aoc3.tar && rm aco3.tar
```
2. Each folder with a hashed name describes a specific layer from the Docker image's `Dockerfile`, and the `manifest.json` describes the order in which the layers were made:
```bash
$ ls
213c48ef9a7134c0a6215bb1a42cb915a83d89eef736d20ec38f87fa901571ea  5901fbb6955cebd9cf4705ec8479409e8fa3071355309e217bba07051ead5b7c  f4d5cac1d6da73b6b3f3f0382471933622e734fd72af78552f161c5d0e07c602       repositories
226bc23b18064b4d0a72fb3c59816f38b241ef8165a75317fb63b4231d69fe59  6ac147b05d7b819ea203a80b33069b780ab2733ba556218c1b0beda7a641d8d9  f886f00520700e2ddd74a14856fcc07a360c819b4cea8cee8be83d4de01e9787.json
2c06d66a6d19b20abaeb8ae4c9f68e9e2bce2419a5acba9a009dc512ca85c918  a79cd751d74ebece5faee3b22ac88e11b5e3c5dd10bd36b9132ba895bde96807  manifest.json
52c3108fa9ec86ba321f021d91d0da0c91a2dd2ac173cd27b633f6c2962fac6f  d8503a2c46a85f35525c34c40ca8366c7e190117ef74d81b5d2c52aca01acd75  README.md
```

**Answer**: `manifest.json`
## What is the token value you found for the bonus challenge?
1. Extract the layer that uses `envconsul` and look for configuration files:
```bash
$ cd 2c06d66a6d19b20abaeb8ae4c9f68e9e2bce2419a5acba9a009dc512ca85c918
$ ls
json  layer.tar  VERSION
$ tar -xf layer.tar && rm layer.tar
$ ls
json  root  VERSION
$ tree root
root
└── envconsul
    └── config.hcl
```
2. `grep` for tokens:
```
$ cat root/envconsul/config.hcl | grep "token"
  # This is the token to use when communicating with the Vault server.
  # assumption that you provide it with a Vault token; it does not have the
  # incorporated logic to generate tokens via Vault's auth methods.
  token = "7095b3e9300542edadbc2dd558ac11fa"
  # This tells Envconsul to load the Vault token from the contents of a file.
  # - by default Envconsul will not try to renew the Vault token, if you want it
  # to renew you will need to specify renew_token = true as below.
  # - Envconsul will periodically stat the file and update the token if it has
  # vault_agent_token_file = "/path/to/vault/agent/token/file"
  # This tells Envconsul that the provided token is actually a wrapped
  # token that should be unwrapped using Vault's cubbyhole response wrapping
  unwrap_token = true
  # This option tells Envconsul to automatically renew the Vault token given.
  # If you are unfamiliar with Vault's architecture, Vault requires tokens be
  # automatically renew the token at half the lease duration of the token. The
  # you want to renew the Vault token using an out-of-band process.
  # There is an exception to the default such that if vault_agent_token_file is
  # set, either from the command line or the above option, renew_token defaults
  # token itself.
  renew_token = true
```

**Answer**: `7095b3e9300542edadbc2dd558ac11fa`
