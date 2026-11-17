USUARIO(<u>id</u>, nombre, password, fecha_registro)
 
LECTOR(<u>id_usuario</u>, apodo)

ADMINISTRADOR(<u>id_usuario</u>, nivel_de_permiso)
donde {id_usuario} referencia a USUARIO.id

LIBRO(<u>id</u>, ISBN, nombre, estado_activo, anio_publicacion, numero_paginas)

AUTOR(<u>id</u>, nombre, nacionalidad)

AUTOR_LIBRO(<u>id_autor</u>, <u>id_libro</u>)
donde {id_autor} referencia a AUTOR.id
donde {id_libro} referencia a LIBRO.id

LECTOR_LIBRO(<u>id_lector</u>, <u>id_libro</u>, estado)
donde {id_lector} referencia a LECTOR.id
donde {id_libro} referencia LIBRO.id