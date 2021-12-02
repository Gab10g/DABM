from flask import Flask,render_template,request,redirect
from flask.globals import request
import os
import random

from werkzeug.utils import secure_filename
from flask.helpers import locked_cached_property
from werkzeug.wrappers import ETagRequestMixin

app = Flask(__name__)

DocAconsultar=0

Nombre=[]
Apellido=[]
Documento=[]
Patologia=[]
RH=[]
email=[]
usuario=[]
password=[]

@app.route('/')
def inicio():
    title="Menu Principal"
    return render_template('menu.html',title=title)

@app.route('/menuFisioterapeuta',methods=["POST"])
def loginFisioterapeuta(): 
    if request.method=="POST":
        usuario=request.form['usuario']
        password=request.form['password']
        resultado=True
        resultado=verificarF(usuario,password)

        if resultado ==True:
            return render_template('menuFisioterapeuta.html')
        else:
            return redirect("/loginFis")
    
def verificarF(usuario,password):
    directorio=os.path.dirname(__file__)        #se abre y lee el archivo de texto de "Fisioterapeutas.cvs"
    nombrearchivo="bd/Fisioterapeutas.csv"
    ruta=os.path.join(directorio,nombrearchivo)

    f= open(ruta,"r")
    lineas=f.readlines()        #leemos las lineas del archivo de texto
    f.close()
    datos=[]                    #lista donde vamos a almacenar cada fila del  archivo de texto
    for l in lineas:
        l=l.replace("\n","")
        l=l.split(";")
        datos.append(l)

    for d in datos:
        if ((d[0]==usuario) and (d[1]==password)):
            return True

@app.route('/menuPaciente',methods=["POST"])
def loginPaciente(): 
    if request.method=="POST":
        usuario=request.form['usuario']
        password=request.form['password']
        resultado=True
        resultado=verificarP(usuario,password)

        if resultado ==True:
            return render_template('menuPaciente.html')
        else:
            return redirect("/loginPas")
    
def verificarP(usuario,password):
    directorio=os.path.dirname(__file__)        #se abre y lee el archivo de texto de "UsuariosPacientes.cvs"
    nombrearchivo="bd/Pacientes.csv"
    ruta=os.path.join(directorio,nombrearchivo)

    f= open(ruta,"r")
    lineas=f.readlines()        #leemos las lineas del archivo de texto
    f.close()
    datos=[]                    #lista donde vamos a almacenar cada fila del  archivo de texto
    for l in lineas:
        l=l.replace("\n","")
        l=l.split(";")
        datos.append(l)

    for d in datos:
        if ((d[6]==usuario) and (d[7]==password)):
            return True

@app.route('/loginPas')
def loginPas():
    return render_template('loginPas.html') 

@app.route('/loginFis')
def loginFis():
    return render_template('loginFis.html') 

@app.route('/RegistrarP')
def RegistrarP():
    return render_template('RegistrarP.html')

@app.route('/GuardarPacientes',methods=["POST"])
def GuardarPacientes():
    global Nombre
    global Apellido
    global Documento
    global Patologia
    global RH
    global email
    global usuario
    global password
    if request.method == "POST":
        Nombre=request.form['NombrePaciente']
        Apellido=request.form['ApellidoPaciente']
        Documento=request.form['Doc']
        Patologia=request.form['Pat']
        RH=request.form['RH']
        email=request.form['email']
        usuario=request.form['username']
        password=request.form['password']
        
        directorio=os.path.dirname(__file__)        #se abre y lee el archivo de texto de "Pacientes.cvs"
        nombrearchivo="bd/pacientes.csv"
        ruta=os.path.join(directorio,nombrearchivo)

        f=open(ruta,"a")
        datos=Nombre+";"+Apellido+";"+Documento+";"+Patologia+";"+RH+";"+email+";"+usuario+";"+password+"\n"
        f.write(datos)
        f.close()
        return render_template('/menuFisioterapeuta.html')

@app.route('/TerapiaAsignada')
def TerapiaAsignada():
    directorio=os.path.dirname(__file__)        #se abre y lee el archivo de texto de "Pacientes.cvs"
    nombrearchivo="bd/Pacientes.csv"
    ruta=os.path.join(directorio,nombrearchivo)

    f= open(ruta,"r")
    lineas=f.readlines()        #leemos las lineas del archivo de texto
    f.close()
    datos=[] 

    for l in lineas:
        l=l.replace("\n","")
        l=l.split(";")
        datos.append(l)

    for d in datos:
        name=d[0]+" "+d[1]
        doc=d[2]
        pat=d[3]

    return render_template('TerapiaAsignada.html',name=name,doc=doc,pat=pat)

@app.route('/GuardarUsuarioP', methods=["POST"])
def GuardarUsuarioP():
    if request.method=="POST":
        

        directorio=os.path.dirname(__file__)        #se abre y lee el archivo de texto de "UsuariosPacientes.cvs"
        nombrearchivo="bd/Pacientes.csv"
        ruta=os.path.join(directorio,nombrearchivo)

        f=open(ruta,"a")
        datos=usuario+";"+password+";"+email+"\n"
        f.write(datos)
        f.close()

        return render_template('menu.html')

@app.route('/Evidencia')
def Evidencia():
    return render_template('Evidencia.html')

@app.route('/Evolucion')
def Evolucion():
    return render_template('Evolucion.html')

@app.route('/GuardarEvolucion',methods=["POST"])
def GuardarEvolucion():
    if request.method=="POST":
        datos=request.form['text']
        name=request.form['Doc']

        directorio=os.path.dirname(__file__)        #se abre y lee el archivo de texto de "UsuariosPacientes.cvs"
        nombrearchivo="bd/"+name+".csv"
        ruta=os.path.join(directorio,nombrearchivo)

        f=open(ruta,"w")
        f.write(datos)
        f.close()

        return render_template('/menuFisioterapeuta.html')

@app.route('/ConsultarEvolucion', methods=["POST"])
def ConsultarEvolucion():
      if request.method=="POST":
        archivo=request.form['Documento']

        directorio=os.path.dirname(__file__)        #se abre y lee el archivo de texto de "UsuariosPacientes.cvs"
        nombrearchivo="bd/"+str(archivo)+".csv"
        ruta=os.path.join(directorio,nombrearchivo)

        f=open(ruta,"r")
        lineas=f.readlines()
        f.close
        
        return render_template('ConsultarEvolucion.html',lineas=lineas)
   

@app.route('/Ej1')
def Ej1():
    return render_template('Ej1.html')

@app.route('/Ej2')
def Ej2():
    return render_template('Ej2.html')

@app.route('/Ej3')
def Ej3():
    return render_template('Ej3.html')

@app.route('/Ej4')
def Ej4():
    return render_template('Ej4.html')

@app.route('/Ej5')
def Ej5():
    return render_template('Ej5.html')

@app.route('/Ej6')
def Ej6():
    return render_template('Ej6.html')

@app.route('/Ej7')
def Ej7():
    return render_template('Ej7.html')

@app.route('/Ej8')
def Ej8():
    return render_template('Ej8.html')

@app.route('/Ej9')
def Ej9():
    return render_template('Ej9.html')

@app.route('/Ej10')
def Ej10():
    return render_template('Ej10.html')

@app.route('/Ej11')
def Ej11():
    return render_template('Ej11.html')

@app.route('/Ej12')
def Ej12():
    return render_template('Ej12.html')

@app.route('/Ej13')
def Ej13():
    return render_template('Ej13.html')

@app.route('/Ej14')
def Ej14():
    return render_template('Ej14.html')

@app.route('/Ej15')
def Ej15():
    return render_template('Ej15.html')

@app.route('/Ej16')
def Ej16():
    return render_template('Ej16.html')

@app.route('/Ej17')
def Ej17():
    return render_template('Ej17.html')

@app.route('/Ej18')
def Ej18():
    return render_template('Ej18.html')

@app.route('/Ej19')
def Ej19():
    return render_template('Ej19.html')

@app.route('/Ej20')
def Ej20():
    return render_template('Ej20.html')

@app.route('/Ej21')
def Ej21():
    return render_template('Ej21.html')

@app.route('/GuardarEvidencias' , methods=["POST"])
def GuardarEvidencias():
    if request.method=="POST":
        Documento =request.form['Documento'] 
        file=request.files['evidencia']
        filename =secure_filename(file.filename)
        extencion = filename.split(".")
        print(extencion)
        file.save(os.path.join("static/evidencias",secure_filename(Documento + "." + extencion[1])))

        return render_template('Evidencia.html')

@app.route('/EvidenciasP')
def EvidenciasP():
    return render_template('EvidenciasP.html')

@app.route('/ConsultarEv', methods=["POST"])
def ConsultarEv():
        global DocAconsultar
        if request.method=="POST":
            DocAconsultar=request.form['Documento']
            res=False
            res=ValidarDoc(DocAconsultar)
            if res == True:
                return redirect('/RevicionDeEvidencias')
            else:
                return render_template('EvidenciasP.html')    

@app.route('/RevicionDeEvidencias')
def RevicionDeEvidencias():
    return render_template('RevicionDeEvidencias.html',Doc=DocAconsultar)

def ValidarDoc(Documento):
    directorio=os.path.dirname(__file__)        #se abre y lee el archivo de texto de "Pacientes.cvs"
    nombrearchivo="bd/Pacientes.csv"
    ruta=os.path.join(directorio,nombrearchivo)

    f= open(ruta,"r")
    lineas=f.readlines()        #leemos las lineas del archivo de texto
    f.close()
    datos=[]                    #lista donde vamos a almacenar cada fila del  archivo de texto
    for l in lineas:
        l=l.replace("\n","")
        l=l.split(";")
        datos.append(l)

    for d in datos:
        if ((d[2]==Documento)):
            print(d[2])
            return True


if __name__=="__main__":
    app.run(debug=True)