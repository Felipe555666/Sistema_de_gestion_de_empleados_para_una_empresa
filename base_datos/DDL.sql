-- creacion de tablas
CREATE TABLE tipoEmpleado (
    Id_tipo_empleado INT PRIMARY KEY AUTO_INCREMENT,
    Tipo VARCHAR(50) NOT NULL,
    Permiso INT NOT NULL CHECK (Permiso >= 0 AND Permiso <= 10)
);


CREATE TABLE empleado (
    id_empleado INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    direccion VARCHAR(200) NOT NULL,
    telefono VARCHAR(20) NOT NULL,
    correo VARCHAR(100) NOT NULL UNIQUE,
    fecha_inicio DATE NOT NULL,
    salario DECIMAL(10, 2) NOT NULL CHECK (salario > 0),
    fecha_nac DATE NOT NULL,
    estado_empleado BOOLEAN DEFAULT TRUE,
    contrasena VARCHAR(255) NOT NULL,
    id_tipo_empleado INT,
    FOREIGN KEY (id_tipo_empleado) REFERENCES tipoEmpleado(Id_tipo_empleado)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);


CREATE TABLE proyecto (
    id_proyecto INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE NOT NULL,
    CONSTRAINT check_fechas CHECK (fecha_fin >= fecha_inicio)
);


CREATE TABLE proyectoEmpleado (
    Id_pro_empleado INT PRIMARY KEY AUTO_INCREMENT,
    Id_proyecto INT,
    Id_empleado INT,
    FOREIGN KEY (Id_proyecto) REFERENCES proyecto(id_proyecto)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (Id_empleado) REFERENCES empleado(id_empleado)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    UNIQUE (Id_proyecto, Id_empleado)
);


CREATE TABLE registroTiempo (
    Id_reg_tiempo INT PRIMARY KEY AUTO_INCREMENT,
    Id_pro_empleado INT,
    horas_trabajadas DECIMAL(5,2) DEFAULT 0 CHECK (horas_trabajadas >= 0 AND horas_trabajadas <= 24),
    fecha DATE NOT NULL,
    FOREIGN KEY (Id_pro_empleado) REFERENCES proyectoEmpleado(Id_pro_empleado)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);


CREATE TABLE departamento (
    Id_departamento INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(100) NOT NULL UNIQUE,
    Telefono VARCHAR(20)
);


CREATE TABLE departamentoEmpleado (
    Id_dep_empleado INT PRIMARY KEY AUTO_INCREMENT,
    Id_departamento INT,
    Id_empleado INT,
    FOREIGN KEY (Id_departamento) REFERENCES departamento(Id_departamento)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (Id_empleado) REFERENCES empleado(id_empleado)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    UNIQUE (Id_departamento, Id_empleado)
);


CREATE TABLE informe (
    Id_informe INT PRIMARY KEY AUTO_INCREMENT,
    Nombre_informe VARCHAR(100) NOT NULL,
    Fecha_creacion DATE NOT NULL,
    Id_empleado INT,
    Estado_informe VARCHAR(50) NOT NULL,
    FOREIGN KEY (Id_empleado) REFERENCES empleado(id_empleado)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);


CREATE TABLE modulos (
    Id_modulo INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(100) NOT NULL UNIQUE,
    Nivel_requerido INT NOT NULL CHECK (Nivel_requerido >= 0 AND Nivel_requerido <= 10)
);


CREATE TABLE Accesos (
    Id_acceso INT PRIMARY KEY AUTO_INCREMENT,
    Id_modulo INT,
    Id_tipo_empleado INT,
    Fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
    Exitoso BOOLEAN NOT NULL,
    FOREIGN KEY (Id_modulo) REFERENCES modulos(Id_modulo)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (Id_tipo_empleado) REFERENCES tipoEmpleado(Id_tipo_empleado)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
