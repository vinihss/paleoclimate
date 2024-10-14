import os
import subprocess
import zipfile

def generate_requirements():
    """Gera o arquivo requirements.txt com as dependências do projeto."""
    print("Gerando requirements.txt...")
    subprocess.run(["pip", "freeze", ">", "requirements.txt"], shell=True)

def generate_project_structure(output_file='project_structure.txt'):
    """Gera a estrutura de diretórios e arquivos do projeto."""
    print(f"Gerando estrutura de diretórios em {output_file}...")
    with open(output_file, 'w') as f:
        subprocess.run(["tree"], stdout=f, stderr=subprocess.DEVNULL, shell=True)

def zip_project_summary(zip_name='project_summary.zip', files_to_include=None):
    """Compacta os arquivos relevantes em um zip."""
    print(f"Compactando arquivos no zip {zip_name}...")
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for file in files_to_include:
            if os.path.exists(file):
                zipf.write(file)
            else:
                print(f"Aviso: {file} não encontrado!")

def clean_up(files):
    """Remove arquivos temporários gerados."""
    for file in files:
        if os.path.exists(file):
            os.remove(file)

def main():
    # Definir arquivos que serão gerados
    files_to_include = ['requirements.txt', 'project_structure.txt', 'README.md']

    # 1. Gerar arquivo de dependências (requirements.txt)
    generate_requirements()

    # 2. Gerar estrutura de diretórios e arquivos
    generate_project_structure()

    # 3. Compactar arquivos relevantes em um zip
    zip_project_summary(files_to_include=files_to_include)

    # 4. Limpar arquivos temporários
    clean_up(['requirements.txt', 'project_structure.txt'])

if __name__ == '__main__':
    main()
