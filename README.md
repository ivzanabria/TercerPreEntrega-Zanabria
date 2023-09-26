
# Orden de ejecución de las pruebas  
1. Se ejecuta `git clone https://github.com/ivzanabria/TercerPreEntrega-Zanabria.git`
2. Para crear los archivos de migración  se ejecuta `python manage.py makemigrations`
3. python manage.py migrate` esto aplicara las migraciones en la base de datos
4.  Creamos un super usuario para el panel de administración ejecutas `python manage.py superuser` 
5. Se ejecuta `python manage.py runserver`
6. Se agrega los objetos: Curso, Estudiante, Entregable y Docente.-
7. Vas `inicio` buscas por **alumno** 

## Esquema de los archivos en el proyecto
Los archivos y carpetas principales son:
 1. models.py. Aqui tenemos la representación en la base de datos.
 2. foms.py. Aqui tenemos los formularios que bindeamos con los archivos html.
 3. admin.py En este archivo agregamos los modelos que queremos mostrar en el panel de administración.
 

 
