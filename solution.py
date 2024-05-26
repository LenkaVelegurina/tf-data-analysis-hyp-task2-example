import pandas as pd
import numpy as np
from scipy.stats import mannwhitneyu


chat_id = 440117284 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    stat, p_value = mannwhitneyu(x, y, alternative='two-sided')
    return p_value < 0.05 # Ваш ответ, True или False
