import psycopg2
def consultar_items(host,database,port,user,pw, schema, table,painel):
    conn = psycopg2.connect(
        host=host,
        port=port,
        dbname= database,
        user=user,
        password=pw
    )
    cs= conn.cursor()

    cs.execute('SELECT count(*) from {esquema}.{tabela}'.format(esquema=schema, tabela=table))

    resultado = cs.fetchone()[0]

    conn.close()
    # print('LOG [FATO]: o resultado de ',painel,' é: ',resultado)
    return resultado
