import numpy as np
from scipy import linalg as la

def SGHMC_friction(theta0, X, grad_logden_data, grad_logden_prior, V, eps, i, C, batch_size, M = None):
    '''
    SGHMC with friction:
    theta0(numpy array): starting position of theta (p,)
    X: data (n,m)
    grad_logden_data: gradient of the data log density (p,)
    grad_logden_prior: gradient of the prior log density (p,)
    V: estimated finsher information, (p,p)
    eps: step size
    i: number of iterations
    C: user specified friction term
    batch_size: size of minibatches
    M: Mass matrix
    '''
    
    def minib(x, batch_size):
        '''
        create minibatchs of x
        x: data
        batch_size: size of minibatch, if len(x)/batch_size is not integer, some batches wille have smaller sizes
        
        output: list of np.array of batchs [[batch_size,],...,[]]
        '''
        m = np.ceil(x.shape[0]/batch_size)
        np.random.shuffle(x)

        return np.array_split(x, m)
    
    def grad_U(grad_log_data, grad_log_prior, batch, theta, n):
        '''compute the gradient of U of batch'''
        
        return -(n*grad_log_data(batch,theta)/batch.shape[0]+grad_log_prior(theta))
    
    n, m = X.shape
    p = theta0.shape[0] # dim of theta
    
    # samples
    thetat = np.zeros((i+1,p)) # (#samples,p)
    thetat[0] = theta0 # set initial
    batch = minib(X, batch_size) # m-list of (batch_size,)
    m = len(batch)
    B = 1/2*eps*V
    
    
    if(M is None):
        M = np.eye(p)
    
    for t in range(i):
        ri = np.random.multivariate_normal(np.zeros(p), M)
        thetai = thetat[t]
        for j in range(m):
            bat = batch[j] # batch_j
            thetai = thetai + eps * np.linalg.inv(M) @ ri
            gU = grad_U(grad_logden_data,grad_logden_prior,bat,thetai,n)
            ri = ri - eps * gU - eps * C @ ri + la.sqrtm(2*(C-B)*eps) @ np.random.multivariate_normal(np.zeros(p), M)
        thetat[t+1] = thetai + eps * np.linalg.inv(M) @ ri
    
    return thetat[100:thetat.shape[0]]
      