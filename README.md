# Minerador Simples

## Objetivo
Gerar um hash válido de acordo com a dificuldade definida pela rede. Começando com uma dificuldade inicial igual a do próprio Bitcoin, que corresponde a 8 zeros no início da hash.

## Configuração

#### implemente um ambiente virtual
```
python3 -m venv ./venv
```

#### acesse o ambiente
```
source venv/bin/activate
```

#### instale as depedencias
```
pip install -r requirements.txt 
```

####  Ajuste o arquivo ````.env```` para adequar ao seu teste
> ```
> challenger  = 6   # quantidade de zeros no início da hash
> threads     = 20  # numero de threadas desejado
> size_max    = 6   # tamanho maximo da sting
> ```

## Execução

> ```
> python3 minerador.py
> ```

## Autor
| [<img src="https://avatars.githubusercontent.com/u/56831082?v=4" width=115><br><sub>Arthur Coelho Estevão</sub>](https://github.com/arthurcoelho442) |
| :---: |