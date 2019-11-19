function sshtelnetCheck() {
    if (document.getElementById('sshCheck').checked) {
        document.getElementById('telnetCon').style.display = 'none';
         document.getElementById('sshCon').style.display = 'block';
    }
    else {
    document.getElementById('sshCon').style.display = 'none';
    document.getElementById('telnetCon').style.display = 'block';}

}