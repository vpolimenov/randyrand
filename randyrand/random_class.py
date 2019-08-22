import numpy as np


class GetRandomNums(object):
    def __init__(self, n_samples, distribution, mu=0, sigma=0.1, interval=5, trials=10, prob=.5, draw=[]):
        self.n_samples = n_samples
        self.distribution = distribution
        self.mu = mu
        self.sigma = sigma
        self.interval = interval
        self.trials = trials
        self.prob = prob
        self._draw = draw
        
    def normal_dist(self, mu, sigma):
        return np.random.normal(mu, sigma, self.n_samples)
    
    def poisson_dist(self, interval):
        return np.random.poisson(interval, self.n_samples)
    
    def binomial_dist(self, trials, prob):
        return np.random.binomial(trials, prob, self.n_samples)
    
    def draw(self):
        if self.distribution == 'normal':
            print(f'''Parameters of the draw: \n
                samples size: {self.n_samples} \n
                distribution: {self.distribution} \n
                mu: {self.mu} \n
                sigma: {self.sigma}
            ''')
            
            self._draw = self.normal_dist(self.mu, self.sigma)
            return self._draw
        elif self.distribution == 'poisson':
            print(f'''Parameters of the draw: \n
                samples size: {self.n_samples} \n
                distribution: {self.distribution} \n
                interval: {self.interval} \n
            ''')
            
            self._draw = self.poisson_dist(self.interval)
            return self._draw
        elif self.distribution == 'binomial':
            print(f'''Parameters of the draw: \n
                samples size: {self.n_samples} \n
                distribution: {self.distribution} \n
                trials: {self.trials} \n
                prob: {self.prob}
            ''')
            self._draw = self.binomial_dist(self.trials, self.prob)
            return self._draw
        else:
            print(f'''Parameters of the draw: \n
                samples size: {self.n_samples} \n
                distribution: {self.distribution} \n
            ''')
            
            return "Distribution not supported!"
        
    def summarize(self):
        if len(self._draw) == 0:
            return 'Please draw a random sample first!'
        random_sample = self._draw
        rnd_sample_min = np.min(random_sample)
        rnd_sample_max = np.max(random_sample)
        rnd_sample_mean = np.mean(random_sample)
        rnd_sample_std = np.std(random_sample)
        
        print (self._draw)
        return f'min: {rnd_sample_min}, max: {rnd_sample_max}, mean: {rnd_sample_mean}, std: {rnd_sample_std}'

