INSERT INTO tipoEmpleado (Tipo, Permiso) VALUES
('Administrador', 'Total'),
('Desarrollador', 'Parcial'),
('Analista', 'Básico');

INSERT INTO empleado (nombre, direccion, telefono, correo, fecha_inicio, salario, fecha_nac, contrasena, id_tipo_empleado) VALUES
('Juan Pérez', 'Calle 123, Ciudad', '123456789', 'juan@example.com', '2023-01-15', 50000.00, '1990-05-20', 'contraseña123', 1),
('Ana García', 'Avenida 456, Ciudad', '987654321', 'ana@example.com', '2023-02-01', 45000.00, '1992-08-10', 'contraseña456', 2);

INSERT INTO proyecto (nombre, descripcion, fecha_inicio, fecha_fin) VALUES
('Proyecto A', 'Descripción del Proyecto A', '2023-03-01', '2023-12-31'),
('Proyecto B', 'Descripción del Proyecto B', '2023-04-15', '2024-04-14');

INSERT INTO proyectoEmpleado (Id_proyecto, Id_empleado) VALUES
(1, 1),
(1, 2),
(2, 2);

INSERT INTO registroTiempo (Id_pro_empleado, horas_trabajadas, fecha) VALUES
(1, 8, '2023-05-01'),
(2, 7, '2023-05-01'),
(3, 6, '2023-05-01');

INSERT INTO departamento (Nombre, Telefono) VALUES
('Desarrollo', '111222333'),
('Recursos Humanos', '444555666');

INSERT INTO departamentoEmpleado (Id_departamento, Id_empleado) VALUES
(1, 1),
(1, 2),
(2, 2);

INSERT INTO informe (Nombre_informe, Fecha_creacion, Id_empleado, Estado_informe) VALUES
('Informe Proyecto A', '2023-05-15', 1, 'Completado'),
('Informe Mensual RH', '2023-05-31', 2, 'En proceso');

INSERT INTO modulos (Nombre, Nivel_requerido) VALUES
('Gestión de Proyectos', 2),
('Administración de Usuarios', 3),
('Reportes', 1);

INSERT INTO Accesos (Id_modulo, Id_tipo_empleado) VALUES
(1, 1),
(1, 2),
(2, 1),
(3, 1),
(3, 2),
(3, 3);