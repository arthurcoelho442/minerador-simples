from dotenv import load_dotenv
from hashlib import sha256
from os import environ
import threading
import random
import string
import time

load_dotenv()

letras      = string.ascii_letters
pontuacoes  = string.punctuation
digitos     = string.digits

multThread, seeds  = [], []

finish_event = threading.Event()

def verificaSEED(_hash):
    if _hash[:int(environ['challenger'])] == "0"*int(environ['challenger']) and "0" not in _hash[int(environ['challenger'])]:
        return True
    return False
    
def random_generator(size=6,chars=letras+pontuacoes+digitos):
    return ''.join(random.choice(chars) for _ in range(size))

def getSeed(seeds, size):
    while(not finish_event.is_set()):
        seed = random_generator(size)
        texto = str(seed).encode('utf-8')
        _hash = sha256(texto).hexdigest()
        if(verificaSEED(_hash)):
            seeds.append(seed)
            finish_event.set()

def map(value, qtd_threads=int(environ['threads']), size_max=int(environ['size_max'])):
    value = int(3 + (size_max * 1.15 * value) / (qtd_threads-1))
    if value > size_max:
        return size_max
    else:
        return value

start_time = time.time()

for i in range(int(environ['threads'])):
    thread = threading.Thread(target=getSeed, args=(seeds, map(i), ))
    multThread.append(thread)
    thread.start()

for thread in multThread:
    thread.join()
    
end_time = time.time()

for seed in seeds:
    texto = str(seed).encode('utf-8')
    _hash = sha256(texto).hexdigest()
    print(f"{_hash} <-> {seed}")
    
print(f"Tempo de execução: {end_time - start_time:.4f} segundos")