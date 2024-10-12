# Modulos de odoo 

Este documento describe los pasos necesarios para clonar el repositorio de Odoo, agregar un submódulo personalizado, y asegurarse de que sea excluido en el `.gitignore` del repositorio principal.

## Pasos para clonar y agregar el submódulo

### 1. Clonar el repositorio de Odoo

Primero, debes clonar el repositorio oficial de Odoo en tu máquina local. Para hacerlo, ejecuta el siguiente comando:

```bash
git clone git@github.com:odoo/odoo.git
```
Esto descargará el repositorio de Odoo en tu sistema

### 2. Agregar un submódulo personalizado

Después de clonar el repositorio de Odoo, necesitas agregar tu repositorio personalizado como un submódulo. En este caso, vamos a agregar el submódulo odoo-modules-bein. Para hacerlo, ejecuta el siguiente comando en la raíz del repositorio de Odoo:

```bash
git submodule add git@github.com:enner1/odoo-modules-bein.git odoo-modules-bein
```
Esto agregará el submódulo odoo-modules-bein como un submódulo del repositorio de Odoo.

### 3. Excluir el submódulo del repositorio principal

Para asegurarse de que el submódulo se excluya del repositorio principal, debes editar el archivo `.gitignore` en la raíz del repositorio de Odoo. Abre el archivo `.gitignore` en tu editor de texto favorito y agrega el siguiente texto al final:

```
/odoo-modules-bein/
```

Esto excluirá el submódulo odoo-modules-bein del repositorio principal.

### Nota

Para agregar cambios en el repositorio de odoo para modulos personalizados, debes ubicarte en la carpeta `odoo-modules-bein` y ejecutar los comandos de git para agregar, modificar, o eliminar archivos.
