# Contributing do Projeto iTech 🌎
<p>Agradecemos seu interesse e contribuição ao projeto Itech. Seu envolvimento é crucial para o sucesso e evolução contínua do projeto.</p>

<br><br><br>

### Nosso projeto:
Clone nosso repositório do github no seguinte endereço https://github.com/Fcc2187/Projeto-FDS
Acesse nosso figma para desenvolvimento de protótipos de baixa fidelidade: iTech – Figma
Visualize nosso andamento em nossa sprint no Jira: PFDSCS Sprint 2 - PFDSCS - Agile Board - Jira (atlassian.net)
<br>

### Configurações da máquina:
Primeiramente, você deverá se certificar se o ambiente de desenvolvimento de sua máquina está com as configurações corretas:

#### 1- Baixar VsCodeStudio:
 Em seu computador  baixe o app de desenvolvimento VsCodeStudio em : https://code.visualstudio.com/download
 
#### 2- Linguagem de programação Python:
Instale a versão 3.7 ou superior do python  na aba de extensões no VSCodeStudio 
<br>

### Jira:
<P>Em nosso planejamento, usamos o método do Scrumban. Separamos 3 histórias do usuário para serem feitas em sprints (de 3 semanas) dividindo-as em: </p>
<ul>
<li>To-Do</li>
<li>Prototipação Lo-Fi</li>
<li>Prototipada</li>
<li>Implementação</li>
<li>Implementada</li>
<li>Validação</li>
<li>Validada</li>
<li>Concluída</li>
</ul>

<p>Além disso, na criação das histórias dos usuários usamos a seguinte configuração:</p>
<p>1- Proposta de valor (se refere ao que a história irá agregar ao usuário) </p>


<p>2- Cenários de validação:</p>
<p>Dado que…</p>
<p>Quando…</p>
<p>Então…</p>
<br>

### Figma:
No figma você poderá colocar suas ideias em algo palpável e rápido de fazer antes de implementá-lo. É de extrema importância que verifique nos protótipos as viabilidades de novas ideias e histórias para evitar o desperdício de recurso e tempo.
Fique livre para prototipar a história da sua maneira. Desenvolva botões e elementos que essa funcionalidade precisará. 
Não é necessário cor, apenas explicar onde cada elemento ficará e suas funções. 
Nomeie sua história com um título breve e explicativo  
<br>

### Configurações do ambiente e usabilidade:
#### Fork do Repositório: 
<p>Faça um fork do repositório do projeto Itech para sua própria conta do GitHub.</p>

#### - Clone o Repositório: 
<p>Clone o repositório do projeto Itech para o seu ambiente de desenvolvimento local.</p>
<p>No git bash:</p>
<p>git clone https://github.com/Fcc2187/Projeto-FDS.git</p>

#### - Crie um Branch: 
<p>Crie um novo branch para trabalhar em sua contribuição.</p>
<p>No git bash:</p>
<p>git checkout -b nome-do-seu-branch</p>

#### - Ambiente virtual:
<p>Recomendamos a utilização de um ambiente virtual para isolar as dependências do projeto:</p>
<p>Criação do ambiente virtual: python -m venv nome do ambiente virtual</p>
<p>Ativação do ambiente virtual em windows: *nome do ambiente virtual*/Scripts/activate</p> 	
<p>Ativação do ambiente virtual em MacOS ou Linux: *nome do ambiente virtual*/bin/activate</p> 

#### - Instalação de dependências:
<p>pip install django</p>
<p>pip install python-dotenv</p>
<p>Pip install requirements.txt</p>

#### - Configurando o Banco de dados:
Entrando na aba de settings.py localizado no app Itech e configure de acordo com as configurações locais do SQLite 

#### - Criação das tabelas no banco de dados:
python manage.py makemigrations

python manage.py migrate

Com as tabelas do banco de dados criados, execute a seguinte linha de comando para rodar o ambiente virtual:

python manage.py runserver
O servidor local estará rodando em http://127.0.0.1:8000/


#### - Faça as Alterações: 
<p>Faça as alterações necessárias em seu branch local.</p>

#### - Certifique-se de seguir as convenções de codificação e estilo do projeto.

#### - Teste suas Alterações:
<p>Execute os testes locais para garantir que suas alterações não causem regressões.</p>

#### - Salvar Alterações: 
<p>Após testar e garantir que suas alterações não gerem outros problemas, faça o commit e envie para seu repositório forkado.</p>
<p>No git Bash:</p>
<p>git init</p>
<p>git add .</p>
<p>git commit -m "Descrição das mudanças" </p>
<p>git push origin nome-do-seu-branch</p>

#### - Envie um Pull Request: 
Depois de fazer suas alterações, envie um PR para o repositório principal do projeto Itech.
 
#### - Aguarde Feedback: 
Os responsáveis do projeto mandaram os feedbacks apropriados assim que possível.
<br><br>


### - Considerações finais: 
Aqui estão algumas considerações finais a serem lembradas: </p>

<p>1-Comunicação: Mantenha uma comunicação aberta com outros contribuidores e com os mantenedores do projeto. Utilize as plataformas disponíveis (Slack, Discord, ou e-mail) para esclarecer dúvidas e discutir melhorias.</p>

<p>2- Qualidade do Código: Certifique-se de que seu código esteja bem documentado e siga as melhores práticas de codificação. Isso inclui a escrita de comentários claros e a aderência aos padrões de estilo do projeto.</p>

<p>3- Revisões de Código: Esteja preparado para revisões detalhadas do seu código. Feedbacks são oportunidades valiosas para aprendizado e melhoria contínua.</p>

<p>4- Colaboração: Colabore com outros membros da equipe e esteja disposto a ajudar novos contribuidores. Um ambiente colaborativo e de apoio é fundamental para o crescimento do projeto. </p>

<p>5-Atualizações Regulares: Mantenha seu fork do repositório atualizado com o repositório principal para evitar conflitos e garantir que você está trabalhando com a versão mais recente do código. </p>

<p>6-Respeito e Profissionalismo: Trate todos os membros da comunidade com respeito e profissionalismo. Um ambiente positivo e inclusivo é essencial para a produtividade e inovação.</p>
<br>

<p>Se tiver alguma dúvida ou precisar de suporte, não hesite em entrar em contato com a equipe de manutenção do projeto. Estamos aqui para ajudar e garantir que sua experiência como colaborador seja positiva e produtiva. Muito obrigado por sua contribuição ao projeto Itech! Juntos, podemos construir algo incrível. Se precisar de mais informações ou suporte adicional, consulte nossa documentação detalhada ou entre em contato diretamente com um dos mantenedores do projeto. Boas contribuições e bom desenvolvimento!</p>

