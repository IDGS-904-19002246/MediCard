from db import get_connection

class ProfesoresP():
    def consultarTodos():
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call ProfesConsultarTodos()')
                resultset = cursor.fetchall()
                for row in resultset:
                    print(row)
                
                return resultset
        except Exception as ex:
            print(ex)
        
    def consultarUno(id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call ProfesConsultarUno(%s)',(id,))
                resultset = cursor.fetchall()
                print(resultset)
                return resultset
        except Exception as ex:
            print(ex)

    def insertar(nom, apa, ema, sue, tel):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    'call ProfesInsertar(%s,%s,%s,%s,%s)',
                    (nom, apa, ema, sue, tel))
                connection.commit()
                connection.close()
                return 'ok'
        except Exception as ex:
            print(ex)
    
    def delete(id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call ProfesBorrar(%s)',(id,))
                connection.commit()
                connection.close()
                return 'ok'
        except Exception as ex:
            print(ex)

    def editar(id,nom, apa, ema, sue, tel):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    'call ProfesEditar(%s,%s,%s,%s,%s,%s)',
                    (id, nom, apa, ema, sue, tel))
                connection.commit()
                connection.close()
                return 'ok'
        except Exception as ex:
            print(ex)





# CONSULTAR
# try:
#     connection = get_connection()
#     with connection.cursor() as cursor:
#         cursor.execute('call ConsultarAlumnosTodo()')
#         resultset = cursor.fetchall()
#         for row in resultset:
#             print(row)
# except Exception as ex:
#     print(ex)

# CONSULTA UNO
# try:
#     connection = get_connection()
#     with connection.cursor() as cursor:
#         #ESTO ES PA QUE LO AGARRE COMO TUPLA (1,)
#         cursor.execute('call ConsultarAlumnoUno(%s)',(1,))
#         resultset = cursor.fetchall()
#         print(resultset)
# except Exception as ex:
#     print(ex)

# # INSERTAR UNO
# try:
#     connection = get_connection()
#     with connection.cursor() as cursor:
#         cursor.execute(
#               'call InsertarAlumno(%s,%s,%s)',
#               ('juan','Lopez','lopez@gmail.com'))
#         connection.commit()
#         connection.close()
#         print('si se pudo')
# except Exception as ex:
#     print(ex)



# ALUMNOS SQML ALCHQMY
# MAESTROS PROCEDIMIENTOS (5 campos)