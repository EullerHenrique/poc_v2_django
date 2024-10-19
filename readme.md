# Login Proposta Django

## Tecnologias Utilizadas

### Front-End
- Python
- Django
- Html
- Bootstrap
- Javascript
- Ajax
  
### Back-End
- Python
- Django
- Django Rest Framework Simple Jwt [RS256]

## Arquitetura 

### Front-End

#### Estrutura do Sistema:
1. manage.py: Representa a main do sistema, ou seja, o arquivo responsável por iniciar sua execução
2. app: Representa o aplicativo único do sistema
3. core: Representa o coração do sistema, ou seja, contém as configurações essenciais para fazê-lo funcionar
4. resource: Representa os recursos do sistema, ou seja, contém os arquivos estáticos (Css, Js, Img, Html etc) e dinâmicos (Templates Hmtl)

#### Estrutura do Aplicativo [MVC/MVT/DDD]:
1. config: Representa as configurações do aplicativo
2. controller: Representa os controladores do aplicativo do sistema, ou seja, seus endpoints rest
3. view: Representa os visualizadores do aplicativo do sistema, ou seja, suas telas
4. domain: Representa o domínio do aplicativo do sistema, ou seja, sua definição 
5. service: Representa os serviços do aplicativo, ou seja, suas regras de negócio

```
├── app
│   ├── config
│   │   ├── migrations
│   ├── controller
│   ├── view
│   ├── domain
│   │   ├── constant
│   ├── service
├── core
│   ├── asgi.py
│   ├── setting.py
│   ├── urls.py
│   ├── wsgi.py
├── resource
│   ├── static
│   ├── template
```

### Back-End

#### Estrutura do Sistema:
1. manage.py: Representa a main do sistema, ou seja, o arquivo responsável por iniciar sua execução
2. app: Representa o aplicativo único do sistema
3. core: Representa o coração do sistema, ou seja, contém as configurações essenciais para fazê-lo funcionar

#### Estrutura do Aplicativo [MVC/DDD]:
1. config: Representa as configurações do aplicativo
2. controller: Representa os controladores do aplicativo do sistema, ou seja, seus endpoints rest
3. domain: Representa o domínio do aplicativo do sistema, ou seja, sua definição 
4. service: Representa os serviços do aplicativo, ou seja, suas regras de negócio
    
```
├── app
│   ├── config
│   │   ├── migrations
│   ├── controller
│   ├── domain
│   │   ├── constant
│   │   ├── exception
│   │   ├── dto
│   │   │  ├── response
│   ├── service
│   │   ├── external
│   │   │  ├── dto
│   │   │  ├── util
│   │   ├── internal
│   │   │  ├── dto
│   │   │  ├── util
├── core
│   ├── asgi.py
│   ├── setting.py
│   ├── urls.py
│   ├── wsgi.py
```

## Configuração
1. Instale o Python: https://www.python.org/downloads/

### Back-End
1. Abra o terminal
2. Vá até a pasta back-end 
3. Rode os comandos:
  1. python -m venv venv
  2. .\venv\Scripts\activate
  3. python.exe -m pip install --upgrade pip
  4. pip install -r requirements.txt
  5. python manage.py makemigrations app
  6. python manage.py migrate
  7. python manage.py createsuperuser

### Front-End
1. Abra o terminal
2. Vá até a pasta front-end
3. Rode os comandos:
  1. python -m venv venv
  2. .\venv\Scripts\activate
  3. python.exe -m pip install --upgrade pip
  4. pip install -r requirements.txt
  5. python manage.py makemigrations app
  6. python manage.py migrate

## Execução

### Back-End

- Rode o comando:
  - python manage.py runserver 8000
- Acesse no host:
  - http://127.0.0.1:8000
    
### Front-End

- Rode o comando:
  - python manage.py runserver 8001
- Acesse no host:
  - http://127.0.0.1:8001

## Telas

### Login

![Screenshot 2024-09-17 231026](https://github.com/user-attachments/assets/3512cbf5-f77a-4a47-ae24-456cc7114fc3)

### Opções

![Screenshot 2024-09-17 231102](https://github.com/user-attachments/assets/484510eb-2690-420e-8991-3fbaff6945da)

### Simular Proposta

![Screenshot 2024-09-12 213348](https://github.com/user-attachments/assets/177caca1-523d-4ddd-9df7-8f0cb593406a)
![Screenshot 2024-09-12 213638](https://github.com/user-attachments/assets/8a896d01-52d0-46a9-b9ab-cd0f112b62e3)

## Endpoints

### Simular Proposta
- Endpoint: GET {{host}}/colaborador/listar/json
- Request: Bearer {tokenJwt}
- Response:
```
[
    {
        "matricula": "00001",
        "userName": "eullerHBO",
        "nome": "Euller Henrique Bandeira Oliveira",
        "email": "eullerhenrique@outlook.com",
        "ufTrabalho": "MG",
        "tipoApuracao": "Timesheet",
        "tipoVinculo": "PJ",
        "status": "1",
        "codigoArea": "ENG",
        "codigoEquipe": "PROJETO-PYTHON",
        "codigoEmpresa": "01"
    },
    {
        "matricula": "00001",
        "userName": "eullerHBO",
        "nome": "Euller Henrique Bandeira Oliveira",
        "email": "eullerhenrique@outlook.com",
        "ufTrabalho": "MG",
        "tipoApuracao": "Timesheet",
        "tipoVinculo": "PJ",
        "status": "1",
        "codigoArea": "ENG",
        "codigoEquipe": "PROJETO-PYTHON",
        "codigoEmpresa": "01"
    }
]
```

### Gerar Excel Simulação Proposta
- Endpoint: GET {{host}}/colaborador/gerarExcel
- Request: Bearer {tokenJwt}
- Response:
![Screenshot 2024-08-13 092351](https://github.com/user-attachments/assets/92c7785b-8eb0-43cf-bc9d-fb6dee851972)

