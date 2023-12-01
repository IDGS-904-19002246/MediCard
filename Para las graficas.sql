SELECT 
	CONCAT(
		'#',m.id_medicamento,' ',
		m.nombre
	) nom,
	(	SELECT COUNT(*) FROM tbl_tratamientos t
		WHERE t.fk_id_medicamento = m.id_medicamento
		AND '2023-10-00' BETWEEN t.fecha_inicio AND t.fecha_final
	)
	cantidad		
FROM tbl_medicamentos m
ORDER BY cantidad DESC
LIMIT 7;