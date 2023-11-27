SELECT
	t.id_tratamiento,
	m.nombre AS medicina,
	(
		SELECT JSON_ARRAYAGG(
			JSON_OBJECT(
				'id_horario',h.id_horario,
				'fecha', DATE_FORMAT(h.fecha, '%Y-%m-%d %T' ),
				'medicina_tomada',h.medicina_tomada
			)
			
		) FROM tbl_horarios AS h
		WHERE h.fk_id_tratamiento = t.id_tratamiento
	) AS horarios
	
FROM tbl_tratamientos AS t
INNER JOIN tbl_medicamentos AS m ON t.fk_id_medicamento = m.id_medicamento

WHERE t.id_tratamiento = 1;



SELECT 
	IFNULL(g.id_grupo,0) grupo_id,
	IFNULL(g.nombre,'Sin grupo') grupo_nombre,
	IFNULL(g.tema,'Sin Tema') grupo_tema,
	f_getgrupos(g.id_grupo) AS tratamientos
--	GROUP_CONCAT(t.fk_id_grupo)
FROM tbl_grupos g
right JOIN tbl_tratamientos t ON t.fk_id_grupo = g.id_grupo
WHERE t.fk_id_usuario = 4
GROUP BY g.id_grupo;



SELECT
	t.id_tratamiento,
	IFNULL (t.fk_id_grupo, 0) AS id_grupo,
	IFNULL (g.nombre, 'Sin Grupo') AS grupo

	
FROM tbl_tratamientos t
left JOIN tbl_grupos g ON t.fk_id_grupo = g.id_grupo
WHERE t.fk_id_usuario = 4;