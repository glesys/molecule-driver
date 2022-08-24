# Molecule GleSYS Plugin

Molecule driver to spin up and run tests in GleSYS Cloud servers for easy testing

# Installation and Usage

```
pip install molecule-glesys
```

Create a new role with molecule using this driver:

```
molecule init role <role_name> -d glesys
```

Configure `<role_name>/molecule/default/molecule.yml` with required parameters.  
Sample config:

```yaml
dependency:
  name: galaxy
  options:
    requirements-file: molecule/default/collections.yml
driver:
  name: glesys
  vm_username: molecule

platforms:
  - name: "demo.demo-ubuntu-20-04"
    template: Ubuntu 20.04 LTS (Focal Fossa)
    description: "ubuntu-20-04"
    datacenter: "Falkenberg"
    platform: KVM
    cpus: 2
    memory: 2048
    disk: 20

  - name: "demo.demo-debian-11"
    template: Debian 11 (Bullseye)
    description: "debian-11"
    datacenter: "Falkenberg"
    platform: KVM
    cpus: 2
    memory: 2048
    disk: 20

provisioner:
  name: ansible
verifier:
  name: ansible
```

# License

The [MIT](LICENSE) License.
