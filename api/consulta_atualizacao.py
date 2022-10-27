import psycopg2
def consultar_atualizacao(host,database,port,user,pw, schema,row_atualizacao,tabela_atualizacao):
    conn = psycopg2.connect(
        host=host,
        port=port,
        dbname= database,
        user=user,
        password=pw
    )
    cs= conn.cursor()

    cs.execute('SELECT MAX({row_atualizacao}) FROM {esquema}.{tabela_atualizacao}'.format(esquema=schema,row_atualizacao=row_atualizacao,tabela_atualizacao=tabela_atualizacao))

    resultado = cs.fetchone()[0]
    
    conn.close()
    return resultado
