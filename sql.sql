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

-- Volcando estructura para tabla idgs1004_medicard.insumos
CREATE TABLE IF NOT EXISTS `insumos` (
  `id_insumo` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(32) DEFAULT NULL,
  `cantidad` int DEFAULT NULL,
  `cantidad_min` int DEFAULT NULL,
  `caducidad` json DEFAULT NULL,
  PRIMARY KEY (`id_insumo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla idgs1004_medicard.insumos: ~0 rows (aproximadamente)

-- Volcando estructura para tabla idgs1004_medicard.proveedores
CREATE TABLE IF NOT EXISTS `proveedores` (
  `id_proveedor` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(32) DEFAULT NULL,
  `correo` varchar(32) DEFAULT NULL,
  `telefono` varchar(10) DEFAULT NULL,
  `direccion` json DEFAULT NULL,
  PRIMARY KEY (`id_proveedor`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla idgs1004_medicard.proveedores: ~0 rows (aproximadamente)

-- Volcando estructura para procedimiento idgs1004_medicard.p_medicamentos_select
DELIMITER //
CREATE PROCEDURE `p_medicamentos_select`()
BEGIN	
	(SELECT * FROM tbl_medicamentos);

    
END//
DELIMITER ;

-- Volcando estructura para tabla idgs1004_medicard.tbl_horarios
CREATE TABLE IF NOT EXISTS `tbl_horarios` (
  `id_horario` int NOT NULL AUTO_INCREMENT,
  `fk_id_tratamiento` int DEFAULT NULL,
  `medicina_tomada` bit(1) DEFAULT NULL,
  `fecha` datetime DEFAULT NULL,
  PRIMARY KEY (`id_horario`),
  KEY `FK_tbl_horario_tbl_tratamientos` (`fk_id_tratamiento`),
  CONSTRAINT `FK_tbl_horario_tbl_tratamientos` FOREIGN KEY (`fk_id_tratamiento`) REFERENCES `tbl_tratamientos` (`id_tratamiento`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla idgs1004_medicard.tbl_horarios: ~2 rows (aproximadamente)
INSERT INTO `tbl_horarios` (`id_horario`, `fk_id_tratamiento`, `medicina_tomada`, `fecha`) VALUES
	(1, 1, b'0', '2023-10-18 18:02:38'),
	(2, 1, b'0', '2023-10-18 18:06:43');

-- Volcando estructura para tabla idgs1004_medicard.tbl_medicamentos
CREATE TABLE IF NOT EXISTS `tbl_medicamentos` (
  `id_medicamento` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `fabricante` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  PRIMARY KEY (`id_medicamento`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla idgs1004_medicard.tbl_medicamentos: ~3 rows (aproximadamente)
INSERT INTO `tbl_medicamentos` (`id_medicamento`, `nombre`, `fabricante`) VALUES
	(1, 'aspirina', 'fizzer'),
	(2, 'paracetamol', 'similares'),
	(3, 'pepto bismol', 'Procter & Gamble Company');

-- Volcando estructura para tabla idgs1004_medicard.tbl_tratamientos
CREATE TABLE IF NOT EXISTS `tbl_tratamientos` (
  `id_tratamiento` int NOT NULL AUTO_INCREMENT,
  `fk_id_usuario` int DEFAULT NULL,
  `fk_id_medicamento` int DEFAULT NULL,
  `precio` int DEFAULT NULL,
  `periodo_en_horas` int DEFAULT NULL,
  `fecha_inicio` date DEFAULT NULL,
  `fecha_final` date DEFAULT NULL,
  PRIMARY KEY (`id_tratamiento`),
  KEY `FK_tbl_tratamiento_tbl_usuarios` (`fk_id_usuario`),
  KEY `FK_tbl_tratamiento_tbl_medicamentos` (`fk_id_medicamento`),
  CONSTRAINT `FK_tbl_tratamiento_tbl_medicamentos` FOREIGN KEY (`fk_id_medicamento`) REFERENCES `tbl_medicamentos` (`id_medicamento`),
  CONSTRAINT `FK_tbl_tratamiento_tbl_usuarios` FOREIGN KEY (`fk_id_usuario`) REFERENCES `tbl_usuarios` (`id_usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla idgs1004_medicard.tbl_tratamientos: ~1 rows (aproximadamente)
INSERT INTO `tbl_tratamientos` (`id_tratamiento`, `fk_id_usuario`, `fk_id_medicamento`, `precio`, `periodo_en_horas`, `fecha_inicio`, `fecha_final`) VALUES
	(1, 1, 1, 1, 4, '2023-09-13', NULL);

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
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla idgs1004_medicard.tbl_usuarios: ~3 rows (aproximadamente)
INSERT INTO `tbl_usuarios` (`id_usuario`, `nombre`, `apellidoP`, `apellidoM`, `correo`, `contrasena`, `rol`) VALUES
	(4, 'juan jose', 'martinez', 'lopez', 'juan@gmail.com', 'sha256$J3TegcnZXhKZIPGq$af0f03d2cecf815aa684b043fba7996ec239907182040e9d95410492a409660f', 'comun'),
	(20, 'juan jose de jesus', 'estrada', 'gasca', 'juan2@gmail.com', 'sha256$IKJnWYMH7lPIjku9$6be2958e49f4f1d8e709ff79d5b8b539943570c3be0a82bec1784d03ce8d9165', 'comun'),
	(21, 'juan', 'martinez', 'lopez', 'juan3@gmail.com', 'sha256$gZGEe0xnQx0Y59BD$cbe490bc5d55f69606ec17e49aeb8423c8551e87ffec66fcdc70235510b3ed9f', 'comun');

-- Volcando estructura para tabla idgs1004_medicard.usuarios
CREATE TABLE IF NOT EXISTS `usuarios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(64) DEFAULT NULL,
  `apellidoP` varchar(64) DEFAULT NULL,
  `apellidoM` varchar(64) DEFAULT NULL,
  `correo` varchar(64) DEFAULT NULL,
  `contrasena` varchar(250) DEFAULT NULL,
  `rol` varchar(8) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla idgs1004_medicard.usuarios: ~0 rows (aproximadamente)

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

-- Volcando estructura para tabla idgs1004_medicard.ventas
CREATE TABLE IF NOT EXISTS `ventas` (
  `id_venta` int NOT NULL AUTO_INCREMENT,
  `id_usuario` int DEFAULT NULL,
  `entrega` int DEFAULT NULL,
  PRIMARY KEY (`id_venta`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla idgs1004_medicard.ventas: ~0 rows (aproximadamente)

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
