
CREATE TABLE proyecto (
    id_proyecto INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(30) NOT NULL,
    descripcion VARCHAR(30) NOT NULL,
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE NOT NULL
);

CREATE TABLE registroTiempo (
    id_reg_tiempo INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(30) NOT NULL,
    direccion VARCHAR(30) NOT NULL,
    telefono VARCHAR(30) NOT NULL,
    correo VARCHAR(30) NOT NULL,
    fecha_inicio DATE NOT NULL,
    salario INTEGER NOT NULL,
    id_pro_empleado INTEGER NOT NULL
);

CREATE TABLE empleado (
    id_empleado INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
    rut VARCHAR (30) NOT NULL,
    nombre VARCHAR(30) NOT NULL,
    direccion VARCHAR(30) NOT NULL,
    telefono VARCHAR(30) NOT NULL,
    correo VARCHAR(30) NOT NULL,
    fecha_inicio DATE NOT NULL,
    salario INTEGER NOT NULL,
    fecha_nac DATE NOT NULL,
    estado_empleado VARCHAR (30) NOT NULL,
    contrasena VARCHAR(30) NOT NULL,
    id_tipo_empleado INTEGER NOT NULL
);

CREATE TABLE informe (
    id_informe INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
    nombre_informe VARCHAR(30) NOT NULL,
    fecha_creacion DATE NOT NULL,
    id_empleado INTEGER NOT NULL,
    estado_informe VARCHAR (30) NOT NULL
);

CREATE TABLE proyectoEmpleado (
    id_pro_empleado INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
    id_proyecto INTEGER NOT NULL,
    id_empleado INTEGER NOT NULL
);

CREATE TABLE departamentoEmpleado (
    id_dep_empleado INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
    id_departameto INTEGER NOT NULL,
    id_empleado INTEGER NOT NULL
);

CREATE TABLE departamento (
    id_departamento INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(30) NOT NULL,
    telefono VARCHAR(15) NOT NULL,
    id_empleado INTEGER NOT NULL
);

CREATE TABLE tipoEmpleado (
    id_tipo_empleado INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
    tipo VARCHAR(20) NOT NULL,
    permiso VARCHAR(100) NOT NULL
);

CREATE TABLE accesos (
    id_acceso INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
    id_modulo VARCHAR(12) NOT NULL,
    id_tipo_empleado INTEGER NOT NULL
);

CREATE TABLE modulos (
    id_modulo VARCHAR(12) PRIMARY KEY NOT NULL,
    nombre VARCHAR(40) NOT NULL
);

ALTER TABLE informe ADD FOREIGN KEY (id_empleado) REFERENCES empleado (id_empleado);
ALTER TABLE accesos ADD FOREIGN KEY (id_modulo) REFERENCES modulos (id_modulo);
ALTER TABLE accesos ADD FOREIGN KEY (id_tipo_empleado) REFERENCES tipoEmpleado (id_tipo_empleado);
ALTER TABLE proyectoEmpleado ADD FOREIGN KEY (id_proyecto) REFERENCES proyecto (id_proyecto);
ALTER TABLE departamento ADD FOREIGN KEY (id_empleado) REFERENCES empleado (id_empleado);
ALTER TABLE departamentoEmpleado ADD FOREIGN KEY (id_departamento) REFERENCES departamento (id_departamento);
ALTER TABLE proyectoEmpleado ADD FOREIGN KEY (id_empleado) REFERENCES empleado (id_empleado);
ALTER TABLE departamentoEmpleado ADD FOREIGN KEY (id_empleado) REFERENCES empleado (id_empleado);
ALTER TABLE empleado ADD FOREIGN KEY (id_tipo_empleado) REFERENCES tipo_empleado (id_tipo_empleado);
ALTER TABLE registroTiempo ADD FOREIGN KEY (id_pro_empleado) REFERENCES proyectoEmpleado (id_pro_empleado);