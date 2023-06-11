## Solving one-dimensional minimization problems
* [Description](#description)
* [Get started](#get-started)
* [Project structure](#project-structure)
* [Scheme of Simplex method](#scheme-of-simplex-method)
* [Results](#results)


### Description

### Get started
```bash
git clone https://github.com/IMZolin/one-dimension-minimization <your project name>
cd <your project name>
pip install -r requirements.txt
```

### Project structure
```bash
├───graphics            # images:graphics+scheme of simplex
├───out                 # result of compiling .tex file
│   ├───...             # some additional files for .tex
│   └───lab1_opt_methods.pdf # report .pdf
├───report
│   ├───lab1_opt_methods.tex # report .tex
├───src                 # code
│   ├───adapter.py      # task reader
│   ├───corner_dots.py  # corner dots 
│   ├───data.xlsx       # task conditions
│   ├───dual.py         # parse to dual task
│   ├───executable.py   # main(executable) file
│   ├───preprocessing.py # additional functional(make canon form)
│   ├───result_analisys.py # get results
│   └───simplex.py      # simplex method
```

### Results
