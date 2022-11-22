let deletar = document.querySelectorAll('.deletar')

for(i = 0; i < deletar.length; i++){
    deletar[i].addEventListener('click', function(e){
        if(confirm('Deseja mesmo excluir esssa receita?')){
            return true
        }else{
            return e.preventDefault()
        }
    })
}
