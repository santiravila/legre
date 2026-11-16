# legre
Tu biblioteca digital


## Entidades

### Libro
#### Relaciones
N libros <-> M autores
---

### Usuario
#### Descripcion
Es la superclase de la que heredan administradores y lectores. 
#### Atributos
id
fecha_registro
email 
nombre
#### Relaciones
...
---

### Lector
#### Descripcion
Un lector es el usuario final de la biblioteca. Se encarga de registrar libros existentes y de manipular dichos libros.
#### Atributos
id_usuario PK y FK donde {id_usuario} referencia Usuario.id
#### Relaciones
N clientes <-> M libros 


### Lector_Libros
#### Descripcion
Tabla intermedia 
#### Atributos
id_usuario, id_libro
---

### Administrador
#### Descripcion
Gestiona los libros disponibles 
#### Atributos
id_usuario PK y FK donde {id_usuario} referencia Usuario.id
#### Relaciones
...
---

### Autor
#### Descripcion
Escribe los libros.
#### Relaciones
N libros -> M autores
---

### Libro_Autor
#### Descripcion
Es una tabla para relacionar los libros y los autores
#### Atributos
id_autor, id_libro (PK Compuesta)
---







Resumen:
Hay libros.
Los libros tienen generos (entidades debiles)

Un usuario (superclase) puede ser administrador o lector. 
Un lector registra libros.
Un administrador gestiona los libros disponibles.

Hay autores.
Un autor escribe libros.