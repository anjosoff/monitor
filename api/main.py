from flask import Flask, make_response,render_template
from datetime import date, datetime
import consulta_item,consulta_atualizacao,ler_planilha

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.errorhandler(404)
def error_404(error):
    return make_response(render_template('404.html'),404)

@app.route('/v1/consultar', methods=['GET'])
def paineis():
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
            items = consulta_item.consultar_items(host,banco,porta,usuario,senha,esquema,tabela)
            atualizacao = consulta_atualizacao.consultar_atualizacao(host,banco,porta,usuario,senha,esquema,row_atualizacao,tabela_atualizacao)
            atualizacao=format(atualizacao,'%d/%m/%Y')
            today=date.today()
            today=format(today,'%d/%m/%Y')
            if items !='0':
                if atualizacao == today:
                    items= str(items)
                    atualizacao=str(atualizacao)
                    result.append({'painel':painel,'projeto':projeto,'sub_projeto':subprojeto,'ultima_atualizacao':atualizacao,'atualizacao':'Atualizado','items':items})
                else:
                    result.append({'painel':painel,'projeto':projeto,'sub_projeto':subprojeto,'ultima_atualizacao':atualizacao,'atualizacao':'Desatualizado','items':items})
            else:
                result.append({'painel':painel,'items':'Não há items','ultima_atualizacao':atualizacao,'atualizacao':atualizacao})
            
        except Exception as e2:
            e2=str(e2)     
            print(e2)    
            result.append({'painel':painel,'projeto':projeto,'sub_projeto':subprojeto,'items':items,'reason':'Ocorreu um erro'})
    return make_response(result)

@app.route('/v1/consultar')
def consultar():
    return render_template('home.html')

if __name__ == '__main__':
    app.run()


