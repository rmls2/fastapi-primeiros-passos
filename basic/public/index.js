
async function carregarAnimais(){

    const response =  await axios.get('http://127.0.0.1:8000/animais')

    const animais = response.data
    const lista = document.getElementById('animais-list') //localiza dentro do documento html a tag que tiver com esse ID
    
    animais.forEach(animal => {
        const item = document.createElement('li')  //cria um elemento do tipo li 
        item.innerText = animal.nome  //add um texto que contem em anima.nome a essa tag li 

        lista.appendChild(item) //dentro da tag localizada em lista essa tag filha 
        
    });
}


function manipularFormulario(){
    const form_animal = document.getElementById("form_animal") 
    const input_nome = document.getElementById('nome') //estamos pegando o id do input do campo de texto

    form_animal.onsubmit = async (event) => {
        event.preventDefault()
        const nome_animal = input_nome.value  //o input de nome fica salvo nesse atributo value 
        
        // vamos fazer um post para o nosso backend cujo o corpo da nossa requisição está entre parênteses
        await axios.post('http://127.0.0.1:8000/animais', { 
            nome: nome_animal,
            idade: 8,
            sexo: 'macho',
            cor: 'branco e preto'
        })
       
        // vamos agora fazer um get para o nosso backend pra recuperar a lista de animais 
        const response =  await axios.get('http://127.0.0.1:8000/animais')
        const animais = response.data
        const lista = document.getElementById('animais-list')

        //como o ultimo animal cadastrado é o animal que procuramos, vamos usar o código abaixo para exibi-lo no nosso frontend
        const ultimo_animal = animais[animais.length -1]
        const item = document.createElement('li')
        item.innerText = ultimo_animal.nome
        lista.appendChild(item)

        alert('animal cadastrado!')
    }
}

function app(){
    console.log('App iniciada')
    carregarAnimais()
    manipularFormulario()
}

app()