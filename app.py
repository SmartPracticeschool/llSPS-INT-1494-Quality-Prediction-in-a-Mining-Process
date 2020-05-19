    # -*- coding: utf-8 -*-
    """
    Created on Mon May 18 14:34:11 2020
    
    @author: Hari
    """
    
    from flask import Flask,render_template,request
    import pickle
    import numpy as np
    
    model = pickle.load(open('qualityPrediction.pkl', 'rb'))
    
    app = Flask(__name__)
    
    @app.route('/')
    def helloworld():
        return render_template("frontend code.html")
    
    @app.route('/login', methods = ['POST'])
    def login():
        iron = request.form['iron%']
        silica = request.form['Silicafeed%']
        starch = request.form['Sf%']
        amina = request.form['af%']
        orepulp = request.form['of%']
        orepulpdensity = request.form['od']
        fl4 = request.form['fl4']
        fl5 = request.form['fl5']
        fl6 = request.form['fl6']
        fl7 = request.form['fl7']
        fle1 = request.form['fle1']
        fle2 = request.form['fle2']
        fle3 = request.form['fle3']
        fle4 = request.form['fle4']
        fle5 = request.form['fle5']
        fle6 = request.form['fle6']
        fle7 = request.form['fle7']
        
        total= [[float(iron),float(silica),float(starch),float(amina),float(orepulp),float(orepulpdensity), float(fl4), float(fl5), float(fl6), float(fl7), float(fel1), float(fel2), float(fel3), float(fel4),float(fel5), float(fel6), float(fel7)]]
        y_pred = model.predict(np.array(total))
        return render_template("frontend code.html" , showcase = y_pred)
    
    if (__name__ == '__main__'):
        app.run(debug = False)
        
    
        
        
    
