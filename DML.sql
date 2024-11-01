-- Insertar tipos de empleado
INSERT INTO tipoEmpleado (Id_tipo_empleado,Tipo, Permisos) VALUES
('Administrador', 'Acceso total'),
('Desarrollador', 'Acceso a desarrollo y informes'),
('Analista', 'Acceso a informes y proyectos');

-- Insertar módulos
INSERT INTO modulos (Id_modulo, Nombre) VALUES
('MOD01', 'Gestión de Proyectos'),
('MOD02', 'Gestión de Recursos'),
('MOD03', 'Informes');

-- Insertar empleados
INSERT INTO empleado (Id_empleado,Rut, Nombre, Direccion, Telefono, Correo, Fecha_inicio, Salario, Fecha_nacimiento, Contrasena, Id_tipoEmpleado)VALUES 
('12.234.567-7','Juan Pérez', 'Av. Libertad 123', '987654321', 'juan.perez@example.com', '2021-06-15', 1500000, '1985-04-20', 'Jperez85!', 1),
('23.532.734-6','Ana Vidal', 'Calle Central 456', '987123456', 'ana.gomez@example.com', '2022-01-05', 1800000, '1990-09-12', 'Agomez90$', 2),
('20.746.237-5','Carlos Ruiz', 'Pasaje Norte 789', '987987654', 'carlos.ruiz@example.com', '2020-11-20', 2000000, '1982-12-01', 'Cruiz82*', 1),
('21.524.759-4','Laura Torres', 'Av. Sur 321', '987654987', 'laura.torres@example.com', '2019-03-27', 2100000, '1992-03-08', 'Ltorres92#', 3),
('8.845.273-9','Pedro Sánchez', 'Calle Este 654', '987321654', 'pedro.sanchez@example.com', '2023-07-12', 1300000, '1988-07-19', 'Psanchez88&', 2),
('14.673.955-6','Sofía Hernández', 'Boulevard Oeste 852', '987456789', 'sofia.hernandez@example.com', '2021-09-18', 2000000, '1995-02-14', 'Shernandez95%', 1);

-- Insertar proyectos
INSERT INTO proyecto (Id_proyecto,Nombre, Descripcion, Fecha_inicio, Fecha_fin) VALUES
('Desarrollo de App Móvil', 'Aplicación para gestionar tareas diarias', '2024-01-10', '2024-06-15'),
('Sistema de Gestión de Inventario', 'Sistema para control de stock en tiempo real', '2024-03-05', '2024-09-30'),
('HRConnect', 'Plataforma de Bienestar y Desarrollo Profesional', '2024-03-05', '2024-09-30');

-- Insertar departamentos
INSERT INTO departamento (id_departamento,Nombre, Telefono, Id_empleado) VALUES
('Desarrollo Sostenible', '555-1234', 1),
('Recursos Humanos', '555-5678', 2),
('Investigacion y Desarrollo', '555-8765', 3),
('Ventas', '555-8765', 4);

-- Insertar relación entre empleados y proyectos
INSERT INTO proyectoEmpleado (Id_proyecto, Id_empleado) VALUES
(1, 1), -- juan Pérez esta en el proyecto desarrollo app movil
(1, 2), -- Ana Vidal esta en el proyecto desarrollo app movil
(2, 3), -- Carlos Ruiz esta en el proyecto sistema de gestion de inventarios
(2, 4), -- Laura Torres esta en el proyecto sistema de gestion de inventarios  
(3, 5); -- Pedro Sánchez esta en el proyecto HRConnect

-- Insertar registros de tiempo
INSERT INTO registroTiempo (Nombre, Direccion, Telefono, Correo, Fecha_inicio, Salario, Id_proyectoEmpleado) VALUES
('Juan Pérez', 'Calle Falsa 123', '555-0001', 'juan@example.com', '2024-01-10', 3000, 1),
('Ana Gómez', 'Avenida Siempre Viva 456', '555-0002', 'ana@example.com', '2024-01-10', 2500, 1),
('Luis Martínez', 'Boulevard Libertad 789', '555-0003', 'luis@example.com', '2024-03-05', 2200, 2);

-- Insertar informes
INSERT INTO informe (Nombre_informe, Fecha_creacion, Id_empleado) VALUES
('Informe de Progreso del Proyecto Móvil', '2024-04-01', 1),
('Informe de Inventario', '2024-06-01', 3);

-- Insertar accesos
INSERT INTO accesos (id_acceso, id_modulo, id_tipo_empleado) VALUES
('MOD01', 1),  -- Administrador tiene acceso a Gestión de Proyectos
('MOD01', 2),  -- Desarrollador tiene acceso a Gestión de Proyectos
('MOD02', 1),  -- Administrador tiene acceso a Gestión de Recursos
('MOD02', 2),  -- Desarrollador tiene acceso a Gestión de Recursos
('MOD03', 1),  -- Administrador tiene acceso a Informes
('MOD03', 2),  -- Desarrollador tiene acceso a Informes
('MOD03', 3);  -- Analista tiene acceso a Informes

-- Insertar datos en la tabla departamentoEmpleado
INSERT INTO departamentoEmpleado (id_departamento, id_empleado) VALUES
(1, 1),  -- Juan Pérez asignado al departamento de Desarrollo
(2, 2),  -- Ana Gómez asignada al departamento de Recursos Humanos
(3, 3);  -- Luis Martínez asignado al departamento de Administración
