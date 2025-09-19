# API de Cidades Brasileiras 🇧🇷

Este projeto é uma API desenvolvida com Django e Django REST Framework para fornecer informações sobre **Regiões**, **Unidades da Federação (UFs)** e **Municípios** do Brasil. A API consome dados da [API do IBGE](https://servicodados.ibge.gov.br) para popular automaticamente as informações dos estados e seus municípios.

---

## 🚀 Tecnologias Utilizadas

- Python 3.13+
- Django 5.2+
- Django REST Framework
- SimpleJWT (para autenticação com tokens)
- SQLite (padrão do Django)
- Requests (para consumo da API do IBGE)

---

## 🧱 Estrutura do Projeto

### Models

- **Região**
  - `id`: ID da região (ex: 1)
  - `nome`: Nome da região (ex: Sudeste)
  - `sigla`: Sigla da região (ex: SE)

- **UF**
  - `id`: ID da UF (ex: 35)
  - `sigla`: Sigla do estado (ex: SP)
  - `regiao`: FK para `Região`

- **Município**
  - `id`: ID do município (ex: 3509502)
  - `nome`: Nome do município (ex: Campinas)
  - `uf`: FK para `UF`

---

## 🔗 Endpoints

| Recurso     | URL Base                | Descrição                             |
|-------------|-------------------------|----------------------------------------|
| Regiões     | `regiao/`          | CRUD de regiões                        |
| UFs         | `uf/`              | Cria UF e popula municípios via IBGE  |
| Municípios  | `municipio/`       | CRUD de municípios                     |
| Token       | `token/`           | Geração de access/refresh tokens JWT  |
| Refresh     | `token/refresh/`   | Atualiza access token via refresh     |

---

## 🛡️ Autenticação

Utiliza JWT (JSON Web Token). Para obter um token:

### POST `/api/token/`

```json
{
  "username": "seu_usuario",
  "password": "sua_senha"
}
```

### Resposta

``` json
{
  "access": "seu_token",
  "refresh": "seu_refresh_token"
}
```

### Use o token acess no cabeçalho:

```http
Authorization: Bearer seu_token
```

## 📝 Exemplo de Uso
### Criando um estado e seus municípios
Para popular o banco de dados com os dados de um estado e seus municípios, basta enviar uma requisição POST para o endpoint de UF, especificando a sigla do estado e a região a qual ele pertence. A API fará o restante do trabalho, consumindo os dados do IBGE.

#### Endpoint:
`POST /api/uf/`

#### Corpo da requisição:

```json
{
  "sigla": "SP",
  "regiao": 1
}
```
