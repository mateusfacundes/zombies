# Zombies Api
A api Zombies permite ter acesso as condições dos sobreviventes de um apocalipse zombie 

## Métodos
Requisições para a API devem seguir os padrões:
| Método | Descrição |
|---|---|
| `GET` | Retorna informações de um ou mais registros. |
| `POST` | Utilizado para criar um novo registro. |
| `PUT` | Atualiza dados de um registro ou altera sua situação. |

# Group Recursos


# Sobreviventes [/sobreviventes]

Os sobreviventes seguem o mesmo padrão mostrando apenas: Nome, idade, sexo, latitude, longitude e se está infectado.


### Listar (List) [GET]

+ Request (application/json)


+ Response 200 (application/json)
        
            {
                {
                    "nome_sobrevivente": "Carlos",
                    "idade_sobrevivente": 31,
                    "sexo_sobrevivente": "Masculino",
                    "latitude_sobrevivente": 120.2,
                    "latitude_sobrevivente": 541.2,
                    "infectado": false,
                    "flags_infectado": 0,
                },
                {
                    "sobreviventes_id": 35, 
                    "nome_sobrevivente": "Mateus", 
                    "idade_sobrevivente": 24, 
                    "sexo_sobrevivente": "Masculino", 
                    "latitude_sobrevivente": 123.0, 
                    "longitude_sobrevivente": 123.0, 
                    "infectato": false, "flags_infectado": 0
                }

            }



# Adicionar Sobreviventes [/sobreviventes/adicionarsobrevivente]

### Novo (Create) [POST]

+ Attributes (object)

    + nome_sobrevivente: Nome do Sobrevivente
    + idade_sobrevivente: Idade do sobrevivente
    + sexo_sobrevivente: Sexo do sobrevivente
    + latitude_sobrevivente: latitude do sobrevivente
    + longitude_sobrevivente: longitude do sobrevivente
    + infectado: Estado de infecção do sobrevivente
    + flags_infectado: Quantidade de alertas do sobrevivente

+ Request (application/json)

    + Body

            {
              "nome_sobrevivente": "Carlos",
              "idade_sobrevivente": 31,
              "sexo_sobrevivente": "Masculino",
              "latitude_sobrevivente": 120.2,
              "latitude_sobrevivente": 541.2,
              "infectado": false,
              "flags_infectado": 0,
            }

+ Response 200 (application/json) 

    + Body

            {
                "data": "Sobrevivente adicionado com sucesso!",
            }


# Zombies

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
