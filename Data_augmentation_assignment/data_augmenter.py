import data_generator as dg

text, iterations= dg.get_input()
samples = {}
dg.print_header(text)

for i in range (iterations):
    augmented_text= dg.data_generation(text)
    dg.check_repetition(augmented_text, samples)

