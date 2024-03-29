#!/usr/bin/python
#!encoding: UTF-8
import sys
import math

def calc_pi (n):
 
    
  if(n>0):
    PI35= 3.1415926535897931159979634685441852
    iniciointervalo=0
    sumatoria=0
    intervalos=1.0/float(n)
    for i in range(n):
      x_i=((i+1)-1.0/2.0)/n
      fx_i=4.0/(1.0 + x_i*x_i)
      iniciointervalo+=intervalos
      sumatoria+=fx_i
    aprox_pi=sumatoria/n
    return (aprox_pi)
    
    
#Programa Principal

argumentos=sys.argv[1:]
if(len(argumentos)==2):
      n=int(argumentos[0])
      aproxima = int(argumentos[1])
else:       
      n=(int(raw_input("Introduzca el nº de intervalos (n>0)")))
      aproxima =(int(raw_input("Introduzca el nº de aproximaciones")))
if (n>0):
      PI35DT= 3.1415926535897931159979634685441852
      intervalo = n
      lista = []
      for i in range(aproxima):
	valor=calc_pi(intervalo)
	lista.append (valor)
	intervalo += n
      print lista
      diferencia = []
      for i in range (aproxima):
	dif = abs(PI35DT - lista[i])
	diferencia.append (dif)
      print "i\tPI35DT\tlista i\tPI35DT - lista i"
      for i in range(aproxima):
	print "%d\t%1.10f\t%1.10f\t%1.10f" % (i+1,PI35DT,lista[i],diferencia[i])