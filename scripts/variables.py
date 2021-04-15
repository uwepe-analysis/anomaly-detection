#!/usr/bin/env python


var_range = {"pxj1": [500,2000],
            "pxj2": [500,2000],
            "pyj1": [500,2000],
            "pyj2": [500,2000],
            "pzj1": [500,2000],
            "pzj2": [500,2000],
            "etaj1": [0, 3],
            "etaj2": [0, 3],
            "phij1": [-2,5],
            "phij2": [-2,5],
            "mj1": [0,600],
            "mj2": [0,600],
            "ej1": [1200,2500],
            "ej2": [1200,2500],
            "tau32j1": [0,1],
            "tau32j2": [0,1],
            "tau21j1": [0,1],
            "tau21j2": [0,1],
            "mjj": [2000, 6000],
            "ejj": [2000, 6000],
           }
var_nbins = {"pxj1": 25,
            "pxj2": 25,
            "pyj1": 25,
            "pyj2": 25,
            "pzj1": 25,
            "pzj2": 25,
            "etaj1": 30,
            "etaj2": 30,
            "phij1": 30,
            "phij2": 30,
            "mj1": 25,
            "mj2": 25,
            "ej1": 30,
            "ej2": 30,
            "tau32j1": 25,
            "tau32j2": 25,
            "tau21j1": 25,
            "tau21j2": 25,
            "mjj": 60,
            "ejj": 50,
            }

var_axis_label = {
            "pxj1": "Leading jet $p_{x}$ [GeV]",
            "pxj2": "Subleading jet $p_{x}$ [GeV]",
            "pyj1": "Leading jet $p_{y}$ [GeV]",
            "pyj2": "Subleading jet $p_{y}$ [GeV]",
            "pzj1": "Leading jet $p_{z}$ [GeV]",
            "pzj2": "Subleading jet $p_{z}$ [GeV]",
            "etaj1": "Leading jet $p_{x}$ [GeV]",
            "etaj2": "Leading jet $\\eta$",
            "phij1": "Subleading jet $\\phi$",
            "phij2": "Leading jet $\\tau_{32}$",
            "mj1": "Leading jet mass [GeV]",
            "mj2": "Subleading jet mass [GeV]",
            "ej1": "Leading jet energy [GeV]",
            "ej2": "Subleading jet energy [GeV]",
            "tau32j1": "Leading jet $\\tau_{32}$",
            "tau32j2": "Subeading jet $\\tau_{32}$",
            "tau21j1": "Leading jet $\\tau_{21}$",
            "tau21j2": "Subleading jet $\\tau_{21}$",
            "mjj" : "$m_{jj}$ [GeV]",
            "ejj" : "$E_{jj}$ [GeV]",
}