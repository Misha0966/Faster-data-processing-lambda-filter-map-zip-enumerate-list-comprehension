print(' '.join(filter(lambda x: not 'абв' in x,'Мороз и солнце - день чудесный! ещёабв тыабв дремабвлешь другабв абвпрелелетный'.split())))

my_str = 'Мороз и солнце - день чудесный, ещёабв тыабв дремабвлешь другабв абвпрелелетный'.split()
res = [word for word in my_str if 'абв' not in word]
print(' '.join([word for word in my_str if 'абв' not in word]))