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

### Lista de todos sobreviventes [GET]

+ Request (application/json)


+ Response 200 (application/json)
        
            {
                {
                    "sobreviventes_id": 35, 
                    "nome_sobrevivente": "Mateus", 
                    "idade_sobrevivente": 24, 
                    "sexo_sobrevivente": "Masculino", 
                    "latitude_sobrevivente": 123.0, 
                    "longitude_sobrevivente": 123.0, 
                    "infectato": false, "flags_infectado": 0
                },
                {
                    "sobreviventes_id": 36, 
                    "nome_sobrevivente": "Sabrina",
                    "idade_sobrevivente": 22,
                    "sexo_sobrevivente": "Feminino",
                    "latitude_sobrevivente": 120.2,
                    "latitude_sobrevivente": 541.2,
                    "infectado": false,
                    "flags_infectado": 0,
                },

            }

# Sobrevivente [/sobrevivente/sobrevivente/:id]

### Conseguir informações de um sobrevivente [GET]

+ Request (application/json)


+ Response 200 (application/json)
        
            {
                "sobreviventes_id": 35, 
                "nome_sobrevivente": "Mateus", 
                "idade_sobrevivente": 24, 
                "sexo_sobrevivente": "Masculino", 
                "latitude_sobrevivente": 123.0, 
                "longitude_sobrevivente": 123.0, 
                "infectato": false, "flags_infectado": 0
            
            }



# Atualizar Sobreviventes [/sobreviventes/atualizarsobrevivente/:id]

### Atualizar um novo sobrevivente [POST]

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
                "data": "Sobrevivente atualizado com sucesso!",
            }


# Adicionar Sobreviventes [/sobreviventes/adicionarsobrevivente]

### Cadastrar um novo sobrevivente [POST]

+ Attributes (object)

    + nome_sobrevivente: Nome do Sobrevivente
    + idade_sobrevivente: Idade do sobrevivente
    + sexo_sobrevivente: Sexo do sobrevivente
    + latitude_sobrevivente: latitude do sobrevivente
    + longitude_sobrevivente: longitude do sobrevivente
    + infectado: Estado de infecção do sobrevivente
    + flags_infectado: Quantidade de alertas do sobrevivente
    + itens: Lista com id dos items e suas respectivas quantidades

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
              "itens": {
                {
                    "inventario_id": 1,
                    "qtd": 2
                },
                {
                    "inventario_id": 3,
                    "qtd": 1
                }
              }
            }

+ Response 200 (application/json) 

    + Body

            {
                "data": "Sobrevivente adicionado com sucesso!",
            }

# Relatorio [/sobreviventes/relatorio]

### Informações do relatório [GET]

+ Request (application/json)


+ Response 200 (application/json)
        
            {
                "porcentagem_infectados": 33.33, 
                "porcentagem_nao_infectados": 66.67, 
                "media_aguas": 42.17, 
                "media_alimentacao": 21.17, 
                "media_medicacao": 12, 
                "media_municao": 2.5, 
                "pontos_perdidos": 44
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

# Dependencias Django

+ rest_framework
+ corsheaders