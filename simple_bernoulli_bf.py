# Three routines to help calculate a Bayes factor for H_fair / H_cheat over a simple Bernoulli process.
#    see https://github.com/hjhornbeck/bayes_speedrun_cheating/ for details.

def prior(r, scale):
    """Generate an appropriate prior to be used during inference with a Beta conjugate prior.
    
    Parameters
    ----------
    r = The expected rate of item drops, assuming no modification of the game. Must be between 0 and 1.
    scale = A value to scale our credence around r. Higher values favour the hypothesis that
       someone played fairly, while lower values favour someone who cheated. Must be a positive real.
       
    Returns
    -------
    A tuple (alpha, beta) representing the Beta prior."""
    
    # ensure the proper values are given
    assert (r > 0) and (r < 1)
    assert scale > 0
    
    if r < .5:
        return (scale, scale*(1-r)/r)
    else:
        return (scale*(1-r)/r, scale)
    
def posterior_H_fair( vec_k, vec_n, r_fair, a_prior, b_prior ):
    """Calculate the likelihood of H_fair, given the posterior distribution defined by vec_n, vec_k, and the prior.
        Relies on mpmath to perform all calculations, which also means you can adjust the precision.
    
    Parameters
    ----------
    vec_k: A total or list containing the successful attempts at this task until it was completed.
    vec_n: A total or list containing the total attempts at this task until it was completed.
    r_fair: A float between 0 and 1 representing the probability of success predicted by H_fair.
    a_prior: A positive or zero float representing the alpha variable of the prior.
    b_prior: A positive or zero float representing the beta variable of the prior.
    
    Returns
    -------
    The likelihood, an mpmath float in the range [0,infinity]."""

    # place some imports here to encourage copy-paste coding
    from mpmath import gammaprod
    from numpy import sum        # vectorized, likely faster than Python's sum
    
    # the downside of encouraging copy-pasting is that this code will face some
    #  dirty/invalid inputs. By going wild with asserts, I'm making it tougher to
    #  use this function inappropriately.
    assert (r_fair > 0) and (r_fair < 1)
    assert (a_prior >= 0) and (b_prior >= 0)
    
    # use duck typing to determine whether these are lists or not
    try:
        len_k = len(vec_k)
        k_is_list = True
    except TypeError:
        len_k = 1
        k_is_list = False

    try:
        len_n = len(vec_n)
        n_is_list = True
    except TypeError:
        len_n = 1
        n_is_list = False
   
    # do additional checks if both are lists
    if k_is_list and n_is_list:
        
        assert len_k == len_n
        for i,n in enumerate(vec_n):
            assert n > 0
            assert (vec_k[i] >= 0) and (vec_k[i] <= n)
                  
    # now calculate sums      
    if k_is_list:
        sum_k = sum(vec_k)
    else:
        sum_k = vec_k
        
    if n_is_list:
        sum_n = sum(vec_n)
    else:
        sum_n = vec_n
        
    # one final round of checks
    assert sum_n >= 1
    assert (sum_k >= 0) and (sum_k <= sum_n)

    # calculate the final result
    numerator =   [a_prior + b_prior + sum_n, a_prior + b_prior + sum_n,
                  2*a_prior + sum_k + r_fair*sum_n - 1,
                  2*b_prior - sum_k + (2 - r_fair)*sum_n - 1]
    denominator = [a_prior + sum_k, b_prior + sum_n - sum_k,
                   a_prior + r_fair*sum_n, b_prior + (1 -r_fair)*sum_n,
                  2*(a_prior + b_prior + sum_n - 1)]
    
    return gammaprod(numerator, denominator)

def BF_H_fair_H_cheat( vec_k, vec_n, r_fair, a_prior, b_prior, sum_n_scalar=0.5 ):
    """Calculate the Bayes factor associated with H_fair / H_cheat, given the posterior distribution defined by vec_n, vec_k, and the prior.
        Relies on mpmath to perform all calculations, which also means you can adjust the precision.
    
    Parameters
    ----------
    vec_k: A total or list containing the successful attempts at this task until it was completed.
    vec_n: A total or list containing the total attempts at this task until it was completed.
    r_fair: A float between 0 and 1 representing the probability of success predicted by H_fair.
    a_prior: A positive or zero float representing the alpha variable of the prior.
    b_prior: A positive or zero float representing the beta variable of the prior.
    sum_n_scalar: A positive or zero float that's used to weight the ||vec_n|| component. Defaults to 1/2.
    
    Returns
    -------
    The Bayes factor, a likelihood and mpmath float in the range [0,infinity]. Values greater than 1 favour
       fairnes, values below 1 favour cheating."""
    
    from mpmath import fdiv, fmul, gammaprod, power
    
    # validate our one new variable
    assert sum_n_scalar >= 0
    
    # rely on posterior_H_fair()'s assertions to validate the remaining inputs
    integral = posterior_H_fair( vec_k, vec_n, r_fair, a_prior, b_prior )
    
    # but we still need sum_n for calculations
    try:
        len_n = len(vec_n)
        n_is_list = True
    except TypeError:
        len_n = 1
        n_is_list = False  
                 
    if n_is_list:
        sum_n = sum(vec_n)
    else:
        sum_n = vec_n

    
    # invoke mpmath instead of python's functions, to discourage precision loss
    m = fdiv( a_prior + r_fair*sum_n - 1,  a_prior + b_prior + sum_n - 2 )
    M = fmul( gammaprod([a_prior + b_prior + sum_n], [a_prior + r_fair*sum_n,b_prior + (1-r_fair)*sum_n]), \
             fmul(power( m, a_prior + r_fair*sum_n - 1 ), power( 1-m, b_prior + (1-r_fair)*sum_n - 1 )) )

    return fdiv( fmul(M - 1 + sum_n_scalar/sum_n, integral), M + sum_n_scalar/sum_n - integral )