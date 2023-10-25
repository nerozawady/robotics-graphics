from adjustText import adjust_text
import numpy as np
import matplotlib.pyplot as plt

# np.random.seed(0)
# x, y = np.random.random((2, 30))
x = []
y = []

x.append(np.float64(2))
x.append(np.float64(10))
x.append(np.float64(28))

y.append(np.float64(20))
y.append(np.float64(1))
y.append(np.float64(8))


print(type(x[0]))
# x = [5.0, 2.1, 10.9, 2.2]
# y = [10.0, 13.2, 20.3, 7.7]
# fig, ax = plt.subplots()
# plt.plot(x, y, 'bo')
# texts = [plt.text(x[i], y[i], 'Text%s' %i, ha='center', va='center') for i in range(len(x))]

# fig, ax = plt.subplots()
plt.scatter(x, y)
texts = [plt.text(x[i], y[i], 'Text%s' % i, ha='center', va='center')
         for i in range(len(x))]
adjust_text(texts)
plt.show()
