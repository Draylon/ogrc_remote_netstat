## Repositorio
[link](https://github.com/Draylon/ogrc_remote_netstat)

## Enunciado
Assim, como já comentado, o usuário poderá solicitar a visualização dos endereços IP e portas remotas
conforme a sua escolha em termos de protocolo de camada de transporte (UDP ou TCP). 

Qdo não for escolhida a opção de protocolo (TCP ou UDP) deverão ser retornadas ambas, levando-se em consideração que as portas
TCP e os respectivos endereços IP a serem mostrados deverão ser aqueles com status stablished. 

Também no caso do protocolo TCP, será necessário informar as portas locais (do computador remoto) e remotas (dos computadores com os quais se conecta) . 

Caso não seja fornecido o endereço IP da máquina remota da qual se deseja as informações, a ferramenta deverá retornar as informações da máquina local. 

Exemplo de execução da ferramenta na linha de comando:
 - varreduraPortas -TCP
 - varreduraPortas -UDP
 - varreduraPortas

que deve retornar todas as portas utilizadas de ambos os protocolos (para informações da máquina local). 

Para informações da máquina remota, basta inserir como primeiro argumento o endereço IP desejado. 

Ex: #varreduraPortas 192.168.5.2 -TCP, ou #varreduraPortas 192.168.5.2 -UDP ou ainda, simplesmente: #varreduraPortas
192.168.5.2.