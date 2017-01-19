total_segundos = int(input('Por favor, entre com o número de segundos que deseja converter: '))


# Um dia tem 86400 segundos
dias = total_segundos // 86400

segundos_restantes = total_segundos % 86400

# Pegamos o restante de segundos que um dia possui
horas = segundos_restantes // 3600

# Nas horas pegamos a parte inteira, nos segundos restantes pegamos o resto da divisão
segundos_restantes = total_segundos % 3600

# Nos minutos pegamos os  segundos que sobraram e dividimos por 60
# Pois 1 minuto possui 60 segundos
minutos = segundos_restantes // 60

# Agora pegamos o resto de segundos restantes e colocamos como segundos finais
segundos_restantes_final = segundos_restantes % 60


print(dias, 'dias,', horas, 'horas,', minutos, 'minutos e', segundos_restantes_final, 'segundos.')