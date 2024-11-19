-- Insertar tipos de empleado
INSERT INTO tipoEmpleado (Tipo, Permiso) VALUES
('Administrador', 10),
('Gerente', 8),
('Supervisor', 6),
('Empleado', 4),
('Practicante', 2);

-- Insertar empleados
INSERT INTO empleado (nombre, direccion, telefono, correo, fecha_inicio, salario, fecha_nac, contrasena, id_tipo_empleado) VALUES
('Juan Pérez', 'Calle 123, Ciudad A', '1234567890', 'juan.perez@email.com', '2023-01-15', 50000.00, '1990-05-20', 'password123', 1),
('María García', 'Av. Principal 456, Ciudad B', '0987654321', 'maria.garcia@email.com', '2023-02-01', 45000.00, '1992-08-10', 'password456', 2),
('Carlos López', 'Plaza Central 789, Ciudad C', '5555555555', 'carlos.lopez@email.com', '2023-03-15', 40000.00, '1988-12-05', 'password789', 3),
('Ana Martínez', 'Ruta 101 KM 1, Ciudad D', '4444444444', 'ana.martinez@email.com', '2023-04-01', 38000.00, '1995-03-25', 'passwordabc', 4),
('Pedro Sánchez', 'Calle Nueva 321, Ciudad E', '3333333333', 'pedro.sanchez@email.com', '2023-05-15', 35000.00, '1993-07-15', 'passworddef', 5);

-- Insertar proyectos
INSERT INTO proyecto (nombre, descripcion, fecha_inicio, fecha_fin) VALUES
('Sistema de Ventas', 'Desarrollo de sistema de gestión de ventas', '2023-01-01', '2023-12-31'),
('App Móvil', 'Desarrollo de aplicación móvil corporativa', '2023-03-01', '2023-12-31'),
('Migración de Base de Datos', 'Migración del sistema legacy a nueva plataforma', '2023-06-01', '2023-12-31'),
('Implementación CRM', 'Implementación de sistema CRM', '2023-04-01', '2023-12-31'),
('Actualización Sistemas', 'Actualización de sistemas internos', '2023-05-01', '2023-12-31');

-- Insertar asignaciones proyecto-empleado
INSERT INTO proyectoEmpleado (Id_proyecto, Id_empleado) VALUES
(1, 1), (1, 2), (1, 3),
(2, 2), (2, 4),
(3, 1), (3, 3), (3, 5),
(4, 2), (4, 4),
(5, 1), (5, 5);

-- Insertar registros de tiempo
INSERT INTO registroTiempo (Id_pro_empleado, horas_trabajadas, fecha) VALUES
(1, 8.0, '2023-06-01'),
(2, 7.5, '2023-06-01'),
(3, 6.0, '2023-06-01'),
(4, 8.0, '2023-06-01'),
(5, 7.0, '2023-06-01');

-- Insertar departamentos
INSERT INTO departamento (Nombre, Telefono) VALUES
('Desarrollo', '1111111111'),
('Recursos Humanos', '2222222222'),
('Marketing', '3333333333'),
('Ventas', '4444444444'),
('Administración', '5555555555');

-- Insertar asignaciones departamento-empleado
INSERT INTO departamentoEmpleado (Id_departamento, Id_empleado) VALUES
(1, 1), (1, 3),
(2, 2),
(3, 4),
(4, 5);

-- Insertar informes
INSERT INTO informe (Nombre_informe, Fecha_creacion, Id_empleado, Estado_informe) VALUES
('Informe Mensual de Ventas', '2023-06-01', 1, 'Completado'),
('Informe de Recursos Humanos', '2023-06-01', 2, 'En Proceso'),
('Reporte de Desarrollo', '2023-06-01', 3, 'Pendiente'),
('Informe de Marketing', '2023-06-01', 4, 'Completado'),
('Reporte de Administración', '2023-06-01', 5, 'En Revisión');

-- Insertar módulos
INSERT INTO modulos (Nombre, Nivel_requerido) VALUES
('Gestión de Empleados', 8),
('Gestión de Proyectos', 6),
('Registro de Tiempo', 4),
('Informes', 6),
('Configuración del Sistema', 10);

-- Insertar registros de accesos
INSERT INTO Accesos (Id_modulo, Id_tipo_empleado, Exitoso) VALUES
(1, 1, TRUE),
(2, 2, TRUE),
(3, 3, TRUE),
(4, 4, FALSE),
(5, 5, FALSE);