<h1 align="center">Netstat</h1>

<p align="center">
  <img alt="Github Issues" src="https://img.shields.io/github/issues/Draylon/ogrc_remote_netstat">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/draylon/ogrc_remote_netstat">

  <img alt="Stars" src="https://img.shields.io/github/stars/draylon/ogrc_remote_netstat">

  <img alt="License" src="https://img.shields.io/github/license/draylon/ogrc_remote_netstat?color=56BEB8">

  <!-- <img alt="Github issues" src="https://img.shields.io/github/issues/draylon/ogrc_remote_netstat?color=56BEB8" /> -->

  <!-- <img alt="Github forks" src="https://img.shields.io/github/forks/draylon/ogrc_remote_netstat?color=56BEB8" /> -->

  <!-- <img alt="Github stars" src="https://img.shields.io/github/stars/draylon/ogrc_remote_netstat?color=56BEB8" /> -->
</p>

<!-- Status -->

<!-- <h4 align="center"> 
	🚧  Netstat 🚀 Under construction...  🚧
</h4> 

<hr> -->

<p align="center">
  <a href="#📌-about">About</a> &#xa0; | &#xa0; 
  <a href="#✨-features">Features</a> &#xa0; | &#xa0;
  <a href="#🚀-technologies">Technologies</a> &#xa0; | &#xa0;
  <a href="#✅-requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#🏁-starting">Starting</a> &#xa0; | &#xa0;
  <a href="#📝-license">License</a> &#xa0; | &#xa0;
  <a href="https://github.com/draylon" target="_blank">Author</a>
</p>

<br>

## 📌 About ##

    Assim, como já comentado, o usuário poderá solicitar a visualização dos endereços IP e portas remotas conforme a sua escolha em termos de protocolo de camada de transporte (UDP ou TCP). 

    Qdo não for escolhida a opção de protocolo (TCP ou UDP) deverão ser retornadas ambas, levando-se em consideração que as portas TCP e os respectivos endereços IP a serem mostrados deverão ser aqueles com status stablished. 

    Também no caso do protocolo TCP, será necessário informar as portas locais (do computador remoto) e remotas (dos computadores com os quais se conecta) . 

    Caso não seja fornecido o endereço IP da máquina remota da qual se deseja as informações, a ferramenta deverá retornar as informações da máquina local. 

    A Varredura deve retornar todas as portas utilizadas de ambos os protocolos (para informações da máquina local). 

    Para informações da máquina remota, basta inserir como primeiro argumento o endereço IP desejado. 

    Ex:
        #varreduraPortas 192.168.5.2 -TCP,
        #varreduraPortas 192.168.5.2 -UDP
        #varreduraPortas 192.168.5.2

## ✨ Features ##

✔ Varredura na máquina __remota__, por TCP e UDP\
✔ Varredura na máquina __local__, por TCP e UDP

## 🚀 Technologies ##

Trabalho utilizou:

- [python 3.9.2](https://python.org/)
- [Tabulate](https://pypi.org/project/tabulate/)
- [easysnmp](https://easysnmp.readthedocs.io/en/latest/)

## ✅ Requirements ##

Before starting 🏁, you need to have [Git](https://git-scm.com) and [Python](https://python.org/) installed.

## 🏁 Starting ##

```bash
# Install easysnmp required snmp libraries
$ sudo apt-get install libsnmp-dev snmp-mibs-downloader

# Install python development
$ sudo apt-get install gcc python-dev

# Install easysnmp
$ pip install easysnmp

# Clone this project
$ git clone https://github.com/Draylon/ogrc_remote_netstat.git

# Access
$ cd ogrc_remote_netstat

# Install dependencies
$ pip3 install -r requirements.txt

# Run the project
$ py -3 main.py

```

## 📝 License ##

This project is under license from MIT. For more details, see the [LICENSE](LICENSE.md) file.


Made with :heart: by <a href="https://github.com/draylon" target="_blank">𝓜!𝓻𝓪𝓬𝓵𝓮𝓐𝓾𝓻𝓪</a>

&#xa0;

<a href="#top">Back to top</a>
