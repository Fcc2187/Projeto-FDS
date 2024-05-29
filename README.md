<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Projeto iTech</title>
  <style>
    body {
      font-family: Arial, sans-serif;
    }
    .tabs {
      display: flex;
      cursor: pointer;
      padding: 10px;
      background-color: #f1f1f1;
      justify-content: center;
    }
    .tab {
      padding: 10px;
      margin: 0 5px;
      background-color: #ddd;
      border: 1px solid #ccc;
    }
    .tab:hover {
      background-color: #ccc;
    }
    .tab.active {
      background-color: #bbb;
    }
    .content {
      display: none;
      padding: 20px;
      border: 1px solid #ccc;
      border-top: none;
    }
    .content.active {
      display: block;
    }
    .center {
      text-align: center;
    }
  </style>
  <script>
    function showContent(event, contentId) {
      var i, tab, content;
      content = document.getElementsByClassName("content");
      for (i = 0; i < content.length; i++) {
        content[i].classList.remove("active");
      }
      tab = document.getElementsByClassName("tab");
      for (i = 0; i < tab.length; i++) {
        tab[i].classList.remove("active");
      }
      document.getElementById(contentId).classList.add("active");
      event.currentTarget.classList.add("active");
    }
  </script>
</head>
<body>

<hr>
<p align="center">
  <img
    src="https://img.shields.io/github/repo-size/Fcc2187/Projeto-FDS?style=flat"
    alt="Repository Size"
  />
  <img
    src="https://img.shields.io/github/commit-activity/t/Fcc2187/Projeto-FDS?style=flat&logo=github"
    alt="Commit Activity"
  />
  <a href="LICENSE.md">
    <img
      src="https://img.shields.io/github/license/Fcc2187/Projeto-FDS"
      alt="License"
    />
  </a>
</p>

<h1>🔎 Visão Geral</h1>
<p> A iTech é uma aplicação e-commerce que tem como foco a venda de produtos relacionados ao mercado de tecnologia. Aqui, apresentamos aos visitantes deste respositório, o processo de desenvolvimento da aplicação e informações a respeito da nossa trajetória. Somos uma equipe de alunos da CESAR School, desempenhando essa tarefa para a disciplina de Fundamentos de Desenvolvimento de Software. </p>

<h2>⭐ Nossa Equipe</h2>
<p class="center">Bernardo Carneiro Heuer Guimarães</p>
<p class="center">Felipe Cavalcanti Caminha</p>
<p class="center">João Cláudio Beltrão</p>
<p class="center">José Braz de Oliveira Neto</p>
<p class="center">Luiz Felipe Pessoa de Arruda</p>
<p class="center">Miguel Chaves Becker</p>
<p class="center">Rodrigo Torres Marques Rodrigues</p>

<h2>Links</h2>
<p class="center"><a href="https://projeto-fds2.atlassian.net/jira/software/projects/PFDSCS/boards/2">🔗 Jira</a></p>
<p class="center"><a href="https://itechdeployment.azurewebsites.net/">🔗 Azure</a></p>
<p class="center"><a href="https://www.figma.com/file/GNcL8wpzwCpdZfd9ezt2uM/iTech?type=design&node-id=0-1&mode=design&t=nK8iW4muqMOR0FkI-0">🔗 Figma</a></p>
<p class="center"><a href="https://docs.google.com/document/d/1rZFu_fQTW7q7PWi0CVUGxjzFjZWSsbrrWYx7XUuSl2Q/edit?usp=sharing">🔗 Documento do Pair Programming</a></p>

<div class="tabs">
  <div class="tab active" onclick="showContent(event, 'entrega1')">📧 Entrega 1</div>
  <div class="tab" onclick="showContent(event, 'entrega2')">📧 Entrega 2</div>
  <div class="tab" onclick="showContent(event, 'entrega3')">📧 Entrega 3</div>
</div>

<div id="entrega1" class="content active">
  <h2>📧 Entrega 1</h2>
  <i>A Entrega 1 resumiu-se ao desenvolvimento do nosso protótipo de baixa fidelidade, a definição das nossas histórias no Jira e a realização de um screencast do nosso protótipo. Não fui uma entrega muito grande então o grupo conseguiu lidar com a situação sem muita pressão e com tempo de sobra. Contudo, após o lançamento dos resultados dessa entrega, a equipe percebeu a falta de muitos requisitos os quais vieram a ser resolvidos posteriormente na Entrega 2.</i>
  
  <h3>Jira Backlog</h3>
  <img src="https://github.com/Fcc2187/Projeto-FDS/assets/149081961/5d083dbb-9cf1-4044-8a0f-2bfede661333" alt="Repository Size">
  
  <h3>Jira Board</h3>
  <img width="1326" alt="Captura de Tela 2024-03-18 às 10 38 46" src="https://github.com/Fcc2187/Projeto-FDS/assets/151794134/d0253052-1593-452e-87bb-eb2aadac7b60">
  
  <h3>Prototipação Lo-Fi</h3>
  <p class="center"><a href="https://www.figma.com/file/GNcL8wpzwCpdZfd9ezt2uM/iTech?type=design&node-id=0-1&mode=design&t=nK8iW4muqMOR0FkI-0">🔗 Figma</a></p>
  
  <h3>Screencast do Protótipo</h3>
  <p class="center"><a href="https://github.com/Fcc2187/Projeto-FDS/assets/151794134/01de6484-9e14-454a-8ee9-71cf50e0a56b">🔗 Screencast do protótipo Lo-Fi (1)</a></p>
</div>

<div id="entrega2" class="content">
  <h2>📧 Entrega 2</h2>
  <i>Resumo da Entrega 2: Começamos a desenvolver o site do iTech iniciando pela página de suporte, responsável pelo contato para reclamações e assistência aos usuários em suas interações com a equipe de administração. Essa decisão foi tomada considerando a simplicidade da história na sprint. No entanto, enfrentamos alguns contratempos. O principal deles foi que a página inicial acabou sendo a de suporte. Tentamos corrigir esse problema e avançar com o cadastro de usuários, mas as URLs e os modelos de dados permaneceram vinculados ao arquivo "contact_us".
  Diante dessa situação, optamos por revisar, separar e realocar os componentes em um novo projeto, incorporando também as histórias relacionadas ao cadastro de produtos (incluindo imagens), carrinho de compras e filtro por categorias. Decidimos deixar a implementação da página de suporte para a terceira entrega. Como todas as etapas já estão devidamente mapeadas, a compilação dessa história já implementada será mais simplificada.
  O deploy foi realizado sem problemas na região US East, visto que a opção BR South implicaria custos adicionais. Além disso, o nosso issue tracker está atualizado e corrigido em sua totalidade. Também concluímos o screencast das histórias na aplicação web.</i>
  
  <h3>Sprint no Jira</h3>
  <img width="1326" alt="Captura de Tela 2024-03-18 às 10 38 46" src="https://github.com/Fcc2187/Projeto-FDS/assets/142420912/e33bfc6b-3c64-4238-ba67-d255634879f0">
  
  <h3>Bug Tracker</h3>
  <img width="1326" alt="Captura de Tela 2024-03-18 às 10 38 46" src="https://github.com/Fcc2187/Projeto-FDS/assets/149081961/b58612d3-a52f-40cd-a4ad-ab66919f4ab0">
  
  <h3>Screencast do site na Azure</h3>
  <p class="center"><a href="https://drive.google.com/file/d/1OeHCIMXWWTiZKo8qsMu5sF3z1B28_z8t/view?usp=share_link">🔗 Screencast do site</a></p>
</div>

<div id="entrega3" class="content">
  <h2>📧 Entrega 3</h2>
  
  <h3>Sprint 2 Refletindo a Entrega 3</h3>
  <img src="https://github.com/Fcc2187/Projeto-FDS/assets/151794134/e7e5e74b-c852-4996-b6b4-84c06b694970" alt="Sprint 2">
  
  <h3>Backlog</h3>
  <img src="https://github.com/Fcc2187/Projeto-FDS/assets/151794134/056c9640-4835-4a05-9c35-702b2af2e55b" alt="Backlog">
  
  <h3>Deploy das Histórias</h3>
  <p class="center"><a href="https://youtu.be/r0Wov5bPIJw?si=TVDEuYRg3f2prAfk">🔗 Screencast das Histórias no deploy</a></p>
  
  <h3>Bug Tracker</h3>
  <img src="https://github.com/Fcc2187/Projeto-FDS/assets/151794134/b75323dc-38e8-4ccc-95ef-9df9f8ef7a3e" alt="Bug Tracker">
  
  <h3>CI/CD com Build de Deploy Atualizado</h3>
  <p class="center"><a href="https://youtu.be/AD2lcN06BO0?si=bCOJb3v2Wyvjljp8">🔗 Screencast CI/CD</a></p>
  
  <h3>Testes do Sistema</h3>
  <p class="center"><a href="https://youtu.be/eH3Rpc6XIRw?si=31JltYk3SrhnrGP9">🔗 Screencast Testes automatizados</a></p>
  
  <h3>Screencast do Protótipo</h3>
  <p class="center"><a href="https://youtu.be/r1VHVAW8MtQ?feature=shared">🔗 Screencast Prototipo </a></p>
</div>

</body>
</html>
