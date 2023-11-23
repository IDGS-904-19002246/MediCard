-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         8.0.30 - MySQL Community Server - GPL
-- SO del servidor:              Win64
-- HeidiSQL Versión:             12.5.0.6677
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para idgs1004_medicard
CREATE DATABASE IF NOT EXISTS `idgs1004_medicard` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `idgs1004_medicard`;

-- Volcando estructura para procedimiento idgs1004_medicard.p_horarios_insertAll
DELIMITER //
CREATE PROCEDURE `p_horarios_insertAll`(
	IN `inicio` DATETIME,
	IN `final` DATETIME,
	IN `n_horas` INT
)
BEGIN
	DECLARE c_date DATETiME;
   DECLARE c_hour INT;
   DECLARE fk_id INT;
--	SET c_date = CONCAT(inicio , ' ', hora_inicio);
	SET c_date = inicio;
	SET c_hour = 0;
--	SET fk_id = (SELECT LAST_INSERT_ID() AS ultimo FROM tbl_tratamientos LIMIT 1);
	SET fk_id = (SELECT MAX(id_tratamiento) FROM tbl_tratamientos);
	
	while c_date <= final DO
		
		SET c_date = DATE_ADD(c_date, INTERVAL n_horas HOUR);
		
--		SELECT fk_id, 0, c_date;
--		--------------------------------------------------		
		
		INSERT INTO tbl_horarios
			(fk_id_tratamiento,medicina_tomada,fecha)
		VALUES(
			fk_id,0, c_date
		);
--		--------------------------------------------------
	END WHILE;
	
	
END//
DELIMITER ;

-- Volcando estructura para procedimiento idgs1004_medicard.p_imagen_update
DELIMITER //
CREATE PROCEDURE `p_imagen_update`(
	IN `id` INT,
	IN `img` VARCHAR(50)
)
BEGIN
	DELETE FROM tbl_imagenes WHERE fk_id_medicamento = id;

	INSERT INTO tbl_imagenes(fk_id_medicamento,url)VALUES(id,img);
END//
DELIMITER ;

-- Volcando estructura para procedimiento idgs1004_medicard.p_medicamentos_insert
DELIMITER //
CREATE PROCEDURE `p_medicamentos_insert`(
	IN `nom` VARCHAR(64),
	IN `fab` VARCHAR(64),
	IN `can` INT,
	IN `med` VARCHAR(16),
	IN `img` VARCHAR(16),
	IN `tip` VARCHAR(32)
)
BEGIN

	INSERT INTO tbl_medicamentos (
		nombre,fabricante,cantidad,medida,estado,fk_id_tipo
	)VALUES(
		nom,fab,can,med,'Verificado',tip
	);
	
	SET @ultimo_id = LAST_INSERT_ID();
	INSERT INTO tbl_imagenes (
		fk_id_medicamento,url
	)VALUES(
		@ultimo_id,img
	);
	
END//
DELIMITER ;

-- Volcando estructura para procedimiento idgs1004_medicard.p_medicamentos_insertApi
DELIMITER //
CREATE PROCEDURE `p_medicamentos_insertApi`(
	IN `nom` VARCHAR(64),
	IN `fab` VARCHAR(64),
	IN `can` INT,
	IN `med` VARCHAR(16),
	IN `img` VARCHAR(16),
	IN `tip` VARCHAR(32)
)
BEGIN

	INSERT INTO tbl_medicamentos (
		nombre,fabricante,cantidad,medida,estado,fk_id_tipo
	)VALUES(
		nom,fab,can,med,'Por Verificar',tip
	);
	
	SET @ultimo_id = LAST_INSERT_ID();
	INSERT INTO tbl_imagenes (
		fk_id_medicamento,url
	)VALUES(
		@ultimo_id,img
	);
	
END//
DELIMITER ;

-- Volcando estructura para procedimiento idgs1004_medicard.p_medicamentos_select
DELIMITER //
CREATE PROCEDURE `p_medicamentos_select`()
BEGIN	
	-- (SELECT * FROM tbl_medicamentos);

	SELECT
		m.id_medicamento,
		m.nombre,
		m.fabricante,
		m.cantidad,
		m.medida,
		m.estado,
		(
			SELECT JSON_ARRAYAGG(i.url) FROM tbl_imagenes AS i
			WHERE i.fk_id_medicamento = m.id_medicamento
		)AS imagenes,
		t.nombre AS tipo

	   FROM tbl_medicamentos m 
	   INNER JOIN tbl_tipos_medicina t on m.fk_id_tipo = t.id_tipo
		WHERE m.estado != 'borrado';
    
END//
DELIMITER ;

-- Volcando estructura para procedimiento idgs1004_medicard.p_medicamentos_selectOne
DELIMITER //
CREATE PROCEDURE `p_medicamentos_selectOne`(
	IN `id` INT
)
BEGIN
	SELECT
		m.id_medicamento,
		m.nombre,
		m.fabricante,
		m.cantidad,
		m.medida,
		m.estado,
		(
			SELECT JSON_ARRAYAGG(i.url) FROM tbl_imagenes AS i
			WHERE i.fk_id_medicamento = m.id_medicamento
		)AS imagenes,
		m.fk_id_tipo

	   FROM tbl_medicamentos m
		WHERE m.id_medicamento = id;
END//
DELIMITER ;

-- Volcando estructura para procedimiento idgs1004_medicard.p_medicamentos_update
DELIMITER //
CREATE PROCEDURE `p_medicamentos_update`(
	IN `nom` VARCHAR(50),
	IN `fab` VARCHAR(50),
	IN `can` INT,
	IN `med` VARCHAR(16),
	IN `est` VARCHAR(16),
	IN `tip` INT,
	IN `id` INT
)
BEGIN

	UPDATE tbl_medicamentos set
	nombre = nom,
	fabricante = fab,
	cantidad=can,
	medida = med,
	estado = est,
	fk_id_tipo = tip
	WHERE id_medicamento = id;
END//
DELIMITER ;

-- Volcando estructura para procedimiento idgs1004_medicard.p_usuarios_select
DELIMITER //
CREATE PROCEDURE `p_usuarios_select`()
BEGIN

	SELECT id_usuario, concat(nombre,' ',apellidoP,' ',apellidoM) AS 'nom', correo, rol FROM tbl_usuarios WHERE rol = 'ADMIN';
 	SELECT id_usuario, concat(nombre,' ',apellidoP,' ',apellidoM) AS 'nom', correo, rol FROM tbl_usuarios WHERE rol = 'EMPLE';
	SELECT id_usuario, concat(nombre,' ',apellidoP,' ',apellidoM) AS 'nom', correo, rol FROM tbl_usuarios WHERE rol = 'COMUN';
	SELECT id_usuario, concat(nombre,' ',apellidoP,' ',apellidoM) AS 'nom', correo, rol FROM tbl_usuarios WHERE rol = 'BANN';
	
END//
DELIMITER ;

-- Volcando estructura para procedimiento idgs1004_medicard.p_usuarios_selectOneData
DELIMITER //
CREATE PROCEDURE `p_usuarios_selectOneData`(
	IN `id` INT
)
BEGIN

SELECT
	t.id_tratamiento,
	CONCAT(m.nombre ,' (',tipo.nombre,')') as medicina,
	DATE_FORMAT(t.fecha_inicio, '%M %e, de %Y') AS inicio,
	DATE_FORMAT(t.fecha_final, '%M %e, de %Y') AS fin,
	t.precio,

	(SELECT JSON_ARRAYAGG(
	CONCAT('{ "fecha": "', DATE_FORMAT(h.fecha, '%M %e, de %Y (%l:%i %p)'),'", "medicina_tomada": "', medicina_tomada, '" }')
--		CONCAT("{'medicina_tomada':",h.medicina_tomada,",'fecha':",h.fecha,"}")

	)FROM tbl_horarios AS h WHERE h.fk_id_tratamiento = t.id_tratamiento) AS horarios

FROM tbl_tratamientos t
INNER JOIN tbl_medicamentos m ON t.fk_id_medicamento = m.id_medicamento
INNER JOIN tbl_tipos_medicina tipo ON  m.fk_id_tipo = tipo.id_tipo
WHERE t.fk_id_usuario = id;

END//
DELIMITER ;

-- Volcando estructura para procedimiento idgs1004_medicard.p_usuarios_updatePass
DELIMITER //
CREATE PROCEDURE `p_usuarios_updatePass`(
	IN `id` INT,
	IN `new_pass` VARCHAR(250)
)
BEGIN
	UPDATE tbl_usuarios AS u
		SET u.contrasena = new_pass
		WHERE u.id_usuario = id;
END//
DELIMITER ;

-- Volcando estructura para procedimiento idgs1004_medicard.p_usuarios_updateRol
DELIMITER //
CREATE PROCEDURE `p_usuarios_updateRol`(
	IN `id` INT,
	IN `rol` VARCHAR(8)
)
BEGIN
	
	UPDATE tbl_usuarios AS u
		SET u.rol = rol
		WHERE u.id_usuario = id;
END//
DELIMITER ;

-- Volcando estructura para tabla idgs1004_medicard.tbl_grupos
CREATE TABLE IF NOT EXISTS `tbl_grupos` (
  `id_grupo` int NOT NULL AUTO_INCREMENT,
  `fk_id_usuario` int DEFAULT NULL,
  `nombre` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `tema` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`id_grupo`),
  KEY `FK_tbl_grupos_tbl_usuarios` (`fk_id_usuario`),
  CONSTRAINT `FK_tbl_grupos_tbl_usuarios` FOREIGN KEY (`fk_id_usuario`) REFERENCES `tbl_usuarios` (`id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla idgs1004_medicard.tbl_grupos: ~0 rows (aproximadamente)
INSERT INTO `tbl_grupos` (`id_grupo`, `fk_id_usuario`, `nombre`, `tema`) VALUES
	(1, 4, 'ezquizofrenia', 'blanquito'),
	(2, 4, 'disfuncion erectil', 'moo');

-- Volcando estructura para tabla idgs1004_medicard.tbl_horarios
CREATE TABLE IF NOT EXISTS `tbl_horarios` (
  `id_horario` int NOT NULL AUTO_INCREMENT,
  `fk_id_tratamiento` int DEFAULT NULL,
  `medicina_tomada` int DEFAULT NULL,
  `fecha` datetime DEFAULT NULL,
  PRIMARY KEY (`id_horario`),
  KEY `FK_tbl_horario_tbl_tratamientos` (`fk_id_tratamiento`),
  CONSTRAINT `FK_tbl_horario_tbl_tratamientos` FOREIGN KEY (`fk_id_tratamiento`) REFERENCES `tbl_tratamientos` (`id_tratamiento`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla idgs1004_medicard.tbl_horarios: ~16 rows (aproximadamente)
INSERT INTO `tbl_horarios` (`id_horario`, `fk_id_tratamiento`, `medicina_tomada`, `fecha`) VALUES
	(9, 1, 0, '2023-01-01 05:00:00'),
	(12, 2, 0, '2023-01-01 11:00:00'),
	(13, 3, 0, '2023-01-01 14:00:00'),
	(28, 1, 1, '2023-11-09 12:05:04'),
	(29, 4, 0, '2023-11-09 12:37:18'),
	(30, 4, 2, '2023-11-09 16:00:00'),
	(31, 4, 0, '2023-01-01 05:00:00'),
	(32, 4, 0, '2023-01-01 08:00:00'),
	(33, 4, 0, '2023-01-01 11:00:00'),
	(34, 4, 0, '2023-01-01 14:00:00'),
	(35, 4, 0, '2023-01-01 17:00:00'),
	(36, 4, 0, '2023-01-01 20:00:00'),
	(37, 4, 0, '2023-01-01 23:00:00'),
	(38, 4, 0, '2023-01-02 02:00:00'),
	(39, 4, 0, '2023-01-02 05:00:00'),
	(40, 3, 0, '2023-01-01 05:00:00');

-- Volcando estructura para tabla idgs1004_medicard.tbl_imagenes
CREATE TABLE IF NOT EXISTS `tbl_imagenes` (
  `id_imagen` int NOT NULL AUTO_INCREMENT,
  `fk_id_medicamento` int DEFAULT NULL,
  `url` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`id_imagen`),
  KEY `FK_tbl_imagenes_tbl_medicamentos` (`fk_id_medicamento`),
  CONSTRAINT `FK_tbl_imagenes_tbl_medicamentos` FOREIGN KEY (`fk_id_medicamento`) REFERENCES `tbl_medicamentos` (`id_medicamento`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla idgs1004_medicard.tbl_imagenes: ~8 rows (aproximadamente)
INSERT INTO `tbl_imagenes` (`id_imagen`, `fk_id_medicamento`, `url`) VALUES
	(1, 1, 'url.png'),
	(2, 2, 'url2.png'),
	(3, 3, 'url3.png'),
	(4, 1, 'url.jpg'),
	(14, 1, 'xd'),
	(15, 13, 'juan.jpg'),
	(19, 17, 'producto x.jpeg'),
	(20, 18, 'f.jpg');

-- Volcando estructura para tabla idgs1004_medicard.tbl_medicamentos
CREATE TABLE IF NOT EXISTS `tbl_medicamentos` (
  `id_medicamento` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `fabricante` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `cantidad` int DEFAULT NULL,
  `medida` varchar(16) DEFAULT NULL,
  `estado` varchar(16) DEFAULT NULL,
  `fk_id_tipo` int DEFAULT NULL,
  PRIMARY KEY (`id_medicamento`),
  KEY `FK_tbl_medicamentos_tbl_tipos_medicina` (`fk_id_tipo`),
  CONSTRAINT `FK_tbl_medicamentos_tbl_tipos_medicina` FOREIGN KEY (`fk_id_tipo`) REFERENCES `tbl_tipos_medicina` (`id_tipo`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla idgs1004_medicard.tbl_medicamentos: ~5 rows (aproximadamente)
INSERT INTO `tbl_medicamentos` (`id_medicamento`, `nombre`, `fabricante`, `cantidad`, `medida`, `estado`, `fk_id_tipo`) VALUES
	(1, 'aspirina 2', 'fizzer', 5, 'ml', 'disponibles', 2),
	(2, 'paracetamol', 'similares', 8, 'pastillas', 'disponibles', 3),
	(3, 'pepto bismol', 'Procter y Gamble Company', 250, 'ml', 'disponibles', 2),
	(13, 'Pastilla dia siguiente', 'Prudence', 1, 'ml', 'disponibles', 6),
	(17, 'producto x', 'x', 8, 'píldoras', 'Verificado', 5),
	(18, 'f', 'f', 3, '4', 'Por Verificar', 1);

-- Volcando estructura para tabla idgs1004_medicard.tbl_tipos_medicina
CREATE TABLE IF NOT EXISTS `tbl_tipos_medicina` (
  `id_tipo` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(32) DEFAULT NULL,
  `descripcion` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id_tipo`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla idgs1004_medicard.tbl_tipos_medicina: ~4 rows (aproximadamente)
INSERT INTO `tbl_tipos_medicina` (`id_tipo`, `nombre`, `descripcion`) VALUES
	(1, 'sin categoria', 'no tiene categoria asignada'),
	(2, 'antiviral', 'palos virus'),
	(3, 'antibacterial', 'palas bcterias'),
	(5, 'antiacido', 'pal acido'),
	(6, 'anticonceptivo', 'no globo no fiesta');

-- Volcando estructura para tabla idgs1004_medicard.tbl_tratamientos
CREATE TABLE IF NOT EXISTS `tbl_tratamientos` (
  `id_tratamiento` int NOT NULL AUTO_INCREMENT,
  `fk_id_usuario` int DEFAULT NULL,
  `fk_id_medicamento` int DEFAULT NULL,
  `precio` int DEFAULT NULL,
  `dosis` int DEFAULT NULL,
  `periodo_en_horas` int DEFAULT NULL,
  `fecha_inicio` datetime DEFAULT NULL,
  `fecha_final` datetime DEFAULT NULL,
  `fk_id_grupo` int DEFAULT NULL,
  PRIMARY KEY (`id_tratamiento`),
  KEY `FK_tbl_tratamiento_tbl_usuarios` (`fk_id_usuario`),
  KEY `FK_tbl_tratamiento_tbl_medicamentos` (`fk_id_medicamento`),
  KEY `FK_tbl_tratamientos_tbl_grupos` (`fk_id_grupo`),
  CONSTRAINT `FK_tbl_tratamiento_tbl_medicamentos` FOREIGN KEY (`fk_id_medicamento`) REFERENCES `tbl_medicamentos` (`id_medicamento`),
  CONSTRAINT `FK_tbl_tratamiento_tbl_usuarios` FOREIGN KEY (`fk_id_usuario`) REFERENCES `tbl_usuarios` (`id_usuario`),
  CONSTRAINT `FK_tbl_tratamientos_tbl_grupos` FOREIGN KEY (`fk_id_grupo`) REFERENCES `tbl_grupos` (`id_grupo`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla idgs1004_medicard.tbl_tratamientos: ~4 rows (aproximadamente)
INSERT INTO `tbl_tratamientos` (`id_tratamiento`, `fk_id_usuario`, `fk_id_medicamento`, `precio`, `dosis`, `periodo_en_horas`, `fecha_inicio`, `fecha_final`, `fk_id_grupo`) VALUES
	(1, 4, 1, 1, 2, 4, '2023-09-13 00:00:00', '2023-11-03 00:00:00', 1),
	(2, 4, 1, 2, 2, 2, '2023-11-03 00:00:00', '2023-11-03 00:00:00', 1),
	(3, 22, 1, 2, 2, 2, '2023-11-07 18:37:33', '2023-11-08 18:29:10', NULL),
	(4, 4, 3, 2, 2, 3, '2023-11-09 12:36:22', '2023-11-09 12:36:24', 2);

-- Volcando estructura para tabla idgs1004_medicard.tbl_usuarios
CREATE TABLE IF NOT EXISTS `tbl_usuarios` (
  `id_usuario` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(64) DEFAULT NULL,
  `apellidoP` varchar(64) DEFAULT NULL,
  `apellidoM` varchar(64) DEFAULT NULL,
  `correo` varchar(64) DEFAULT NULL,
  `contrasena` varchar(250) DEFAULT NULL,
  `rol` varchar(8) DEFAULT NULL,
  PRIMARY KEY (`id_usuario`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla idgs1004_medicard.tbl_usuarios: ~4 rows (aproximadamente)
INSERT INTO `tbl_usuarios` (`id_usuario`, `nombre`, `apellidoP`, `apellidoM`, `correo`, `contrasena`, `rol`) VALUES
	(4, 'juan jose', 'martinez', 'lopez', 'juan@gmail.com', 'sha256$J3TegcnZXhKZIPGq$af0f03d2cecf815aa684b043fba7996ec239907182040e9d95410492a409660f', 'COMUN'),
	(20, 'juan jose de jesus', 'estrada', 'gasca', 'juan2@gmail.com', 'sha256$IKJnWYMH7lPIjku9$6be2958e49f4f1d8e709ff79d5b8b539943570c3be0a82bec1784d03ce8d9165', 'ADMIN'),
	(21, 'juan', 'martinez', 'lopez', 'juan3@gmail.com', 'sha256$gZGEe0xnQx0Y59BD$cbe490bc5d55f69606ec17e49aeb8423c8551e87ffec66fcdc70235510b3ed9f', 'ADMIN'),
	(22, 'juan jr', 'lopez', 'martinez', 'juanjr@gmail.com', 'sha256$Ei8lU0rGxv6lxaWn$ddc3e5510955d54ec53fb3ff23a3463074efd9729fedb48a96a7b6682065f720', 'comun');

-- Volcando estructura para procedimiento idgs1004_medicard.usuariosInsert
DELIMITER //
CREATE PROCEDURE `usuariosInsert`(
	IN `nom` VARCHAR(64),
	IN `apeP` VARCHAR(64),
	IN `apeM` VARCHAR(64),
	IN `cor` VARCHAR(50),
	IN `con` VARCHAR(250)
)
BEGIN

	INSERT INTO tbl_usuarios(
		nombre,
		apellidoP,
		apellidoM,
		correo,
		contrasena,
		rol
	) VALUES(
		nom,
		apeP,
		apeM,
		
		cor,
		con,
		'comun'
	);
	
END//
DELIMITER ;

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
