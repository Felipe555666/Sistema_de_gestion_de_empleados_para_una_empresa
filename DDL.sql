
CREATE TABLE proyecto (
    id_proyecto INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(30) NOT NULL,
    descripcion VARCHAR(30) NOT NULL,
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE NOT NULL
);

CREATE TABLE registroTiempo (
    id_registroTiempo INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(30) NOT NULL,
    direccion VARCHAR(30) NOT NULL,
    telefono VARCHAR(30) NOT NULL,
    correo VARCHAR(30) NOT NULL,
    fecha_inicio DATE NOT NULL,
    salario INTEGER NOT NULL,
    id_proyectoEmpleado INTEGER NOT NULL
);

CREATE TABLE empleado (
    id_empleado INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(30) NOT NULL,
    direccion VARCHAR(30) NOT NULL,
    telefono VARCHAR(30) NOT NULL,
    correo VARCHAR(30) NOT NULL,
    fecha_inicio DATE NOT NULL,
    salario INTEGER NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    contrasena VARCHAR(30) NOT NULL,
    id_tipoEmpleado INTEGER NOT NULL
);

CREATE TABLE informe (
    id_informe INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
    nombre_informe VARCHAR(30) NOT NULL,
    fecha_creacion DATE NOT NULL,
    id_empleado INTEGER NOT NULL
);

CREATE TABLE proyectoEmpleado (
    id_proyectoEmpleado INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
    id_proyecto INTEGER NOT NULL,
    id_empleado INTEGER NOT NULL
);

CREATE TABLE departamentoEmpleado (
    id_departamentoEmpleado INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
    id_departameto INTEGER NOT NULL,
    id_empleado INTEGER NOT NULL
);

CREATE TABLE departamento (
    id_departamento INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
    departamento_nombre VARCHAR(30) NOT NULL,
    telefono VARCHAR(15) NOT NULL,
    id_empleado INTEGER NOT NULL
);

CREATE TABLE tipoEmpleado (
    id_tipoEmpleado INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
    tipo VARCHAR(20) NOT NULL,
    permisos VARCHAR(100) NOT NULL
);

CREATE TABLE accesos (
    id_accesos INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
    id_modulo VARCHAR(12) NOT NULL,
    id_tipoEmpleado INTEGER NOT NULL
);

CREATE TABLE modulos (
    id_modulo VARCHAR(12) PRIMARY KEY NOT NULL,
    nombre VARCHAR(40) NOT NULL
);

ALTER TABLE informe ADD FOREIGN KEY (id_empleado) REFERENCES empleado (id_empleado);
ALTER TABLE accesos ADD FOREIGN KEY (id_modulo) REFERENCES modulos (id_modulo);
ALTER TABLE accesos ADD FOREIGN KEY (id_tipoEmpleado) REFERENCES tipoEmpleado (id_tipoEmpleado);
ALTER TABLE proyectoEmpleado ADD FOREIGN KEY (id_proyecto) REFERENCES proyecto (id_proyecto);
ALTER TABLE departamento ADD FOREIGN KEY (id_empleado) REFERENCES empleado (id_empleado);
ALTER TABLE departamentoEmpleado ADD FOREIGN KEY (id_departamento) REFERENCES departamento (id_departamento);
ALTER TABLE proyectoEmpleado ADD FOREIGN KEY (id_empleado) REFERENCES empleado (id_empleado);
ALTER TABLE departamentoEmpleado ADD FOREIGN KEY (id_empleado) REFERENCES empleado (id_empleado);
ALTER TABLE empleado ADD FOREIGN KEY (id_tipoEmpleado) REFERENCES tipoEmpleado (id_tipoEmpleado);
ALTER TABLE registroTiempo ADD FOREIGN KEY (id_proyectoEmpleado) REFERENCES proyectoEmpleado (id_proyectoEmpleado);