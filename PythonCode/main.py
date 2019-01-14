# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 11:23:22 2019

@author: 748418
"""

from flask import Flask, render_template, request, redirect, session, flash
from herois import Herois

app = Flask(__name__)
app.secret_key = 'MeteoroDePegasus'
heroi1 = Herois('Homem-aranha', 'masc', '10')
heroi2 = Herois('Pantera Negra', 'masc', '20')
heroi3 = Herois('Capitã Marvel', 'fem', '40')

lista_herois=[heroi1, heroi2, heroi3]


@app.route('/')
def index():
    return render_template('index.html', title='Heroi', lista=lista_herois)
 
@app.route('/new')
def new():
    if 'usuario_logado' not in session['usuario_logado'] or session['usuario_logado'] == None:
         return redirect('/login')
    return render_template('new.html', title='Cadastro Heroi')

@app.route('/create', methods=['POST'])
def create():
    nome = request.form['nome']
    genero = request.form['genero']
    poder = request.form['poder']
    print(nome, genero, poder)
    lista_herois.append(Herois(nome, genero, poder))
    return redirect('/')

@app.route('/login')
def login():
    return render_template('login.html', title='Login')



@app.route('/auth', methods=['post'])
def auth():
    
    
    lista_usuarios=[]

    usuario=request.form['usuario']
    senha=request.form['senha']
    
    
    while usuario == [A-Z] or [a-z] or [0-9]:
     cont = 0
     lista_user in lista_usuarios:
        print(lista_user)
    
    
    if 'pudinzinho' in request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash('O {} logado. '.format(request.form['usuario']))
        return redirect('/create')
    else:
        flash('Senha e/ou usuario inválidos. Tente novamente!')
        return redirect('/login')
    
    
    
@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    return redirect('/')

    
app.run(debug=True)
