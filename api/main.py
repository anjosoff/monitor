from flask import Flask, make_response, jsonify,request,render_template
import pygsheets
import pandas as pd
from flask_swagger_ui import get_swaggerui_blueprint
import consulta,ler_planilha

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
            resultado = consulta.consultar(host,banco,porta,usuario,senha,esquema,tabela)
            resultado= str(resultado)
            if resultado !='0':
                result.append({'painel':painel,'projeto':projeto,'sub_projeto':subprojeto,'items':resultado,'status':True})
            else:
                result.append({'painel':painel,'items':resultado,'status':False})
        except Exception as e2:
            e2=str(e2)     
            print(e2)    
            result.append({'painel':painel,'projeto':projeto,'sub_projeto':subprojeto,'status':False,'reason':e2})
    return make_response(result)
# @app.route('/v1/paineis', methods=['GET'])
# def get_paineis():
#     gc=pygsheets.authorize(service_file='./env/key.json')
#     CODE = '149FnZjzn4lNqpvSX5PvxBa2Wk-f3SHDFDoZ_CCVgp6M'
#     sh=gc.open_by_key(CODE)  
#     wks = sh[0]
#     data=wks.get_all_records()
#     return make_response( 
#             jsonify(data)
#          ) 
   
if __name__ == '__main__':
    app.run()


