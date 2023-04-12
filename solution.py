import pandas as pd
import numpy as np


chat_id = 335933917

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    count = np.array([x_success * x_cnt, y_success * y_cnt])
    nobs = np.array([x_cnt, y_cnt])
    stat, pval = proportions_ztest(count, nobs, alternative = 'smaller')
    if pval < 0.07:
      return True
    else:
      return False
