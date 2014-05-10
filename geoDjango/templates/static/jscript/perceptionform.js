function sendtoright(){
    selectleft = document.getElementById('id_risque');
    selectright = document.getElementById('id_risqueR');
    console.log(selectleft.name);
    console.log(selectleft);
    for(i=0;i<selectleft.options.length;i++){
        console.log(selectleft.options[i]);
        if(selectleft.options[i].selected){
            selectright.add(selectleft.options[i]);
            selectleft.options[i].remove();
        }
    }
}
document.getElementById('id_risque').onSelect = function(){
    console.log(document.getElementById('id_risque').value);
}