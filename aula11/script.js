class Cliente{
    constructor(nome,sexo,idade,profissao){
        this.nome = nome
        this.sexo = sexo
        this.idade = idade
        this.profissao = profissao
    }
    exibirInformacao(){
        console.log(`Nome: ${this.nome},Sexo: ${this.sexo},Idade: ${this.idade},Profissao: ${this.profissao}`)
        
        const resultado = document.getElementById("resultado")

        resultado.textContent = `Nome: ${this.nome},Sexo: ${this.sexo},Idade: ${this.idade},Profissao: ${this.profissao}`
    }
}

function pegarDados(){
    let nomeDigitado = document.getElementById("nome").value
    let sexoDigitado = document.getElementById("sexo").value
    let idadeDigitada = document.getElementById("idade").value
    let profissaoDigitada = document.getElementById("profissao").value

    const cliente = new Cliente(nomeDigitado, sexoDigitado, idadeDigitada,profissaoDigitada)
    cliente.exibirInformacao()

}


class Produto{
    constructor(produto,marca){
        this.produto = produto
        this.marca = marca
        
    }
    exibirInformacao(){
        console.log(`Produto: ${this.produto},Marca: ${this.marca}`)
        
        const resultado = document.getElementById("resultado")

        resultado.textContent = `Produto: ${this.produto},Marca: ${this.marca}`
    }
}

function pegarDados(){
    let produtoDigitado = document.getElementById("produto").value
    let marcaDigitada = document.getElementById("marca").value
   
    const cliente = new Produto (produtoDigitado, marcaDigitada)
    cliente.exibirInformacao()

}