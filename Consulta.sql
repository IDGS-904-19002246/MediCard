SELECT
	JSON_ARRAYAGG(JSON_OBJECT(
     'id_tratamiento', t.id_tratamiento,
     'medicina', m.nombre,
     'horarios',(
     SELECT
	  		JSON_ARRAYAGG(JSON_OBJECT(
	  		'id_horario',h.id_horario,
	  		'fecha',DATE_FORMAT(h.fecha, '%Y-%m-%d %T' ),
	  		'medicina_tomada',h.medicina_tomada
			)) AS d FROM tbl_horarios h WHERE h.fk_id_tratamiento = t.id_tratamiento
		  
			)
	)) AS f
	
	FROM tbl_tratamientos AS t
	INNER JOIN tbl_medicamentos AS m ON t.fk_id_medicamento = m.id_medicamento
	WHERE t.fk_id_grupo = 1;
	
	
	
SELECT
    JSON_ARRAYAGG(JSON_OBJECT(
        'id_tratamiento', t.id_tratamiento,
        'medicina', m.nombre,
        'lista', JSON_ARRAY(JSON_OBJECT(
					'id_horario','h',
					'fecha','f',
					'medicina_tomada','m'
			))
    )) AS resultado
FROM tbl_tratamientos AS t
INNER JOIN tbl_medicamentos AS m ON t.fk_id_medicamento = m.id_medicamento
WHERE t.fk_id_grupo = 1;