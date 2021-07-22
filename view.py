import eel
import desktop
import search

app_name="html"
end_point="index.html"
size=(700,600)

@ eel.expose
#def python_function2(word):
#    result = word
#    eel.view_log_js(f"Hello")
def get_kimetsu_search(word,csv_file,add_flg):
    result = search.kimetsu_search(word,csv_file,add_flg)
    eel.view_log_js(result)

desktop.start(app_name,end_point,size)
#desktop.start(size=size,appName=app_name,endPoint=end_point)