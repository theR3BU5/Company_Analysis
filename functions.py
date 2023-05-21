
def simp_ror(init_val: float, final_val: float):
    return init_val, final_val

def roi(net_prof: float, init_inv: float, div=0):
    return ((net_prof / init_inv) + div) / init_inv * 100

def roe(net_inc: float, share_equity: flaot):
    return (net_inc / share_equity) * 100

def cagr(init_val: float, final_val: float, periods=1):
    return pow((final_val / init_val), (1 / periods)) - 1

"""
# Example usage
nopat = 5000000  # Net Operating Profit After Tax
invested_capital = 25000000  # Invested Capital
"""
def calculate_roic(nopat: float, invested_capital: float):
    roic = nopat / invested_capital
    return roic