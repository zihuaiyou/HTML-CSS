from flask import Flask,request

app = Flask(__name__)
# 当前url既可以支持个体请求也可以支持post请求，如果不写只能支持get请求
@app.route('/index/',methods=['GET','POST'])
def index():
    print(request.form) # 获取form表单提交过来的普通键值对，非文件数据（加name属性的数据）

    file_obj = request.files.get('myfile')
    print(file_obj.name)
    file_obj.save(file_obj.name)
    return 'OK'
app.run()