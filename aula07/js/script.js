function calcularProduto() {
    var quantidade = parseInt(document.getElementById("quantidade").value)
    var unidade = parseFloat(document.getElementById("unidade").value)

    var total = quantidade * unidade
    document.getElementById("total").value = total
}

function tabuada() {
    var numero = parseInt(document.getElementById("numero").value)
    for (let i =0; i <= 10; i++) {
        document.write("<p>"+numero+" X "+i+" = "+numero*i+"</p>")
        
    }
}

function analiseNumeros() {
    var n1 = parseInt(document.getElementById("n1").value)
    var n2 = parseInt(document.getElementById("n2").value)

    var result
        if (n1>n2) {
          result = (n1+" é maior que o "+n2)
          
        } else if (n2>n1) {
           result = (n2+" é maior que o "+n1)
           
        } else {
            result = (n1+" é igual ao "+n2)
            
        }

        //document.getElementById("result").value = result

        document.getElementById("result").textContent = result
    }

var salarioBruto // variável global
    
function calcularInss(salarioBruto) {

    let inss //variável local

    if (salarioBruto >= 3000) {
        inss = salarioBruto * 0.11
    } else if (salarioBruto >= 2000) {
        inss = salarioBruto * 0.09
    } else {
        inss = salarioBruto * 0.08
    }
    return inss
}

function valeTransporte (salarioBruto) {

    let vale

    if (salarioBruto >= 3000) {
        vale = salarioBruto * 0.06
    } else {
        vale = salarioBruto * 0.05
    }
    return vale
    
}

function verificarCargo(salarioBruto) {

    let cargo
    
    if (salarioBruto >= 3000) {
        cargo = "Acionista"
    } else if (salarioBruto >= 2000) {
        cargo = "Gerente"
    } else {
        cargo = "Vendedor"
    }
    return cargo
}

function exibirSalario() {
    let sb = parseFloat(document.getElementById("salarioBruto").value)

    if (isNaN(sb) || sb <0) { 
     alert("Digitar um salário bruto válido.")
     document.getElementById("salarioBruto").value = ""
     document.getElementById("inss").value = ""
     document.getElementById("vale").value = ""
     document.getElementById("cargo") = ""
     document.getElementById("salarioLiquido").value = ""
     document.getElementById("salarioBruto").focus()    
    }

    const inss = calcularInss(sb)
    const vale = valeTransporte(sb)
    const liquido = sb - inss - vale

    document.getElementById("inss").value = inss.toFixed(2)
    document.getElementById("vale").value = vale.toFixed(2)
    document.getElementById("cargo").value = verificarCargo(sb)
    document.getElementById("salarioLiquido").value = liquido.toFixed(2)

}
//provas


function verificarSituacao(media) {
    

let situacao
if (media>=7) {
    situacao = "aprovado"
    
} else {
    situacao = "reprovado"
}

}

function calcularResultadoAluno() {

    let p1 = parseFloat(document.getElementById("prova1").value)
    let p2 = parseFloat(document.getElementById("prova2").value)
    let p3 = parseFloat(document.getElementById("prova3").value)
    let md = parseFloat(document.getElementById("media").value)
    let sit = (document.getElementById("situacao").value)

    const media = (p1,p2,p3)/3
    

    document.getElementById("media").value = media.toFixed(2)
    document.getElementById("situacao").value = verificarSituacao(media)
}


    