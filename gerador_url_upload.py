import boto3
from botocore.exceptions import ClientError
import os

def create_presigned_put_url(bucket_name, object_name, expiration=86400, profile_name=None):
    """
    Gera uma URL pré-assinada (pre-signed URL) para fazer UPLOAD (PUT) de um arquivo no S3.
    """
    # Inicia a sessão da AWS. Se profile_name for None, ele usa a sessão padrão ou as variáveis de ambiente ativas.
    session = boto3.Session(profile_name=profile_name) if profile_name else boto3.Session()
    s3_client = session.client('s3')
    
    try:
        response = s3_client.generate_presigned_url(
            'put_object',
            Params={'Bucket': bucket_name, 'Key': object_name},
            ExpiresIn=expiration
        )
    except ClientError as e:
        print(f"Erro ao gerar a URL (verifique seu login no SSO): {e}")
        return None
    return response

if __name__ == "__main__":
    BUCKET_NAME = 'price-list-aws'
    # Nome genérico do arquivo. O que o TAM subir via curl vai cair com esse nome no seu S3
    NOME_DO_ARQUIVO = 'tam/upload_do_tam.zip' 
    EXPERACAO_SEGUNDOS = 43200 # 12 horas
    
    # Se você tiver configurado uma variável de ambiente AWS_PROFILE no terminal, o script vai achar.
    PROFILE_SSO = os.environ.get('AWS_PROFILE', None)
    
    print(f"--- Gerador de Pre-Signed URL PUT ---")
    if PROFILE_SSO:
        print(f"Perfil AWS detectado: {PROFILE_SSO}")
    else:
        print("Perfil AWS padrão em uso. (Se der erro de credencial, defina o AWS_PROFILE antes).")
        
    print(f"Bucket: {BUCKET_NAME} | Destino no S3: {NOME_DO_ARQUIVO}\n")

    url = create_presigned_put_url(BUCKET_NAME, NOME_DO_ARQUIVO, EXPERACAO_SEGUNDOS, PROFILE_SSO)

    if url:
        print("✅ URL gerada com sucesso! \nEnvie este link acompanhado da instrução abaixo para o TAM da AWS:")
        print("-" * 80)
        print(url)
        print("-" * 80)
        print("\nPara o TAM enviar o arquivo, ele só precisa usar esse comando no terminal dele:")
        print(f'curl -X PUT -T "arquivo_dele_local.zip" "{url}"\n')
    else:
        print("❌ Falha ao gerar a URL. Tente rodar o comando de login do SSO novamente.")
