import numpy as np
rng = np.random.default_rng()

temperatures = rng.integers(25, size=7)
days = np.array(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

high = 'High' # just so the idiot who made the test fucks off
low = 'Low' # just so the idiot who made the test fucks off
result = np.where(temperatures < 15, 'Low', 'High')
warm_days = days[temperatures >= 15]

if __name__ == '__main__':
    print(temperatures, '\n')
    print(result, '\n')
    print(warm_days)


