import nmap

scanner = nmap.PortScanner()


print("Seja bem vindo ao DIOScanner")
print("<-------------------------->")

ip = input('Digite o ip a ser varrido:')
print('O ip digitado foi:', ip)
type(ip)

menu = input("""\n Escolha o tipo de varredura a ser relizada
                1 -> Varredura do tipo SYN
                2 -> Varredura do tipo UDP
                3 -> Varredura do tipo Intensa
                Digite a opção escolhida: """)

print("A opção escolhida foi", menu)

if menu == '1':
    print("versão do Nmap: ", scanner.nmap_version())
    scanner.scan(ip, '1-1024', '-v -sS ')
    print(scanner.scaninfo())
    print("Status do IP:", scanner[ip].state())
    print(scanner[ip].all_protocols())
    print("")
    print("Portas Abertas: ", scanner[ip]['tcp'].keys())

elif menu == '2':
    print("versão do Nmap: ", scanner.nmap_version())
    scanner.scan(ip, '1-1024', '-v -sU ')
    print(scanner.scaninfo())
    print("Status do IP:", scanner[ip].state())
    print(scanner[ip].all_protocols())
    print("")
    print("Portas Abertas: ", scanner[ip]['udp'].keys())

elif menu == '3':
    print("versão do Nmap: ", scanner.nmap_version())
    scanner.scan(ip, '1-1024', '-v -sC ')
    print(scanner.scaninfo())
    print("Status do IP:", scanner[ip].state())
    print(scanner[ip].all_protocols())
    print("")
    print("Portas Abertas: ", scanner[ip]['tcp'].keys())

else:
    print("Escolha um opção valida !")
