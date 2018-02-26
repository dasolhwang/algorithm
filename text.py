    #def numerical_gradient(self, x, t):
    #    loss_W = lambda W: self.loss(x,t)
    #    grads={}
    #    grad['W1'] = numerical_gradient(loss_W, self.params['W1'])
    #    grad['b1'] = numerical_gradient(loss_W, self.params['b1'])
    #    grad['W2'] = numerical_gradient(loss_W, self.params['W2'])
    #    grad['b2'] = numerical_gradient(loss_W, self.params['b2'])
    #    grad['Wout'] = numerical_gradient(loss_W, self.params['Wout'])
    #    grad['bout'] = numerical_gradient(loss_W, self.params['bout'])
    #    return grads
        
    
    #def parameter_update(self, x, t, lr):
    #    grads = self.numerical_gradient(x,t)
    #    self.parmas['W1'] -= lr*grads['W1']
    #    self.parmas['b1'] -= lr*grads['b1']
    #    self.params['W2'] -= lr*grads['W2']
    #    self.parmas['b2'] -= lr*grads['b2']
    #    self.params['Wout'] -= lr*grads['Wout']
    #    self.params['bout'] -= lr*grads['bout']
    #    return prams

def numerical_gradient(f, x):
    h = 1e-4 # 0.0001
    grad = np.zeros_like(x)
    
    it = np.nditer(x, flags=['multi_index'], op_flags=['readwrite'])
    while not it.finished:
        idx = it.multi_index
        tmp_val = x[idx]
        x[idx] = float(tmp_val) + h
        fxh1 = f(x) # f(x+h)
        
        x[idx] = tmp_val - h 
        fxh2 = f(x) # f(x-h)
        grad[idx] = (fxh1 - fxh2) / (2*h)
        
        x[idx] = tmp_val # ö·ªòêªªË?ª¹
        it.iternext()   
        
    return grad