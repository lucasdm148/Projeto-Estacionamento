<h1> Projeto Estacionamento </h1>

<p>Este projeto visa criar uma aplicação para o gerenciamento do patio de um estacionamento <br>
⚠️ Atenção!! Projeto Ainda em Desenvolvimento, faltam muitos recursos!!</p>

<h2>⚙️ Funcionamento </h2>
<p>O projeto possui duas tabs: 
  
   * Entrada
   * Saída
  
  Você pode navegar pelas Tabs utilizando Control + Tab
</p>

<h3>Entrada do Veículo </h3>
<p>Basicamente o usuário deve fornecer as caractéristicas do veículo que está entrando no pátio, sendo elas:
  
  * Placa (❗Essa característica é obrigatória)
  * Tipo de Veículo: Se trata de carro ou moto?
  * Cor (Essa característica não é obrigatória)
  * Marca (Essa Característica não é obrigatória)
  
  ![Imagem-Entrada](https://github.com/lucasdm148/Projeto-Estacionamento/assets/86303047/6d448c30-f0c7-4c5a-a115-a535a2c86e14)
  <br>
  
  Se o usuário clicar em "Entrada" sem haver digitado a placa, a seguinte imagem de erro aparecerá na tela: 
  
  ![imagem - erro](https://github.com/lucasdm148/Projeto-Estacionamento/assets/86303047/e65091df-c03f-4b09-a51a-a435e09381c7)
  <br>
  Se o usuário inserir todas as informações corretamente, uma messagebox de confirmação será acionada:
  
 <div align = 'center'>
   <img src = 'https://github.com/lucasdm148/Projeto-Estacionamento/assets/86303047/3a922b54-482b-4a92-a22b-bfc902e4af1f' width = 700px>
</div>
  Ao pressionar Enter ou em ok o veículo será inserido na treewiew. <br><br>
  Se o usuário inserir a placa de um veículo que já esteja no partio, uma messagebox de erro será exibida: <br>
  
 <div align = 'center'>
   <img src = 'https://github.com/lucasdm148/Projeto-Estacionamento/assets/86303047/d39ceaa4-5196-4dd4-8483-a3c10feca582' width = 700px>
</div>
  
  Se o usuário inserir a placa de um veículo cadastrado no banco de dados do sistema como mensalista, a seguinte mensagem de alerta será exibida: 
  
 <div align = 'center'>
   <img src = 'https://github.com/lucasdm148/Projeto-Estacionamento/issues/5#issue-1708267334' width = 700px>
</div>

<p>
  
<h3>Saída de Veículo</h3>
<p>O usuário deve inserir as seguintes informações: 
  
  * Placa do veículo a sair do pátio (Essa informação é obrigatória)
  * Marcar a confirmação se o recibo está carimbado por uma empresa conveniada ou não
  * Caso o recibo esteja carimbado selecionar a empresa conveniada
  Se o usuário não inserir uma placa e ainda assim precionar o botão de saída, uma mensagem de erro também será exibida <br>
  Se o usuário inserir uma placa que não está no patio, uma mensagem de erro será exibida <br>
  Se o usuário marcar o check button de recibo carimbado uma menssagem confirmando a saída do veículo será exibida <br>
  Se o usuário não marcar o check button de recibo carimbado e pressionar enten ou cliclar no botão de sáida uma nova janela será aberta para fazer o cálculo do valor a ser pago e do troco:
  
 <div align = 'center'>
   <img src = 'https://github.com/lucasdm148/Projeto-Estacionamento/assets/86303047/974d87cd-fa98-4529-9ada-db2d8ac83644' width = 700px>
</div>
<br>

<p> Também é possível adicionar um veículo mensalista clicando no menu "Mensalistas" -> "Adicionar Mensalistas", no qual a seguinte janela será aberta</p>
 <div align = 'center'>
   <img src = 'https://github.com/lucasdm148/Projeto-Estacionamento/issues/7#issue-1708293822'>
</div>

<h2>Tecnologias Utilizadas</h2>
<p>Para esse projeto foi utilizado o seguinte Stack:
  
  * Linguagem de programção python3
  * Bibliotecas Tkinter e Custom Tkinter para a criação das GUIs
  * Biblioteca datetime para manipulação de datas e horas
  * Sqlite3 como banco de dados

  Além disso existem diversos recusos de Binding no projeto, como menus pop-ups que acionam ao cliclar com botão direito, clicar duas vezes em uma seleção da treeview e vários outros
</p>
</p>


