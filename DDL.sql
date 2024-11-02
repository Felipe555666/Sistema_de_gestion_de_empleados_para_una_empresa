-- Creación de tablas

CREATE TABLE tipoEmpleado (
    Id_tipo_empleado INT PRIMARY KEY AUTO_INCREMENT,
    Tipo VARCHAR(50) NOT NULL,
    Permiso INT NOT NULL
);

CREATE TABLE empleado (
    id_empleado INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    direccion VARCHAR(200) NOT NULL,
    telefono VARCHAR(20) NOT NULL,
    correo VARCHAR(100) NOT NULL,
    fecha_inicio DATE NOT NULL,
    salario DECIMAL(10, 2) NOT NULL,
    fecha_nac DATE NOT NULL,
    estado_empleado BOOLEAN DEFAULT TRUE,
    contrasena VARCHAR(255) NOT NULL,
    id_tipo_empleado INT,
    FOREIGN KEY (id_tipo_empleado) REFERENCES tipoEmpleado(Id_tipo_empleado)
);

CREATE TABLE proyectos (
    id_proyecto INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE NOT NULL
);

CREATE TABLE proyectoEmpleado (
    Id_pro_empleado INT PRIMARY KEY AUTO_INCREMENT,
    Id_proyecto INT,
    Id_empleado INT,
    FOREIGN KEY (Id_proyecto) REFERENCES proyecto(id_proyecto),
    FOREIGN KEY (Id_empleado) REFERENCES empleado(id_empleado)
);

CREATE TABLE registroTiempo (
    Id_reg_tiempo INT PRIMARY KEY AUTO_INCREMENT,
    Id_pro_empleado INT,
    horas_trabajadas INT DEFAULT 0,
    fecha DATE NOT NULL,
    FOREIGN KEY (Id_pro_empleado) REFERENCES proyectoEmpleado(Id_pro_empleado)
);

CREATE TABLE departamento (
    Id_departamento INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(100) NOT NULL,
    Telefono VARCHAR(20)
);

CREATE TABLE departamentoEmpleado (
    Id_dep_empleado INT PRIMARY KEY AUTO_INCREMENT,
    Id_departamento INT,
    Id_empleado INT,
    FOREIGN KEY (Id_departamento) REFERENCES departamento(Id_departamento),
    FOREIGN KEY (Id_empleado) REFERENCES empleado(id_empleado)
);

CREATE TABLE informe (
    Id_informe INT PRIMARY KEY AUTO_INCREMENT,
    Nombre_informe VARCHAR(100) NOT NULL,
    Fecha_creacion DATE NOT NULL,
    Id_empleado INT,
    Estado_informe VARCHAR(50) NOT NULL,
    FOREIGN KEY (Id_empleado) REFERENCES empleado(id_empleado)
);

CREATE TABLE modulos (
    Id_modulo INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(100) NOT NULL,
    Nivel_requerido INT NOT NULL
);

CREATE TABLE Accesos (
    Id_acceso INT PRIMARY KEY AUTO_INCREMENT,
    Id_modulo INT,
    Id_tipo_empleado INT,
    FOREIGN KEY (Id_modulo) REFERENCES modulos(Id_modulo),
    FOREIGN KEY (Id_tipo_empleado) REFERENCES tipoEmpleado(Id_tipo_empleado)
);
