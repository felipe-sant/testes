<div align="center">

# 💻 Meu Portfólio Pessoal 💻

[![HTML5](https://img.shields.io/badge/HTML-E44D26?style=for-the-badge&logo=html5&logoColor=white)](https://sua-url-aqui.com)
[![HTML3](https://img.shields.io/badge/CSS-264DE4?&style=for-the-badge&logo=css3&logoColor=white)](https://sua-url-aqui.com)
[![HTML3](https://img.shields.io/badge/Python-2973A1?style=for-the-badge&logo=python&logoColor=white)](https://sua-url-aqui.com)
[![Flask Badge](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://sua-url-aqui.com)

</div>

Olá, meu nome é Luiz Felipe, mas pode me chamar só de Felipe, nesse repositório você poderá acessar o meu portfólio pessoal que fala sobre mim, meus conhecimentos e informações para entrar em contato.

## ⚙️ Como rodar:

1. Abra o CMD no local que deseja clonar o repositório e execute este comando:

```
git clone https://github.com/felipe-sant/portfolio.git
```

2. Para instalar as dependencias siga os seguintes comandos:

```
cd portfolio/src/
python -m venv venv
.\venv\Scripts\activate
pip install -r ../requirements.txt
flask run
```

3. Após isso, abra o seguinte link no navegador de sua preferência: http://127.0.0.1:5000

4. Para fechar o ambiente virtual e sair digite:

```
deactivate
```

## 📄 Descrição do Projeto:

Na pasta [doc/](doc/) há os aquivos de documentação do projeto, havendo os arquivos:

- [wireframe.pdf](doc/wireframe.pdf), arquivo pdf do wireframe do projeto, contendo tanto a versão em desktop quanto a versão em mobile das telas.

Na pasta [src/](src/) há os arquivos de source, havendo as pastas:
- [static/](src/static/), contendo arquivos estaticos, como imagens e páginas de estilo.
- [templates/](src/templates/), contendo os arquivos de templates das páginas.
- [app.py](src/app.py), sendo o arquivo de aplicação, onde é utilizado o Flask com um sistema de templates para imprimir a página HTML.
