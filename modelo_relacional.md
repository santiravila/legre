USUARIO(<u>id</u>, nombre, password, fecha_registro)
 
LECTOR(<u>id_usuario</u>, apodo)

ADMINISTRADOR(<u>id_usuario</u>, nivel_de_permiso)

LIBRO(<u>id</u>, ISBN, nombre, estado_activo, anio_publicacion, numero_paginas)

AUTOR(<u>id</u>, nombre, nacionalidad)

AUTOR_LIBRO(<u>id_autor</u>, <u>id_libro</u>)

LECTOR_LIBRO(<u>id_lector</u>, <u>id_libro</u>, estado)