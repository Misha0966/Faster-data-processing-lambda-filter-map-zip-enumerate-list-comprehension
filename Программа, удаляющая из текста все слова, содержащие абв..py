my_str = 'Мороз и солнце - день чудесный ещёабв тыабв дремабвлешь другабв абвпрелелетный'.split()
print(' '.join([word for word in my_str if 'абв' not in word]))
