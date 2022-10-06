import pygsheets



def lendoPlanilha():
    gc=pygsheets.authorize(service_file='./env/key.json')
    CODE = '149FnZjzn4lNqpvSX5PvxBa2Wk-f3SHDFDoZ_CCVgp6M'
    sh=gc.open_by_key(CODE)  
    wks = sh[0]
    return wks.get_all_records()