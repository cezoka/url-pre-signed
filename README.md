# Gerador de Pre-Signed URL S3

Um script simples em Python para gerar links (pre-signed URLs) que dão permissão temporária de upload em um bucket do S3. 

Foi criado para que pessoas de fora (como o suporte da AWS ou algum parceiro) consigam enviar arquivos direto pro nosso S3 (`price-list-aws`) sem a gente precisar criar usuário no IAM ou repassar qualquer credencial.

### O que você precisa ter na máquina

Antes de rodar pela primeira vez, confira se você já tem:
- Python 3.x instalado
- AWS CLI configurado e logado (via SSO)

### Como rodar do zero

1. **Instale a dependência do Python (`boto3`)**
   Abra o seu terminal na pasta do projeto e instale a biblioteca oficial da AWS para Python:
   ```bash
   pip install boto3
   ```

2. **Sua sessão na AWS tem que estar ativa**
   A autenticação via SSO precisa estar de pé. Logue normalmente como você já faz para trabalhar. 
   
   ```bash
   aws sso login
   ```
   *Dica: Se você usar algum profile específico além do default, é só definir a variável no terminal antes (ex: no PowerShell `$env:AWS_PROFILE="seu-perfil-sso"` ou no bash/mac `export AWS_PROFILE="seu-perfil-sso"`).*

3. **Execute o script!**
   Com o login garantido no terminal, é só rodar do jeito clássico mesmo:
   ```bash
   python gerador_url_upload.py
   ```

### E o resultado?

O script vai cuspir um comando inteirinho no seu terminal! Ele devolve o link criptografado e blindado de segurança (expira em 12 horas) empacotado num exato comando do `curl`.
Basta copiar da tela e mandar para pessoa! O contato que vai fazer o upload só precisa apontar para o arquivo dele no computador e colar o `curl` lá no terminal.
