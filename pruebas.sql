SELECT 
m.nombre
FROM tbl_medicamentos AS m
 
inner JOIN tbl_imagenes AS i ON  m.id_medicamento = i.fk_id_medicamento
group BY i.url asc
;

SELECT i.url FROM tbl_imagenes AS i GROUP BY i.fk_id_medicamento;

SELECT * FROM tbl_profeciones;
SELECT*FROM receta;