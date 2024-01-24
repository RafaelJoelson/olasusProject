# olasusProject

Este é um projeto baseado em aplicações utilizadas por Agentes Comunitários de Saúde do SUS.

## Tecnologias Utilizadas

- Python 3.10
- Django

## Conteúdo

Explicação sobre os principais arquivos e diretórios no seu projeto.
- `olasusProjectGH/`: Diretório do Github.
	- `olasusProject/`: Diretório do projeto.
		- `app_website/`: Contém os arquivos da aplicação Django.
			- `templates/`: Contém os arquivos HTML das páginas.
				- `olasus_app/` : Contém os arquivos HTML das páginas.
                    - index.html : Página de login
			- `migrations/`: Contém as migrações dos dados do projeto.
				- 0001_initial.py : Migração inicial do banco de dados.
			- `admin.py`: Configurações para o Django Admin.
			- `apps.py`: Configurações da aplicação.
			- `forms.py`: Formulários do Django para validação.
			- `models.py`: Modelos de dados para o banco de dados.
			- `tests.py`: Testes da aplicação.
			- `urls.py`: Configurações de URLs da aplicação.
			- `views.py`: Funções de visualização da aplicação.
		- `static/`: Local para armazenar arquivos de mídia (vídeos, imagens, etc.).
            - `olasus_app/`: Local para armazenar arquivos de mídia (vídeos, imagens, etc.).
                - `css/`: Armazena os estilos CSS do projeto.
                - `img/`: Armazena as imagens do projeto.

## Instalação

1. Clone o repositório:

    ```bash
    
    ```

2. Navegue até o diretório do projeto:

    ```bash
    cd 
    ```

3. Crie e ative um ambiente virtual com o Anaconda prompt (recomendado):

	```bash
    conda create --name pythonProject python=3.11
    conda activate pythonProject
    ```

4. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

5. Execute as migrações do banco de dados:

    ```bash
    python manage.py migrate
    ```

6. Crie um superusuário para acessar o Django Admin:

    ```bash
    python manage.py createsuperuser
    ```

7. Inicie o servidor de desenvolvimento:

    ```bash
    python manage.py runserver
    ```

8. Acesse o sistema em [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Acesso ao Django Admin

1. Acesse [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).
2. Faça login com as credenciais do superusuário.

## Referência Original



## Autor

Rafael Joelson
