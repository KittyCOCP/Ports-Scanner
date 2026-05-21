# Escáner de Puertos Local 🐍

## Descripción General 📋

Este proyecto es un **Escáner de Puertos Local** desarrollado en Python. Su objetivo principal es auditar la seguridad del equipo identificando qué puertos se encuentran abiertos y escuchando conexiones. 

Al automatizar esta revisión, la herramienta permite:
* 🔍 **Detectar servicios innecesarios:** Identificar qué puertos abiertos no se están utilizando.
* 🛡️ **Reducir la superficie de ataque:** Facilitar el cierre de conexiones expuestas para mitigar riesgos.
* 💻 **Fortalecer el bastionado (*hardening*):** Proteger el dispositivo frente a posibles amenazas externas maliciosas.

---

## Guía de Uso e Instalación ⚙️

### Requisitos Previos
* Tener instalado **Python 3**.
* Una terminal de comandos (como Git Bash).

### Instrucciones de Ejecución
1. Descarga o copia el archivo de código y asegúrate de guardarlo con el nombre `scaner_puertos.py`.
2. Abre tu terminal y navega hasta la carpeta donde se encuentra el archivo usando el comando `cd`.
3. Ejecuta el script con el siguiente comando:
   
```bash
   python scaner_puertos.py
