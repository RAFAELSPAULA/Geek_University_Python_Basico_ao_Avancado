import numpy as np

teste = np.array([i for i in range(1, 41)]).reshape((10, 4))
print('Normal:')
print(teste)

print('Transposta:')
print(teste.T)
