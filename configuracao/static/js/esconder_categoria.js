var select = document.querySelector('.nice-select')

select.addEventListener('mouseover', function(){
    var esconder_current = document.querySelector('.current')
    esconder_current.classList.add('esconder')
})

select.addEventListener('mouseout', function(){
    var esconder_current = document.querySelector('.current')
    esconder_current.classList.remove('esconder')
})
