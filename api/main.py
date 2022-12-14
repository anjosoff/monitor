from flask import Flask, make_response,render_template

from datetime import date, datetime
import consulta_item, consulta_atualizacao, ler_planilha


now=datetime.now()
now=format(now,'%d/%m/%Y %H:%M:%S')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.errorhandler(404)
def error_404(error):
    return make_response(render_template('404.html'),404)

@app.route('/v1/consultar', methods=['GET'])
def monitor():
    print(f'[{now}] LOG [API]: REQUISIÇÃO EM ANDAMENTO')
    dados=ler_planilha.lendoPlanilha()
    result=[]
    for linha in dados[1:]:
        try:
            host = linha['host']         
            porta= linha['porta']
            banco= linha['database']
            usuario= linha['usuario']
            senha= linha['senha']
            esquema= linha['schema']
            tabela= linha['tabela']
            painel= linha['painel']
            projeto = linha['projeto']
            subprojeto = linha['sub_projeto']
            row_atualizacao=linha['row_atualizacao']
            tabela_atualizacao=linha['tabela_atualizacao']
            link_painel=linha['link_painel']
            items = consulta_item.consultar_items(host,banco,porta,usuario,senha,esquema,tabela,painel)
            atualizacao = consulta_atualizacao.consultar_atualizacao(host,banco,porta,usuario,senha,esquema,row_atualizacao,tabela_atualizacao,painel)
            atualizacao=format(atualizacao,'%d/%m/%Y')
            today=date.today()
            today=format(today,'%d/%m/%Y')
            if items !='0':
                if atualizacao == today:
                    items= str(items)
                    atualizacao=str(atualizacao)
                    result.append({'painel':painel,'projeto':projeto,'sub_projeto':subprojeto,'ultima_atualizacao':atualizacao,'situacao':'Ok','items':items, 'link_painel':link_painel})
                else:
                    result.append({'painel':painel,'projeto':projeto,'sub_projeto':subprojeto,'ultima_atualizacao':atualizacao,'situacao':'Desatualizado','items':items, 'link_painel':link_painel})
            else:
                if atualizacao == today:
                    result.append({'painel':painel,'items':'Não há items','ultima_atualizacao':atualizacao,'situacao':'Ok', 'link_painel':link_painel})
                else:
                    result.append({'painel':painel,'items':'Não há items','ultima_atualizacao':atualizacao,'situacao':'Desatualizado', 'link_painel':link_painel})
            
        except Exception as e2:
            e2=str(e2)     
            print(f'[{now}] LOG [API - ERRO]: ',e2)    
            result.append({'painel':painel,'projeto':projeto,'sub_projeto':subprojeto,'items':items,'situacao':'Error'})
    print(f'[{now}] LOG [API]: REQUISIÇÃO CONCLUÍDA')
    return make_response(result)

@app.route('/v1/consultar')
def consultar():
    return render_template('home.html')




if __name__ == '__main__':
    app.run(host='localhost', port=5000)
    