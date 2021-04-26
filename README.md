# Melhoria na resolução das imagens com aplicação de redes neurais convolucionais

## Instruções para colaboradores

Use `git clone https://github.com/TCC-CCP48/image-resolution.git` para clonar o repositório na sua máquina

Antes de editar o código crie uma *branch* local `git checkout -b feature/nome-da-branch`

Após editar o código e der `git push` abra um ***Pull Request*** da sua *branch* para a *branch* `develop` e adicione os colaboradores do repositório como revisores (*reviewers*)

Se o seu ***Pull Request*** for aprovado por todos os colaboradores, a sua *branch* será mergeada com a *branch* `develop`, que por sua vez será mergeada com a *branch* `master`
> Esse processo serve para evitar que erros possam ser passados da sua *branch* para a *branch* principal `master`

## Git Cheatsheet

```
# Entra na branch especificada:
git checkout develop  

# Cria uma nova branch:
git checkout -b feature/nome-da-branch

# Puxa o código do repositório da branch atual:   
git pull

# Puxa o código do repositório da branch especificada para a 
branch atual:
git pull origin develop

# Dá o status do processo:
git status

# Adiciona todos os arquivos criados/modificados para a 
branch atual:
git add .

# Faz o commit na branch atual:
git commit -m "Titulo do commit"

# Faz o push da branch atual para o repositório
git push
```