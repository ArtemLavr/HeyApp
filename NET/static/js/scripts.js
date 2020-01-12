function sshtelnetCheck() {
    var tel = document.getElementsByClassName('telnetCon');
    var ssh  = document.getElementsByClassName('sshCon');
    if (document.getElementById('sshCheck').checked) {
       
        for (var i = 0, len =tel.length ; i < len ; i++) {
            tel[i].style.display = 'none';
        }
        for (var i = 0 , len = ssh.length; i< len ; i++) {
            ssh[i].style.display = 'block';
        }    
    }
    else{
        for(var i = 0 , len = tel.length; i< len ; i++)
        {
            tel[i].style.display = 'block';
        }
        for (var i = 0 , len =ssh.length ; i < len  ; i++)
        {
            ssh[i].style.display = 'none';
        }  

        }
}
/*window.onload=function(){
    var aColl = document.getElementsByClassName('a'); //Cache the collection here, so that even a new element added with the same class later we can avoid querying this again by using the cached collection.
    var bColl = document.getElementsByClassName('b');

    document.getElementById('A').addEventListener('mouseover', function(){
        changeColor(aColl, 'red');
    });

    document.getElementById('B').addEventListener('mouseover', function(){
        changeColor(bColl, 'blue');
    });
}
function changeColor(coll, color){

    for(var i=0, len=coll.length; i<len; i++)
    {
        coll[i].style["background-color"] = color;
    }
}*/
