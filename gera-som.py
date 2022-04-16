# Instalar: pip install gTTS
from gtts import gTTS

# Informações
texto = 'Tu te tornas eternamente responsável por aquilo que cativas.'
audio = 'audio.mp3'
language = 'pt-br'

# Definições
gerar = gTTS(
	text = texto, 
	lang = language
)

# Gera áudio
gerar.save(audio)

# Cor para exibição
AZUL  = '\033[1;34m'
FIMCOR = '\033[0;0m'

# Exibe texto após finalizar
print(AZUL + 'Audio gerado com texto:' + FIMCOR + ' ' + texto)