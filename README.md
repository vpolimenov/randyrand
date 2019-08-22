# randyrand

# Installation

1. Open terminal and activate your virtual environment of preference.
2. Clone the repository locally in a selected directory (/tmp for instance) - `git clone https://github.com/vpolimenov/randyrand.git`
3. Then from the directory you ran step 1 command you can `pip install randyrand` (again in a selected python3 environment), which should install this package and all required packages (if not already satisfied)
4. Open a python console from terminal - just type `python` in the same environment where the package was installed.
5. You now should be able to do the following: `from randyrand.random_class import GetRandomNums`

# Parameters

The number of samples (`n_samples`) and distribution type (`distribution`) are compulsory parameters (see some examples below).

There are three supported distributions at the moment - normal, binomial and poisson. Each of them takes different parameters. There are default values assigned to each distribution parameter:

```
The normal distribution takes mu and sigma, where mu=0 and sigma=0.1
The binomial distribution takes trials and probability, where trials=10 and prob=0.5
The poisson distribution takes interval, where interval=5
```

However, if you would like to change some of the additional parameters you can pass them to the class instance (see some examples below).

# Some examples

**Example1**
(Use default distribution parameters. Call just draw(), then call summarize())
```
rand1 = GetRandomNums(n_samples = 5, distribution = 'normal')
rand1.draw()

# Should return something like:
# Parameters of the draw: 
#                samples size: 5 
#                distribution: normal 
#                mu: 0 
#                sigma: 0.1
# [ 0.04172006  0.0923807   0.02645455 -0.00710711 -0.00346559]

rand1.summarize()

# Should return something like:
# Parameters of the draw: 
#                samples size: 5 
#                distribution: normal 
#                mu: 0 
#                sigma: 0.1
# [ 0.04172006  0.0923807   0.02645455 -0.00710711 -0.00346559]
# 'min: -0.00710710701999073, max: 0.09238069884665677, mean: 0.029996522979300562, std: 0.03616120772612344'
```

**Example2**
(Pass distribution parameters)

```
rand5 = GetRandomNums(n_samples = 5, distribution = 'normal', mu = 4, sigma = 1)
rand5.summarize()

# Should return something like:
# Parameters of the draw: 
#                samples size: 5 
#                distribution: normal 
#                mu: 4 
#                sigma: 1
# [3.10469812 5.08752916 4.31424743 5.7948281  6.07260011]
# 'min: 3.1046981181658846, max: 6.072600107174173, mean: 4.874780581834363, std: 1.074607868448617'
```

Additional examples you can see in the notebooks directory - `random_nums_from_dist` notebook in particular.
