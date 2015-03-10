import numpy as np

data = open("test.txt")

sample_data = []

for numbers in data:
	sample_data.append(numbers)

new_data = np.fft.fft(sample_data)
frequency = np.fft.fftfreq(len(sample_data))

for coef, freq in zip(new_data, frequency):
	if coef:
		print('{c:>6} * exp(2 pi i t * {f})'.format(c=coef,f=freq))
